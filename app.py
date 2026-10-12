import os
import re
import logging
import threading
from http.server import HTTPServer, BaseHTTPRequestHandler
from dotenv import load_dotenv
from slack_bolt import App
from slack_bolt.adapter.socket_mode import SocketModeHandler
from openai import OpenAI

# Muat variabel environment dari .env
load_dotenv()

logging.basicConfig(level=logging.INFO)
logger = logging.getLogger("slack-grok-bot")

# Inisialisasi token
SLACK_BOT_TOKEN = os.environ.get("SLACK_BOT_TOKEN")
SLACK_APP_TOKEN = os.environ.get("SLACK_APP_TOKEN")
XAI_API_KEY = os.environ.get("XAI_API_KEY")
XAI_MODEL = os.environ.get("XAI_MODEL", "grok-2-mini")
SYSTEM_PROMPT = os.environ.get(
    "SYSTEM_PROMPT",
    "Anda adalah asisten AI resmi CDPK HQ yang didukung oleh Grok. Berikan jawaban yang cerdas, solutif, dan profesional."
)

if not all([SLACK_BOT_TOKEN, SLACK_APP_TOKEN, XAI_API_KEY]):
    logger.warning("Peringatan: Pastikan SLACK_BOT_TOKEN, SLACK_APP_TOKEN, dan XAI_API_KEY sudah diisi di file .env!")

# Inisialisasi Slack App & xAI Client (kompatibel OpenAI)
app = App(token=SLACK_BOT_TOKEN)
ai_client = OpenAI(
    api_key=XAI_API_KEY,
    base_url="https://api.x.ai/v1",
)

def clean_mention(text: str) -> str:
    """Membersihkan mention <@U12345678> dari teks input pengguna."""
    return re.sub(r"<@[A-Z0-9]+>", "", text).strip()

def ask_grok(messages: list) -> str:
    """Mengirim pesan ke xAI Grok API."""
    try:
        response = ai_client.chat.completions.create(
            model=XAI_MODEL,
            messages=messages,
            temperature=0.7,
        )
        return response.choices[0].message.content
    except Exception as e:
        logger.error(f"Error memanggil xAI API: {e}")
        return f"⚠️ Terjadi kendala saat menghubungi Grok API: `{str(e)}`"

def load_knowledge_base() -> str:
    """Membaca semua file Markdown (.md) di folder knowledge/ sebagai basis pengetahuan resmi CDPK HQ."""
    knowledge_dir = os.path.join(os.path.dirname(__file__), "knowledge")
    if not os.path.exists(knowledge_dir):
        return ""

    docs = []
    for root, _, files in os.walk(knowledge_dir):
        for file in sorted(files):
            if file.endswith(".md") and file.lower() != "readme.md":
                path = os.path.join(root, file)
                try:
                    with open(path, "r", encoding="utf-8") as f:
                        content = f.read().strip()
                        if content:
                            docs.append(f"### DOKUMEN: {file}\n{content}")
                except Exception as e:
                    logger.warning(f"Gagal membaca knowledge file {file}: {e}")

    if docs:
        return "\n\n---\n\n".join(docs)
    return ""

# Daftar User ID & Email Resmi CDPK HQ (Diverifikasi Langsung dari Slack API)
DIREKSI_USER_IDS = {"U0C1PULSVUK", "U0C2CR9NAF7", "U0C5FJNKXJR", "U0C6VQR8RT7"}
DIREKSI_EMAILS = {"gama@citradata.id", "adrian@citradata.id", "janice@citradata.id", "rjap@citradata.id"}

FINANCE_USER_IDS = {"U0C6KD2P527", "U0C6V9YCYLC", "U0C502ZV7FA"}
FINANCE_EMAILS = {"sensen@citradata.id", "office@citradata.id", "finance@techsolutions.id"}

