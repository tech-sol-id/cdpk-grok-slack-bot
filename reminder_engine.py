import os
import json
import time
import datetime
import threading
import logging
from typing import List, Dict, Optional

logger = logging.getLogger("reminder_engine")

REMINDERS_FILE = os.path.join(os.path.dirname(__file__), "reminders.json")
_lock = threading.Lock()
_worker_started = False

WIB_TZ = datetime.timezone(datetime.timedelta(hours=7))

def get_now_wib() -> datetime.datetime:
    """Mengembalikan waktu saat ini dalam zona waktu WIB (UTC+7)."""
    return datetime.datetime.now(WIB_TZ)

def format_wib_time(epoch_sec: float) -> str:
    """Format timestamp epoch ke format tanggal & waktu WIB yang mudah dibaca."""
    dt = datetime.datetime.fromtimestamp(epoch_sec, tz=WIB_TZ)
    return dt.strftime("%d %B %Y pukul %H:%M WIB")

def load_reminders() -> List[Dict]:
    """Membaca daftar pengingat dari berkas JSON."""
    with _lock:
        if not os.path.exists(REMINDERS_FILE):
            return []
        try:
            with open(REMINDERS_FILE, "r", encoding="utf-8") as f:
                return json.load(f)
        except Exception as e:
            logger.error(f"Gagal membaca reminders.json: {e}")
            return []

def save_reminders(reminders: List[Dict]):
    """Menyimpan daftar pengingat ke berkas JSON secara aman."""
    with _lock:
        try:
            with open(REMINDERS_FILE, "w", encoding="utf-8") as f:
                json.dump(reminders, f, indent=2, ensure_ascii=False)
        except Exception as e:
            logger.error(f"Gagal menyimpan reminders.json: {e}")

def add_reminder(
    creator_id: str,
    channel: str,
    target: str,
    message: str,
    delay_seconds: int,
    target_time_description: str = "",
    recurrence: str = "none",
    thread_ts: Optional[str] = None
) -> Dict:
    """Menjadwalkan pengingat baru."""
    now_ts = time.time()
    due_ts = now_ts + max(5, int(delay_seconds))
    due_time_formatted = format_wib_time(due_ts)
    
    # Generate unique ID
    reminder_id = f"rem_{int(now_ts)}_{os.urandom(2).hex()}"
    
    reminder_obj = {
        "id": reminder_id,
        "creator_id": creator_id,
        "channel": channel,
        "thread_ts": thread_ts,
        "target": target or "tim",
        "message": message,
        "due_timestamp": due_ts,
        "due_time_str": due_time_formatted,
        "target_time_description": target_time_description or due_time_formatted,
        "recurrence": recurrence if recurrence in ["none", "daily", "weekly_monday", "weekly_friday"] else "none",
        "status": "pending",
        "created_at": get_now_wib().isoformat()
    }
    
    reminders = load_reminders()
    reminders.append(reminder_obj)
    save_reminders(reminders)
    
    logger.info(f"Pengingat dijadwalkan [{reminder_id}] untuk '{target}' pada {due_time_formatted}")
    return reminder_obj

def list_active_reminders(channel: Optional[str] = None) -> List[Dict]:
    """Mengambil daftar pengingat yang berstatus pending."""
    reminders = load_reminders()
    active = [r for r in reminders if r.get("status") == "pending"]
    if channel:
        active = [r for r in active if r.get("channel") == channel]
    # Urutkan berdasarkan waktu paling dekat
    active.sort(key=lambda x: x.get("due_timestamp", 0))
    return active

def cancel_reminder(identifier: str, channel: Optional[str] = None) -> bool:
    """Membatalkan pengingat berdasarkan ID atau kata kunci pesan."""
    reminders = load_reminders()
    matched = False
    ident_lower = identifier.lower().strip()
    
    for r in reminders:
        if r.get("status") == "pending":
            if channel and r.get("channel") != channel:
                continue
            # Cocokkan ID atau bagian dari teks pesan
            if r.get("id") == identifier or ident_lower in r.get("message", "").lower():
                r["status"] = "cancelled"
                matched = True
                logger.info(f"Pengingat {r.get('id')} berhasil dibatalkan.")
                break
                
    if matched:
        save_reminders(reminders)
    return matched

