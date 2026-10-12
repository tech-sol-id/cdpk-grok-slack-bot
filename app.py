import os
import re
import logging
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

def get_thread_context(client, channel: str, thread_ts: str, bot_user_id: str) -> list:
    """Mengambil riwayat percakapan dalam thread agar percakapan memiliki memori/konteks."""
    messages = [{"role": "system", "content": SYSTEM_PROMPT}]
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

    # Ambil konteks jika berada dalam thread, atau buat percakapan baru
    if "thread_ts" in event:
        conversation = get_thread_context(client, channel, thread_ts, bot_user_id)
    else:
        conversation = [
            {"role": "system", "content": SYSTEM_PROMPT},
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

    conversation = [
        {"role": "system", "content": SYSTEM_PROMPT},
        {"role": "user", "content": user_text}
    ]

    reply = ask_grok(conversation)
    say(text=reply)

    try:
        client.reactions_remove(channel=event["channel"], timestamp=event["ts"], name="thinking_face")
    except Exception:
        pass

if __name__ == "__main__":
    logger.info("Memulai Grok Slack Bot dalam Socket Mode...")
    handler = SocketModeHandler(app, SLACK_APP_TOKEN)
    handler.start()