def get_user_access_level(client, user_id: str) -> dict:
    """Mengecek profil penanya di Slack untuk menentukan level hak akses secara presisi (Direksi, Finance, Standard)."""
    if not user_id:
        return {"level": "STANDARD", "name": "Anggota Tim", "email": ""}

    # 1. Verifikasi Cepat via User ID Permanen
    if user_id in DIREKSI_USER_IDS:
        return {"level": "DIREKSI", "name": "Direksi CDPK HQ", "email": ""}
    if user_id in FINANCE_USER_IDS:
        return {"level": "FINANCE", "name": "Tim Finance CDPK HQ", "email": ""}

    try:
        user_info = client.users_info(user=user_id).get("user", {})
        profile = user_info.get("profile", {})
        email = profile.get("email", "").lower().strip()
        real_name = profile.get("real_name") or user_info.get("name", "Anggota Tim")
        display_name = (profile.get("display_name") or "").lower()
        title = (profile.get("title") or "").lower()

        # 2. Verifikasi Berlapis via Email Resmi
        if email in DIREKSI_EMAILS or any(d in email for d in ["adrian", "gama", "janice", "rjap"]):
            return {"level": "DIREKSI", "name": real_name, "email": email, "title": profile.get("title", "")}
        if email in FINANCE_EMAILS or any(f in email for f in ["sensen", "finance@"]):
            return {"level": "FINANCE", "name": real_name, "email": email, "title": profile.get("title", "")}

        # 3. Verifikasi via Kata Kunci Jabatan
        if any(t in title for t in ["direktur", "director", "ceo", "cfo", "coo", "cto"]):
            return {"level": "DIREKSI", "name": real_name, "email": email, "title": profile.get("title", "")}
        if any(t in title for t in ["finance", "accounting", "keuangan"]):
            return {"level": "FINANCE", "name": real_name, "email": email, "title": profile.get("title", "")}

        # 4. Default: Staf / Karyawan Umum
        return {"level": "STANDARD", "name": real_name, "email": email, "title": profile.get("title", "")}
    except Exception as e:
        logger.warning(f"Gagal mengambil profil user {user_id}: {e}")
        return {"level": "STANDARD", "name": "Anggota Tim", "email": ""}

def get_effective_system_prompt(user_access: dict = None) -> str:
    """Menggabungkan System Prompt identitas, Hak Akses Pengguna (3-Tier RBAC), Panduan Rujukan, dan Basis Pengetahuan."""
    kb = load_knowledge_base()

    user_name = user_access.get("name", "Anggota Tim") if user_access else "Anggota Tim"
    user_level = user_access.get("level", "STANDARD") if user_access else "STANDARD"

    if user_level == "DIREKSI":
        rbac_instruction = (
            f"👤 IDENTITAS PENANYA: {user_name} (ROLE: DIREKSI CDPK HQ).\n"
            f"OTORITAS AKSES: TERTINGGI (ALL ACCESS).\n"
            f"- Penanya memiliki wewenang penuh untuk mengakses SELURUH informasi CDPK HQ tanpa batasan, termasuk dokumen dari folder 'Slack - Khusus Direksi', folder 'Slack - Finance', dokumen 'Gaji', dan seluruh data finansial perusahaan."
        )
    elif user_level == "FINANCE":
        rbac_instruction = (
            f"👤 IDENTITAS PENANYA: {user_name} (ROLE: TIM FINANCE CDPK HQ).\n"
            f"OTORITAS AKSES: FINANCE & DOKUMEN UMUM.\n"
            f"- Penanya BERHAK mengakses dokumen operasional umum, folder 'Slack - Finance', folder 'Finance and Accounting', dan 'Order Management'.\n"
            f"- BATASAN KETAT: JANGAN PERNAH berikan informasi dari folder 'Slack - Khusus Direksi' atau dokumen dengan judul/tema 'Gaji'. Jika ditanyakan, tolak secara sopan dan jelaskan bahwa dokumen Direksi dan data Penggajian hanya dapat diakses oleh Direksi."
        )
    else:
        rbac_instruction = (
            f"👤 IDENTITAS PENANYA: {user_name} (ROLE: STAF / KARYAWAN UMUM CDPK HQ).\n"
            f"OTORITAS AKSES: DOKUMEN PUBLIK & OPERASIONAL UMUM SAJA.\n"
            f"- Penanya HANYA berhak mengakses informasi SOP dan operasional umum (seperti FMTCS, IMS, Operasional umum, panduan produk, dll).\n"
            f"- BATASAN KETAT: JANGAN PERNAH berikan informasi dari folder 'Finance and Accounting', 'Order Management', 'Slack - Finance', 'Slack - Khusus Direksi', atau informasi bertema 'Gaji'. Jika ditanyakan, tolak dengan sopan dan jelaskan bahwa informasi tersebut bersifat konfidensial dan hanya dapat diakses oleh Tim Finance atau Direksi."
        )

    citation_instruction = (
        "📌 PANDUAN RUJUKAN & SUMBER REFERENSI:\n"
        "- Ketika menjawab pertanyaan seputar SOP, regulasi, atau kebijakan kantor, SELALU sebutkan nama file dokumen sumbernya (contoh: 'Berdasarkan dokumen SOP-X...') yang tertera pada metadata dokumen agar penanya mengetahui dasar rujukannya."
    )

    prompt_parts = [
        SYSTEM_PROMPT,
        rbac_instruction,
        citation_instruction
    ]

    if kb:
        prompt_parts.append(
            f"=== BASIS PENGETAHUAN RESMI CDPK HQ (KNOWLEDGE BASE) ===\n"
            f"Gunakan dokumen rujukan resmi berikut sebagai panduan utama dalam menjawab pertanyaan seputar CDPK HQ:\n\n"
            f"{kb}\n"
            f"=== AKHIR BASIS PENGETAHUAN ==="
        )

    return "\n\n".join(prompt_parts)