def check_and_trigger_reminders(client):
    """Memeriksa pengingat yang telah jatuh tempo dan mengirim pesan ke Slack."""
    now_ts = time.time()
    reminders = load_reminders()
    updated = False
    
    for r in reminders:
        if r.get("status") == "pending" and r.get("due_timestamp", 0) <= now_ts:
            channel = r.get("channel")
            target = r.get("target", "tim")
            msg_text = r.get("message", "")
            creator_id = r.get("creator_id", "")
            recurrence = r.get("recurrence", "none")
            thread_ts = r.get("thread_ts")
            
            # Format target mention jika berupa ID user
            if target.startswith("U0") or target.startswith("W0"):
                target_mention = f"<@{target}>"
            elif target.lower() in ["saya", "me"]:
                target_mention = f"<@{creator_id}>" if creator_id else "Anda"
            elif target.lower() in ["channel", "here", "semua"]:
                target_mention = "<!channel>"
            else:
                target_mention = target
                
            creator_mention = f"<@{creator_id}>" if creator_id else "CDPK Assistant"
            
            # Buat pesan pengingat resmi CDPK HQ
            slack_text = (
                f"⏰ *PENGINGAT CDPK HQ*\n"
                f"📌 *Penerima:* {target_mention}\n"
                f"📋 *Pesan:* {msg_text}\n"
                f"👤 *Dijadwalkan oleh:* {creator_mention}\n"
                f"🕒 *Waktu Pengingat:* {r.get('due_time_str')}"
            )
            
            if recurrence != "none":
                slack_text += f"\n🔄 *Pengulangan:* `{recurrence}`"
                
            try:
                client.chat_postMessage(
                    channel=channel,
                    thread_ts=thread_ts,
                    text=slack_text,
                    mrkdwn=True
                )
                logger.info(f"Pesan pengingat [{r.get('id')}] berhasil dikirim ke {channel}")
            except Exception as e:
                logger.error(f"Gagal mengirim pesan pengingat ke Slack: {e}")
                
            # Tangani pengulangan (recurrence)
            if recurrence == "daily":
                r["due_timestamp"] = now_ts + 86400  # +24 jam
                r["due_time_str"] = format_wib_time(r["due_timestamp"])
            elif recurrence == "weekly_monday" or recurrence == "weekly_friday":
                r["due_timestamp"] = now_ts + (7 * 86400)  # +7 hari
                r["due_time_str"] = format_wib_time(r["due_timestamp"])
            else:
                r["status"] = "triggered"
                
            updated = True
            
    if updated:
        save_reminders(reminders)

def _reminder_worker_loop(client, interval: int = 15):
    """Loop worker latar belakang yang berjalan setiap interval detik."""
    logger.info("Reminder background worker aktif dan berjalan...")
    while True:
        try:
            check_and_trigger_reminders(client)
        except Exception as e:
            logger.error(f"Error di loop reminder worker: {e}")
        time.sleep(interval)

def start_reminder_worker(client):
    """Menjalankan background worker thread jika belum berjalan."""
    global _worker_started
    if not _worker_started:
        _worker_started = True
        worker_thread = threading.Thread(target=_reminder_worker_loop, args=(client,), daemon=True)
        worker_thread.start()
        logger.info("Thread reminder worker berhasil diinisialisasi.")

# Tool definitions untuk Grok Function Calling
REMINDER_TOOLS = [
    {
        "type": "function",
        "function": {
            "name": "set_reminder",
            "description": "Menjadwalkan pengingat (reminder) otomatis untuk anggota tim, diri sendiri, atau channel. Bot akan otomatis mengirim notifikasi ke Slack saat waktunya tiba.",
            "parameters": {
                "type": "object",
                "properties": {
                    "target": {
                        "type": "string",
                        "description": "Target yang diingatkan (contoh: '<@U0C2CR9NAF7>', 'Richard', 'saya', 'tim finance', 'channel')"
                    },
                    "reminder_message": {
                        "type": "string",
                        "description": "Isi pesan atau hal yang harus diingatkan"
                    },
                    "delay_seconds": {
                        "type": "integer",
                        "description": "Selisih waktu dari sekarang dalam hitungan detik hingga pengingat dibunyikan. Contoh: 10 menit = 600, 1 jam = 3600, besok pagi jam 9 = selisih detik dari waktu server saat ini."
                    },
                    "target_time_description": {
                        "type": "string",
                        "description": "Deskripsi waktu dalam bahasa manusia (contoh: 'Besok jam 09:00 WIB', '30 menit lagi', 'Hari Senin jam 08:30 WIB')"
                    },
                    "recurrence": {
                        "type": "string",
                        "enum": ["none", "daily", "weekly_monday", "weekly_friday"],
                        "description": "Pengulangan pengingat: 'none' (sekali), 'daily' (tiap hari), 'weekly_monday' (tiap Senin), 'weekly_friday' (tiap Jumat)"
                    }
                },
                "required": ["reminder_message", "delay_seconds"]
            }
        }
    },
    {
        "type": "function",
        "function": {
            "name": "list_reminders",
            "description": "Melihat daftar pengingat (reminder) yang sedang aktif dan dijadwalkan.",
            "parameters": {
                "type": "object",
                "properties": {}
            }
        }
    },
    {
        "type": "function",
        "function": {
            "name": "cancel_reminder",
            "description": "Membatalkan pengingat yang sedang aktif berdasarkan ID pengingat atau kata kunci pesan.",
            "parameters": {
                "type": "object",
                "properties": {
                    "reminder_id": {
                        "type": "string",
                        "description": "ID pengingat (contoh 'rem_...') atau kata kunci pesan pengingat yang ingin dibatalkan"
                    }
                },
                "required": ["reminder_id"]
            }
        }
    }
]
