import os
import re
import json
import math
import urllib.request
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

# Inisialisasi token & konfigurasi
SLACK_BOT_TOKEN = os.environ.get("SLACK_BOT_TOKEN")
SLACK_APP_TOKEN = os.environ.get("SLACK_APP_TOKEN")
XAI_API_KEY = os.environ.get("XAI_API_KEY")
XAI_MODEL = os.environ.get("XAI_MODEL", "grok-4.3")
GITHUB_TOKEN = os.environ.get("GITHUB_TOKEN")
GITHUB_REPO = os.environ.get("GITHUB_REPO", "tech-sol-id/cdpk-grok-slack-bot")
SYSTEM_PROMPT = os.environ.get(
    "SYSTEM_PROMPT",
    "Anda adalah asisten AI resmi CDPK HQ yang didukung oleh Grok. Anda HANYA mencari, mengacu, dan menjawab pertanyaan berdasarkan dokumen-dokumen resmi berformat Markdown (.md) CDPK HQ."
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

def is_sync_command(text: str) -> bool:
    """Mendeteksi apakah teks perintah meminta sinkronisasi atau pembaruan basis pengetahuan."""
    t = text.lower().strip()
    keywords = [
        "update knowledge",
        "sync knowledge",
        "sinkronisasi knowledge",
        "perbarui knowledge",
        "update dokumen",
        "sync dokumen",
        "sync drive",
        "update drive",
        "sinkronisasi drive"
    ]
    return any(k in t for k in keywords)

def trigger_cloud_sync() -> tuple:
    """Memicu GitHub Actions workflow untuk menyinkronkan dokumen Google Drive ke Knowledge Base."""
    token = os.environ.get("GITHUB_TOKEN")
    repo = os.environ.get("GITHUB_REPO", "tech-sol-id/cdpk-grok-slack-bot")

    if not token:
        logger.error("GITHUB_TOKEN tidak ditemukan di environment variables.")
        return False, "GITHUB_TOKEN belum dikonfigurasi di server."

    url = f"https://api.github.com/repos/{repo}/actions/workflows/sync_drive.yml/dispatches"
    payload = json.dumps({"ref": "main"}).encode("utf-8")
    req = urllib.request.Request(
        url,
        data=payload,
        headers={
            "Accept": "application/vnd.github+json",
            "Authorization": f"Bearer {token}",
            "User-Agent": "cdpk-grok-slack-bot",
            "Content-Type": "application/json",
        },
        method="POST"
    )

    try:
        with urllib.request.urlopen(req, timeout=15) as resp:
            if resp.status in (200, 204):
                return True, "Berhasil memicu workflow sinkronisasi di GitHub Actions."
            return False, f"Status code tidak terduga: {resp.status}"
    except urllib.error.HTTPError as e:
        err_msg = e.read().decode("utf-8") if e.fp else str(e)
        logger.error(f"Gagal memicu GitHub dispatch (HTTP {e.code}): {err_msg}")
        return False, f"HTTP {e.code}: {err_msg}"
    except Exception as e:
        logger.error(f"Gagal memicu GitHub dispatch: {e}")
        return False, str(e)

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

def extract_smart_snippet(content: str, query_tokens: list, max_length: int = 5000) -> str:
    """Mengekstrak cuplikan cerdas yang berfokus pada bagian dokumen dengan kemunculan kata kunci terbanyak."""
    if len(content) <= max_length:
        return content

    content_lower = content.lower()
    match_positions = []
    for t in query_tokens:
        if len(t) < 3:
            continue
        try:
            for m in re.finditer(r'\b' + re.escape(t) + r'\b', content_lower):
                match_positions.append(m.start())
        except Exception:
            pass

    if not match_positions:
        return content[:max_length]

    match_positions.sort()
    best_pos = match_positions[0]
    max_in_window = 0
    window_span = 2500

    for pos in match_positions:
        count = sum(1 for p in match_positions if pos <= p <= pos + window_span)
        if count > max_in_window:
            max_in_window = count
            best_pos = pos

    start_pos = max(0, best_pos - 600)
    end_pos = min(len(content), start_pos + max_length - 600)
    header = content[:400].strip()

    if start_pos <= 400:
        return content[:max_length]
    else:
        return f"{header}\n\n[... bagian dokumen sebelumnya dilewati ...]\n\n{content[start_pos:end_pos]}"

def retrieve_relevant_knowledge(query: str, user_level: str = "STANDARD", top_k: int = 8) -> str:
    """Mencari dokumen paling relevan dengan pertanyaan pengguna berdasarkan hak akses:
    - DIREKSI: mencari di subfolder umum, finance, dan direksi.
    - FINANCE: mencari di subfolder umum dan finance.
    - STANDARD: hanya mencari di subfolder umum.
    """
    knowledge_dir = os.path.join(os.path.dirname(__file__), "knowledge")
    if not os.path.exists(knowledge_dir):
        return ""

    if user_level == "DIREKSI":
        allowed_subfolders = {"umum", "finance", "direksi"}
    elif user_level == "FINANCE":
        allowed_subfolders = {"umum", "finance"}
    else:
        allowed_subfolders = {"umum"}

    raw_tokens = [t.lower() for t in re.findall(r'[a-zA-Z0-9]+', query) if len(t) >= 2]
    stop_words = {
        "apa", "dan", "yang", "di", "ke", "dari", "ini", "itu", "untuk", "pada", "adalah",
        "saya", "bisa", "bagaimana", "apakah", "ttg", "tentang", "jelaskan", "tolong", "info", "kasih",
        "minta", "berikan", "kirim", "lihat", "cari", "tampilkan", "sebutkan", "dong", "ya", "mohon", "cek"
    }
    search_tokens = [t for t in raw_tokens if t not in stop_words and len(t) >= 3]
    if not search_tokens:
        search_tokens = raw_tokens

    # Deteksi kode model/produk (mengandung kombinasi huruf & angka, misal 'is440', 'slr5000', 'rg170')
    product_codes = [t for t in raw_tokens if any(c.isdigit() for c in t) and any(c.isalpha() for c in t)]

    # Sinonim istilah teknis dari Bahasa Indonesia ke Bahasa Inggris untuk dokumen internasional
    synonyms = {
        "spesifikasi": ["specification", "specifications", "technical features", "datasheet", "features"],
        "spek": ["specification", "specifications", "technical features", "datasheet"],
        "brosur": ["brochure", "flyer"],
        "panduan": ["manual", "guide", "operating manual"],
        "instruksi": ["instructions", "safety"],
    }
    expanded_tokens = list(search_tokens)
    for st in search_tokens:
        if st in synonyms:
            expanded_tokens.extend(synonyms[st])

    phrases = []
    for t in raw_tokens:
        split_parts = re.findall(r'[a-zA-Z]+|\d+', t)
        if len(split_parts) > 1:
            phrases.append(" ".join(split_parts))

    scored_docs = []
    for root, _, files in os.walk(knowledge_dir):
        rel_dir = os.path.relpath(root, knowledge_dir)
        first_segment = rel_dir.split(os.sep)[0] if rel_dir != "." else "."

        # Filter keamanan data level folder
        if first_segment != "." and first_segment not in allowed_subfolders:
            continue

        for file in files:
            # Hanya memproses file berformat Markdown (.md), abaikan hidden file dan readme
            if file.startswith(".") or not file.endswith(".md") or file.lower() == "readme.md":
                continue

            path = os.path.join(root, file)
            try:
                with open(path, "r", encoding="utf-8", errors="ignore") as f:
                    content = f.read()

                fn_lower = file.lower()
                content_lower = content.lower()

                score = 0.0
                matched_token_count = 0

                # 1. Product code matching (sangat spesifik, prioritas tertinggi)
                for pc in product_codes:
                    if pc in fn_lower:
                        score += 800.0
                        matched_token_count += 2
                    elif pc in content_lower:
                        score += 400.0
                        matched_token_count += 1

                # 2. Matching frasa khusus (contoh 'rg 170', 'is 440')
                for ph in phrases:
                    if ph in fn_lower:
                        score += 300.0
                        matched_token_count += 1
                    elif ph in content_lower:
                        score += 150.0
                        matched_token_count += 1

                # 3. Matching token pencarian & sinonim teknis
                for t in expanded_tokens:
                    in_fn = t in fn_lower
                    c = len(re.findall(r'\b' + re.escape(t) + r'\b', content_lower))
                    if in_fn or c > 0:
                        matched_token_count += 1
                        if in_fn:
                            score += 80.0
                        if c > 0:
                            score += (1.0 + math.log(c)) * 25.0

                # 4. Multi-token correlation bonus
                if matched_token_count == len(search_tokens) and len(search_tokens) >= 2:
                    score += 250.0
                elif matched_token_count >= 2:
                    score += matched_token_count * 60.0

                # 5. Boost dokumen profil/overview HANYA jika bukan pencarian kode produk spesifik
                if not product_codes:
                    if any(w in fn_lower for w in ["cdpk_overview", "businessprospect", "prospect", "training", "katalog", "profile"]):
                        score += 150.0

                    if "cdpk_overview" in fn_lower:
                        score += 200.0

                if score > 0:
                    category = first_segment.upper() if first_segment != "." else "UMUM"
                    snippet = extract_smart_snippet(content, search_tokens + product_codes)
                    scored_docs.append((score, file, category, snippet))
            except Exception as e:
                logger.warning(f"Gagal membaca file .md {file}: {e}")

    scored_docs.sort(key=lambda x: x[0], reverse=True)
    top_docs = scored_docs[:top_k]

    if not top_docs:
        overview_path = os.path.join(knowledge_dir, "umum", "cdpk_overview.md")
        if os.path.exists(overview_path):
            try:
                with open(overview_path, "r", encoding="utf-8", errors="ignore") as f:
                    return f"### DOKUMEN [UMUM]: cdpk_overview.md\n{f.read()[:5000]}"
            except Exception:
                pass
        return ""

    docs_formatted = []
    for _, fname, cat, snippet in top_docs:
        docs_formatted.append(f"### DOKUMEN [{cat}]: {fname}\n{snippet}")

    return "\n\n---\n\n".join(docs_formatted)

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

def get_effective_system_prompt(user_access: dict = None, query: str = "") -> str:
    """Menggabungkan System Prompt identitas, Hak Akses Pengguna (3-Tier RBAC), Panduan Rujukan, dan Basis Pengetahuan Relevan."""
    user_name = user_access.get("name", "Anggota Tim") if user_access else "Anggota Tim"
    user_level = user_access.get("level", "STANDARD") if user_access else "STANDARD"
    kb = retrieve_relevant_knowledge(query, user_level)

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

    strict_md_instruction = (
        "🔒 ATURAN KETAT SUMBER PENGETAHUAN & DOMAIN BISNIS CDPK HQ:\n"
        "1. SUMBER TUNGGAL: Anda HANYA diperbolehkan mencari, membaca, dan mendasarkan jawaban Anda pada berkas-berkas resmi berformat Markdown (.md) CDPK HQ yang disediakan di bawah ini.\n"
        "2. DOMAIN BISNIS RESMI: CDPK HQ bergerak di bidang SOLUSI KOMUNIKASI RADIO NIRKABEL PROFESIONAL (Motorola Solutions, FMTCS Solutions, POCStar, Tramigo), PERALATAN OUTDOOR & DIVING (Skywoods), serta PERANGKAT INTRINSICALLY SAFE ATEX/EX (i.Safe Mobile).\n"
        "3. ANTI-HALUSINASI SINGKATAN/ISTILAH: DILARANG KERAS mengartikan singkatan internal/produk (seperti FMTCS, IMS, FMTCS-LRF, POCStar, MCX, DMR, DAS, ATEX, HazLoc) ke bidang lain di luar bisnis telekomunikasi CDPK HQ (contoh: DILARANG mengartikan FMTCS ke bidang perbankan, perbendaharaan, atau keuangan umum). FMTCS adalah penyedia solusi sistem komunikasi nirkabel dan DAS mitra CDPK HQ.\n"
        "4. JIKA TIDAK DITEMUKAN: Jika informasi yang ditanyakan pengguna TIDAK DITEMUKAN dalam berkas Markdown (.md) CDPK HQ (atau penanya tidak berhak mengaksesnya), nyatakan secara jujur: 'Informasi tersebut tidak ditemukan dalam basis data dokumen Markdown (.md) resmi CDPK HQ.'\n"
        "5. KUTIPAN NAMA FILE: SELALU sebutkan nama berkas Markdown (.md) sumber rujukan pada setiap jawaban."
    )

    prompt_parts = [
        SYSTEM_PROMPT,
        rbac_instruction,
        strict_md_instruction
    ]

    if kb:
        prompt_parts.append(
            f"=== BASIS PENGETAHUAN RESMI CDPK HQ (HANYA BERKAS MARKDOWN .MD) ===\n"
            f"Berikut adalah kutipan dokumen Markdown (.md) resmi CDPK HQ yang relevan dengan pertanyaan:\n\n"
            f"{kb}\n"
            f"=== AKHIR BASIS PENGETAHUAN MARKDOWN (.MD) ==="
        )
    else:
        prompt_parts.append(
            "=== BASIS PENGETAHUAN RESMI CDPK HQ (HANYA BERKAS MARKDOWN .MD) ===\n"
            "TIDAK DITEMUKAN berkas Markdown (.md) yang relevan untuk pertanyaan ini di dalam basis data atau dalam cakupan hak akses penanya.\n"
            "Jelaskan kepada penanya bahwa informasi yang dicari tidak ditemukan dalam berkas Markdown (.md) resmi CDPK HQ.\n"
            "=== AKHIR BASIS PENGETAHUAN MARKDOWN (.MD) ==="
        )

    return "\n\n".join(prompt_parts)

def get_thread_context(client, channel: str, thread_ts: str, bot_user_id: str, user_access: dict = None, query: str = "") -> list:
    """Mengambil riwayat percakapan dalam thread agar percakapan memiliki memori/konteks."""
    messages = [{"role": "system", "content": get_effective_system_prompt(user_access, query=query)}]
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

    # 1. Pengecekan Perintah Khusus: Sinkronisasi / Update Knowledge Base dari Drive
    if is_sync_command(user_text):
        if user_access.get("level") == "DIREKSI":
            success, msg = trigger_cloud_sync()
            if success:
                reply = (
                    "🚀 *Sinkronisasi Cloud Dimulai!*\n\n"
                    "Permintaan konversi dokumen Google Drive -> Markdown resmi via **Gemini 3.8 Flash** "
                    "telah berhasil dikirim ke cloud (GitHub Actions).\n\n"
                    "• Dokumen dari Google Drive (termasuk folder shortcut & dokumen baru) sedang diekstraksi.\n"
                    "• Dokumen akan dilengkapi ringkasan, struktur lengkap, FAQ otomatis, dan aturan hak akses 3-tier.\n"
                    "• Grok akan secara otomatis memperbarui memori knowledge base segera setelah proses selesai (~2-3 menit)."
                )
            else:
                reply = f"⚠️ Gagal memicu sinkronisasi cloud: `{msg}`"
        else:
            reply = (
                "🔒 *Akses Dibatasi*\n"
                "Perintah pembaruan/sinkronisasi basis pengetahuan Google Drive hanya dapat dijalankan oleh jajaran *Direksi* CDPK HQ."
            )
        say(text=reply, thread_ts=thread_ts)
        try:
            client.reactions_remove(channel=channel, timestamp=event["ts"], name="thinking_face")
        except Exception:
            pass
        return

    # Ambil konteks jika berada dalam thread, atau buat percakapan baru
    if "thread_ts" in event:
        conversation = get_thread_context(client, channel, thread_ts, bot_user_id, user_access, query=user_text)
    else:
        conversation = [
            {"role": "system", "content": get_effective_system_prompt(user_access, query=user_text)},
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

    # 1. Pengecekan Perintah Khusus: Sinkronisasi / Update Knowledge Base dari Drive via DM
    if is_sync_command(user_text):
        if user_access.get("level") == "DIREKSI":
            success, msg = trigger_cloud_sync()
            if success:
                reply = (
                    "🚀 *Sinkronisasi Cloud Dimulai!*\n\n"
                    "Permintaan konversi dokumen Google Drive -> Markdown resmi via **Gemini 3.8 Flash** "
                    "telah berhasil dikirim ke cloud (GitHub Actions).\n\n"
                    "• Dokumen dari Google Drive (termasuk folder shortcut & dokumen baru) sedang diekstraksi.\n"
                    "• Dokumen akan dilengkapi ringkasan, struktur lengkap, FAQ otomatis, dan aturan hak akses 3-tier.\n"
                    "• Grok akan secara otomatis memperbarui memori knowledge base segera setelah proses selesai (~2-3 menit)."
                )
            else:
                reply = f"⚠️ Gagal memicu sinkronisasi cloud: `{msg}`"
        else:
            reply = (
                "🔒 *Akses Dibatasi*\n"
                "Perintah pembaruan/sinkronisasi basis pengetahuan Google Drive hanya dapat dijalankan oleh jajaran *Direksi* CDPK HQ."
            )
        say(text=reply)
        try:
            client.reactions_remove(channel=event["channel"], timestamp=event["ts"], name="thinking_face")
        except Exception:
            pass
        return

    conversation = [
        {"role": "system", "content": get_effective_system_prompt(user_access, query=user_text)},
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