def get_thread_context(client, channel: str, thread_ts: str, bot_user_id: str, user_access: dict = None) -> list:
    """Mengambil riwayat percakapan dalam thread agar percakapan memiliki memori/konteks."""
    messages = [{"role": "system", "content": get_effective_system_prompt(user_access)}]
    try:
        result = client.conversations_replies(channel=channel, ts=thread_ts, limit=10)
        for msg in result.get("messages", []):
            role = "assistant" if msg.get("user") == bot_user_id else "user"
            clean_text = clean_mention(msg.get("text", ""))
            if clean_text:
                messages.append({"role": role, "content": clean_text})
    except Exception as e:
        logger.warning(f"Gagal mengambil riwayat thread: {e}")
    return messages

@app.event("app_mention")
def handle_mention(event, say, client):
    """Menangani ketika bot di-mention di channel."""
    channel = event["channel"]
    thread_ts = event.get("thread_ts", event["ts"])
    user_text = clean_mention(event.get("text", ""))

    if not user_text:
        say(text="Halo! Ada yang bisa saya bantu untuk tim CDPK HQ?", thread_ts=thread_ts)
        return

    # Tambahkan reaksi emoji tanda bot sedang memproses
    try:
        client.reactions_add(channel=channel, timestamp=event["ts"], name="thinking_face")
    except Exception:
        pass

    auth_info = client.auth_test()
    bot_user_id = auth_info["user_id"]
    user_id = event.get("user")
    user_access = get_user_access_level(client, user_id)

    # Ambil konteks jika berada dalam thread, atau buat percakapan baru
    if "thread_ts" in event:
        conversation = get_thread_context(client, channel, thread_ts, bot_user_id, user_access)
    else:
        conversation = [
            {"role": "system", "content": get_effective_system_prompt(user_access)},
            {"role": "user", "content": user_text}
        ]

    # Dapatkan jawaban dari Grok
    reply = ask_grok(conversation)

    # Kirim balasan selalu di dalam thread agar rapi
    say(text=reply, thread_ts=thread_ts)

    # Hapus reaksi emoji thinking
    try:
        client.reactions_remove(channel=channel, timestamp=event["ts"], name="thinking_face")
    except Exception:
        pass

@app.event("message")
def handle_direct_message(event, say, client):
    """Menangani pesan langsung (Direct Message) 1-on-1."""
    # Hanya tangani jika tipe channel adalah DM (im) dan pesan bukan dari bot itu sendiri
    if event.get("channel_type") != "im" or event.get("subtype") is not None:
        return

    user_text = event.get("text", "").strip()
    if not user_text:
        return

    try:
        client.reactions_add(channel=event["channel"], timestamp=event["ts"], name="thinking_face")
    except Exception:
        pass

    user_id = event.get("user")
    user_access = get_user_access_level(client, user_id)

    conversation = [
        {"role": "system", "content": get_effective_system_prompt(user_access)},
        {"role": "user", "content": user_text}
    ]

    reply = ask_grok(conversation)
    say(text=reply)

    try:
        client.reactions_remove(channel=event["channel"], timestamp=event["ts"], name="thinking_face")
    except Exception:
        pass

class HealthCheckHandler(BaseHTTPRequestHandler):
    def do_GET(self):
        self.send_response(200)
        self.send_header("Content-type", "text/plain; charset=utf-8")
        self.end_headers()
        self.wfile.write(b"CDPK Grok Slack Bot is running!")

    def log_message(self, format, *args):
        # Mute logging request agar log terminal tetap bersih
        pass

def start_health_server(port: int = 7860):
    server = HTTPServer(("0.0.0.0", port), HealthCheckHandler)
    server.serve_forever()

if __name__ == "__main__":
    port = int(os.environ.get("PORT", 7860))
    health_thread = threading.Thread(target=start_health_server, args=(port,), daemon=True)
    health_thread.start()
    logger.info(f"Health check HTTP server berjalan di port {port}")

    logger.info("Memulai Grok Slack Bot dalam Socket Mode...")
    handler = SocketModeHandler(app, SLACK_APP_TOKEN)
    handler.start()

