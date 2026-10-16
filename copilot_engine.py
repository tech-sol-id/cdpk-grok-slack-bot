import os
import re
import json
import time
import datetime
import threading
import logging
from typing import Optional, Dict, Any, List, Set

logger = logging.getLogger("copilot_engine")

WIB_TZ = datetime.timezone(datetime.timedelta(hours=7))

def get_now_wib() -> datetime.datetime:
    """Mengembalikan waktu saat ini dalam zona waktu WIB (UTC+7)."""
    return datetime.datetime.now(WIB_TZ)

# ==============================================================================
# DAFTAR PILOT DIREKSI & MANAGEMENT (EXECUTIVE CO-PILOT TARGETS)
# ==============================================================================
PILOT_EXECUTIVES: Dict[str, Dict[str, Any]] = {
    "U0C2CR9NAF7": {
        "user_id": "U0C2CR9NAF7",
        "name": "Adrian Bany Kansil (Pak Adrian)",
        "short_name": "Pak Adrian",
        "role": "DIREKSI",
        "title": "Vice Director",
        "email": "adrian@citradata.id",
        "aliases": ["adrian", "pak adrian", "bany", "adrian kansil"]
    },
    "U0C1PULSVUK": {
        "user_id": "U0C1PULSVUK",
        "name": "Gamaliel Alexander Emil Waney (Pak Gama)",
        "short_name": "Pak Gama",
        "role": "DIREKSI",
        "title": "Direktur",
        "email": "gama@citradata.id",
        "aliases": ["gama", "pak gama", "gamaliel"]
    },
    "U0C5FJNKXJR": {
        "user_id": "U0C5FJNKXJR",
        "name": "Janice Jacob Kayan (Bu Janice)",
        "short_name": "Bu Janice",
        "role": "DIREKSI",
        "title": "Direktur Utama",
        "email": "janice@citradata.id",
        "aliases": ["janice", "bu janice", "jen", "bu jen"]
    },
    "U0C6VQR8RT7": {
        "user_id": "U0C6VQR8RT7",
        "name": "Jap Yacob Kayan / Richard (Pak Richard)",
        "short_name": "Pak Richard",
        "role": "DIREKSI",
        "title": "Direktur",
        "email": "rjap@citradata.id",
        "aliases": ["richard", "pak richard", "rjap", "richard jap"]
    },
    "U0C6LAR079B": {
        "user_id": "U0C6LAR079B",
        "name": "Nada Najiha (Bu Nada)",
        "short_name": "Bu Nada",
        "role": "CORP_SECRETARY",
        "title": "Corporate Secretary",
        "email": "ho@citradata.id",
        "aliases": ["nada", "bu nada", "mba nada", "mbak nada", "nada najiha"]
    }
}

# ==============================================================================
# CACHE & STATE UNTUK ZERO-TRUST MEMBERSHIP & CO-PILOT COOLDOWN
# ==============================================================================
_CHANNEL_MEMBERS_CACHE: Dict[str, Dict[str, Any]] = {}
_CHANNEL_LIST_CACHE: Dict[str, Any] = {"channels": [], "expires_at": 0}
_COPILOT_COOLDOWN: Dict[str, float] = {}
_PROACTIVE_SENT_CACHE: Set[str] = set()
_SCHEDULER_STATE_FILE = os.path.join(os.path.dirname(__file__), "logs", "copilot_scheduler_state.json")
_SCHEDULER_LOCK = threading.Lock()
_COPILOT_WORKER_STARTED = False

# Cooldown 180 detik (3 menit) per pasangan (channel_id, target_exec_id) agar hemat token & tidak spam
COOLDOWN_SECONDS = int(os.environ.get("COPILOT_COOLDOWN_SECONDS", "180"))


def get_channel_members_safe(client, channel_id: str, ttl_sec: int = 180) -> Set[str]:
    """
    Mengambil daftar user_id yang merupakan anggota resmi dari suatu channel via Slack API `conversations.members`.
    Menggunakan in-memory cache berumur pendek (default 3 menit) untuk efisiensi API.
    """
    if not client or not channel_id or channel_id.startswith("D"):
        return set()

    now = time.time()
    cached = _CHANNEL_MEMBERS_CACHE.get(channel_id)
    if cached and cached.get("expires_at", 0) > now:
        return cached["members"]

    members_set: Set[str] = set()
    try:
        cursor = None
        while True:
            kwargs = {"channel": channel_id, "limit": 200}
            if cursor:
                kwargs["cursor"] = cursor
            res = client.conversations_members(**kwargs)
            members_set.update(res.get("members", []))
            cursor = res.get("response_metadata", {}).get("next_cursor")
            if not cursor:
                break
        _CHANNEL_MEMBERS_CACHE[channel_id] = {
            "members": members_set,
            "expires_at": now + ttl_sec
        }
    except Exception as e:
        logger.warning(f"Gagal memanggil conversations_members untuk {channel_id}: {e}")
        if cached:
            return cached.get("members", set())
    return members_set


def verify_user_channel_membership(client, user_id: str, channel_id: str) -> bool:
    """
    Memvalidasi secara mutlak (Zero-Trust) apakah `user_id` adalah anggota resmi dari `channel_id`.
    """
    if not user_id or not channel_id:
        return False
    if channel_id.startswith("D"):
        return True
    members = get_channel_members_safe(client, channel_id)
    if not members:
        # Fail-closed: jika gagal mengambil member list channel tertutup, anggap bukan member demi keamanan
        return False
    return user_id in members


def get_workspace_channels_map(client, ttl_sec: int = 300) -> Dict[str, Dict[str, Any]]:
    """
    Mengambil peta seluruh channel yang dapat dilihat bot (nama -> metadata channel, dan id -> metadata channel).
    """
    now = time.time()
    if _CHANNEL_LIST_CACHE.get("expires_at", 0) > now and _CHANNEL_LIST_CACHE.get("map"):
        return _CHANNEL_LIST_CACHE["map"]

    ch_map: Dict[str, Dict[str, Any]] = {}
    # Fallback default untuk #leadership
    ch_map["leadership"] = {"id": "C0C27CR4B5Y", "name": "leadership", "is_private": True}
    ch_map["c0c27cr4b5y"] = {"id": "C0C27CR4B5Y", "name": "leadership", "is_private": True}

    if not client:
        return ch_map

    try:
        res = client.conversations_list(types="public_channel,private_channel", limit=200)
        for c in res.get("channels", []):
            cid = c.get("id", "")
            cname = c.get("name", "").lower()
            meta = {
                "id": cid,
                "name": cname,
                "is_private": bool(c.get("is_private", False)),
                "is_member": bool(c.get("is_member", False))
            }
            if cid:
                ch_map[cid.lower()] = meta
            if cname:
                ch_map[cname] = meta
        _CHANNEL_LIST_CACHE["map"] = ch_map
        _CHANNEL_LIST_CACHE["expires_at"] = now + ttl_sec
    except Exception as e:
        logger.debug(f"Gagal mengambil daftar channel workspace: {e}")

    return ch_map


def check_cross_channel_access_guard(
    client,
    user_id: str,
    user_access: dict,
    current_channel_id: str,
    user_text: str,
    audit_alert_fn=None
) -> Optional[str]:
    """
    SISTEM KEAMANAN MUTLAK (ZERO-TRUST GUARDRAIL — A & C):
    Mendeteksi apabila pengguna (di DM maupun di channel lain) mencoba meminta rekap, ringkasan,
    aktivitas diskusi, atau mengintip isi dari suatu channel yang mana pengguna tersebut BUKAN anggota resminya.
    Jika terdeteksi percobaan akses ilegal:
    1. Menolak permintaan secara tegas (Anti-Inference Protection).
    2. Melaporkan secara real-time via DM ke Pak Adrian (U0C2CR9NAF7).
    """
    if not user_text or not user_id:
        return None

    text_lower = user_text.lower()
    ch_map = get_workspace_channels_map(client)

    # 1. Deteksi penyebutan channel eksplisit format Slack <#C01234567|nama> atau <#C01234567>
    referenced_channels: List[Dict[str, Any]] = []
    explicit_ids = re.findall(r"<#(C[A-Z0-9]+)(?:\|[^>]+)?>", user_text)
    for cid in explicit_ids:
        meta = ch_map.get(cid.lower()) or {"id": cid, "name": cid.lower(), "is_private": True}
        referenced_channels.append(meta)

    # 2. Deteksi penyebutan nama channel dengan tanda pagar #<nama_channel> atau kata "channel <nama>"
    for key, meta in ch_map.items():
        cname = meta.get("name", "")
        if not cname or key == meta.get("id", "").lower():
            continue
        # Cek pola: #leadership, channel leadership, grup leadership, di leadership
        patterns = [
            rf"#{re.escape(cname)}\b",
            rf"\b(?:channel|chanel|saluran|grup|group|room|ruang)\s+#?{re.escape(cname)}\b",
        ]
        # Khusus channel sensitif seperti leadership / grp-finance / tch-finance, deteksi juga jika ada kata pancingan aktivitas/bahasan
        if cname in ["leadership", "grp-finance", "tch-finance"]:
            patterns.append(rf"\b(?:di|dalam|isi|rekap|bahasan|obrolan|diskusi|chat|pesan)\s+#?{re.escape(cname)}\b")
            if cname == "leadership" and re.search(r"\bleadership\b", text_lower):
                # Jika kata 'leadership' disebut bersamaan dengan kata tanya seputar channel/diskusi/rekap/tadi/apa
                inquiry_words = [
                    "channel", "bahas", "diskusi", "rekap", "ringkas", "rangkum", "obrolan", "chat",
                    "pesan", "tadi", "kemarin", "omongin", "bicarakan", "sebut", "tag", "mention", "siapa", "apa"
                ]
                if any(iw in text_lower for iw in inquiry_words):
                    patterns.append(r"\bleadership\b")

        if any(re.search(p, text_lower) for p in patterns):
            if not any(rc.get("id") == meta.get("id") for rc in referenced_channels):
                referenced_channels.append(meta)

    if not referenced_channels:
        return None

    # 3. Validasi keanggotaan resmi via Slack API `conversations.members` untuk setiap channel yang dirujuk
    for target_ch in referenced_channels:
        target_cid = target_ch.get("id", "")
        target_cname = target_ch.get("name", target_cid)

        # Jika user sedang berada di channel itu sendiri, berarti dia anggota
        if current_channel_id and target_cid.upper() == current_channel_id.upper():
            continue

        is_member = verify_user_channel_membership(client, user_id, target_cid)
        if not is_member:
            # TERDETEKSI PERCOBAAN AKSES / INFERENCE CHANNEL TANPA HAK KEANGGOTAAN!
            category_label = f"Zero-Trust Channel Guard — Percobaan Akses/Intip Channel #{target_cname} ({target_cid}) Tanpa Keanggotaan Resmi"
            if audit_alert_fn:
                try:
                    audit_alert_fn(client, user_access, current_channel_id, user_text, category_label)
                except Exception as e:
                    logger.error(f"Gagal memanggil audit_alert_fn pada cross_channel_guard: {e}")

            return (
                f"🔒 *Akses Saluran Ditolak (Zero-Trust Channel Membership Guard)*\n"
                f"Mohon maaf, berdasarkan verifikasi keanggotaan saluran resmi CDPK HQ, Anda *bukan anggota resmi* dari saluran *#{target_cname}*."
            )

    return None


# ==============================================================================
# TAHAP 1: SMART CO-PILOT GHOSTWRITER (KHUSUS JAJARAN DIREKSI & CORP SECRETARY)
# ==============================================================================
def detect_executive_mentions(text: str, sender_id: str) -> List[Dict[str, Any]]:
    """
    Mendeteksi apakah pesan di channel me-mention salah satu dari 5 Target Pengguna Pilot
    (Pak Adrian, Pak Gama, Bu Janice, Pak Richard, Bu Nada) baik melalui Slack tag `<@U...>`
    maupun panggilan nama eksplisit (`@Adrian`, `Pak Adrian`, `Bu Janice`, dll).
    """
    if not text:
        return []

    matched_execs: List[Dict[str, Any]] = []
    seen_ids: Set[str] = set()
    text_lower = text.lower()

    # 1. Cek Slack mention eksplisit <@U...>
    explicit_uids = re.findall(r"<@(U[A-Z0-9]+)>", text)
    for uid in explicit_uids:
        if uid in PILOT_EXECUTIVES and uid != sender_id and uid not in seen_ids:
            matched_execs.append(PILOT_EXECUTIVES[uid])
            seen_ids.add(uid)

    # 2. Cek panggilan nama (@Adrian, Pak Adrian, Bu Janice, Pak Gama, Pak Richard, Bu Nada)
    for uid, profile in PILOT_EXECUTIVES.items():
        if uid == sender_id or uid in seen_ids:
            continue
        for alias in profile.get("aliases", []):
            # Cocokkan '@nama' atau 'pak/bu nama'
            pattern = rf"(?:@{re.escape(alias)}\b|\b(?:pak|bapak|bu|ibu|mba|mbak|ko|koh)\s+{re.escape(alias.replace('pak ', '').replace('bu ', ''))}\b)"
            if re.search(pattern, text_lower):
                matched_execs.append(profile)
                seen_ids.add(uid)
                break

    return matched_execs


def is_meaningful_question_or_request(text: str) -> bool:
    """
    Mengecek apakah pesan yang me-mention Direksi merupakan pertanyaan/permintaan/diskusi bermakna
    (bukan sekadar 'siap pak', 'ok terima kasih pak', dll) agar Co-Pilot tepat guna & hemat token.
    """
    clean = re.sub(r"<@[A-Z0-9]+>", "", text).strip()
    if len(clean) < 12:
        return False

    trivial_phrases = {
        "siap pak", "siap bu", "baik pak", "baik bu", "oke pak", "ok pak", "oke bu", "ok bu",
        "terima kasih pak", "terima kasih bu", "makasih pak", "makasih bu", "noted pak", "noted bu",
        "thank you pak", "thanks pak", "pagi pak", "siang pak", "sore pak", "malam pak"
    }
    if clean.lower().rstrip(".!,") in trivial_phrases:
        return False

    return True


def handle_smart_copilot_ghostwriter(
    client,
    event: dict,
    ask_grok_fn,
    retrieve_kb_fn,
    get_channel_ident_fn
):
    """
    TAHAP 1 (Smart Co-Pilot Ghostwriter) & ATURAN SILENT DROP (Mention Boundary):
    - Berjalan di background thread ketika ada pesan di channel publik/privat.
    - Jika pesan me-mention anggota non-channel di channel tertutup (#leadership), menerapkan SILENT DROP mutlak (tidak melakukan apa-apa untuk non-direksi).
    - Jika pesan me-mention salah satu dari 5 Pilot Direksi/Corp Secretary:
      1. Memverifikasi secara mutlak (`conversations.members`) bahwa Direksi yang di-mention MEMANG anggota resmi channel tersebut. Jika bukan anggota channel tersebut -> SILENT DROP!
      2. Mengecek Cooldown/Debounce agar hemat token dan tidak spam.
      3. Mencari konteks di Knowledge Base CDPK HQ sesuai wewenang Direksi tersebut.
      4. Menyusun Private Co-Pilot Draft (Ringkasan Konteks + Usulan Draf Balasan Siap Kirim) dan mengirimkannya via DM Pribadi ke Direksi yang bersangkutan (TIDAK menjawab di channel publik).
    """
    try:
        channel_id = event.get("channel", "")
        sender_id = event.get("user", "")
        text = event.get("text", "")
        ts = event.get("ts", "")
        thread_ts = event.get("thread_ts") or ts

        if not channel_id or channel_id.startswith("D") or not sender_id or not text:
            return

        # Jangan proses jika pesan juga me-mention bot Grok secara langsung (karena sudah ditangani oleh @app.event("app_mention"))
        try:
            bot_uid = client.auth_test().get("user_id", "")
            if bot_uid and f"<@{bot_uid}>" in text:
                return
        except Exception:
            pass

        # 1. Deteksi apakah ada Pilot Executive yang di-mention
        # CATATAN SILENT DROP (Aturan 2.B):
        # Kami HANYA memproses target yang ada di PILOT_EXECUTIVES, dan di bawah ini wajib diverifikasi
        # keanggotaan channelnya via `verify_user_channel_membership`.
        # Jika ada staf biasa disebut/di-tag di channel tertutup (#leadership), fungsi ini 100% DIAM TOTAL (Silent Drop).
        mentioned_execs = detect_executive_mentions(text, sender_id=sender_id)
        if not mentioned_execs:
            return

        if not is_meaningful_question_or_request(text):
            return

        # Ambil nama pengirim pesan
        sender_name = "Anggota Tim"
        try:
            u_info = client.users_info(user=sender_id).get("user", {})
            sender_name = u_info.get("profile", {}).get("real_name") or u_info.get("name", "Anggota Tim")
        except Exception:
            pass

        ch_name = get_channel_ident_fn(client, channel_id) if get_channel_ident_fn else channel_id

        # Buat permalink pesan agar Direksi bisa langsung klik menuju pesan tersebut
        permalink = ""
        try:
            p_res = client.chat_getPermalink(channel=channel_id, message_ts=ts)
            permalink = p_res.get("permalink", "")
        except Exception:
            pass

        for exec_prof in mentioned_execs:
            exec_uid = exec_prof["user_id"]
            exec_short = exec_prof["short_name"]
            exec_role = exec_prof["role"]

            # 2. ATURAN ZERO-TRUST & SILENT DROP (Mention Boundary):
            # Pastikan Direksi/CorpSec yang di-mention benar-benar anggota resmi channel tempat pesan dikirim!
            if not verify_user_channel_membership(client, exec_uid, channel_id):
                logger.info(
                    f"[SILENT DROP] {exec_short} ({exec_uid}) di-mention di #{ch_name} ({channel_id}), "
                    f"namun bukan anggota channel tersebut. Menerapkan Silent Drop mutlak."
                )
                continue

            # 3. Mekanisme Cooldown / Debounce per (channel_id, exec_uid)
            cooldown_key = f"{channel_id}:{exec_uid}"
            now = time.time()
            last_sent = _COPILOT_COOLDOWN.get(cooldown_key, 0)
            if now - last_sent < COOLDOWN_SECONDS:
                logger.info(
                    f"[CO-PILOT COOLDOWN] Melewati pengiriman draf Co-Pilot untuk {exec_short} di #{ch_name} "
                    f"(masih dalam jeda cooldown {int(COOLDOWN_SECONDS - (now - last_sent))} detik)."
                )
                continue

            _COPILOT_COOLDOWN[cooldown_key] = now

            # 4. Cari materi relevan di Knowledge Base CDPK HQ sesuai role eksekutif
            clean_q = re.sub(r"<@[A-Z0-9]+>", "", text).strip()
            kb_level = "DIREKSI" if exec_role == "DIREKSI" else "STANDARD"
            kb_context = retrieve_kb_fn(clean_q, user_level=kb_level, top_k=5, user_name=exec_prof["name"]) if retrieve_kb_fn else ""

            # Ambil sedikit konteks thread jika berada di dalam thread
            thread_snippet = ""
            if event.get("thread_ts"):
                try:
                    t_res = client.conversations_replies(channel=channel_id, ts=thread_ts, limit=5)
                    t_lines = []
                    for m in t_res.get("messages", [])[-4:]:
                        m_txt = re.sub(r"<@[A-Z0-9]+>", "", m.get("text", "")).strip()
                        if m_txt:
                            t_lines.append(f"- {m_txt[:250]}")
                    if t_lines:
                        thread_snippet = "\n".join(t_lines)
                except Exception:
                    pass

            copilot_system_prompt = (
                f"Anda adalah Executive Smart Co-Pilot & Ghostwriter pribadi untuk {exec_prof['name']} ({exec_prof['title']} CDPK HQ).\n"
                f"Baru saja ada anggota tim ({sender_name}) yang me-mention {exec_short} di channel #{ch_name}.\n\n"
                f"TUGAS ANDA:\n"
                f"1. Analisis singkat inti pertanyaan/permintaan dari {sender_name}.\n"
                f"2. Cari jawaban faktual dan rujukan teknis dari Basis Pengetahuan Resmi CDPK HQ di bawah (Motorola, i.Safe Mobile, FMTCS, RugGear, regulasi, SOP, atau korporat).\n"
                f"3. Susun *Usulan Draf Balasan Siap Kirim (Ghostwriter Draft)* dalam gaya bahasa eksekutif {exec_short} yang tegas, solutif, ramah, dan langsung siap di-copy-paste ke channel #{ch_name}.\n"
                f"4. Gunakan format Slack mrkdwn (*bold* asteris tunggal, bullet •, tanpa tabel pipa markdown).\n\n"
                f"=== BASIS PENGETAHUAN RESMI CDPK HQ ===\n"
                f"{kb_context if kb_context else 'Gunakan pengetahuan standar portofolio CDPK HQ (Motorola, i.Safe Mobile, FMTCS, RugGear, SOP).'}\n"
                f"=== AKHIR BASIS PENGETAHUAN ==="
            )

            user_prompt = (
                f"Pesan dari *{sender_name}* di channel *#{ch_name}*:\n"
                f"\"{clean_q}\"\n\n"
                + (f"Konteks thread sebelumnya:\n{thread_snippet}\n\n" if thread_snippet else "")
                + f"Tolong buatkan:\n"
                f"1. 📌 *Ringkasan Konteks & Data Rujukan CDPK HQ*\n"
                f"2. ✍️ *Draf Balasan Siap Salin untuk {exec_short}* (dalam block quote `>` agar mudah disalin)"
            )

            ai_draft = ask_grok_fn(
                [
                    {"role": "system", "content": copilot_system_prompt},
                    {"role": "user", "content": user_prompt}
                ],
                client=client,
                channel=None,  # Jangan unggah file otomatis ke channel publik
                thread_ts=None,
                user_id=exec_uid
            )

            link_line = f"🔗 *Tautan Pesan Langsung:* <{permalink}|Klik untuk membuka percakapan di #{ch_name}>\n" if permalink else ""
            dm_message = (
                f"🤖 *[EXECUTIVE SMART CO-PILOT — GHOSTWRITER DRAFT]*\n"
                f"Halo *{exec_short}*, Anda baru saja di-mention oleh *{sender_name}* (<@{sender_id}>) di saluran <#{channel_id}> (*#{ch_name}*).\n"
                f"{link_line}"
                f"───────────────────────────────────\n"
                f"💬 *Pesan Masuk:*\n"
                f"> _{clean_q[:500]}_\n\n"
                f"{ai_draft}\n"
                f"───────────────────────────────────\n"
                f"💡 _Pesan ini dikirim secara privat (1-on-1 DM) khusus untuk Anda. Grok tidak membalas di channel publik._"
            )

            # Kirim via DM Pribadi ke Direksi yang di-mention
            try:
                im_res = client.conversations_open(users=exec_uid)
                dm_cid = im_res.get("channel", {}).get("id") or exec_uid
                client.chat_postMessage(channel=dm_cid, text=dm_message, mrkdwn=True)
                logger.info(f"[SMART CO-PILOT] Berhasil mengirim Ghostwriter Draft via DM ke {exec_short} ({exec_uid}) untuk mention di #{ch_name}")
            except Exception as e:
                logger.error(f"Gagal mengirim DM Co-Pilot ke {exec_uid}: {e}")

    except Exception as e:
        logger.error(f"Error pada handle_smart_copilot_ghostwriter: {e}")


# ==============================================================================
# TAHAP 2: SCHEDULE READER (0 TOKEN PYTHON PARSER) & PROACTIVE REMINDER (07:45 WIB)
# ==============================================================================
def parse_local_schedules_zero_token(target_user_id: Optional[str] = None) -> Dict[str, List[Dict[str, Any]]]:
    """
    Membaca jadwal agenda/meeting/pengingat Direksi menggunakan murni parsing Python lokal (0 Token API):
    1. Dari `reminders.json` (jadwal meeting/agenda aktif yang terdaftar di sistem).
    2. Dari file jadwal/agenda di folder `knowledge/` (jadwal rutin mingguan & agenda kegiatan).
    """
    now = get_now_wib()
    today_date = now.date()

    active_today: List[Dict[str, Any]] = []
    upcoming_soon: List[Dict[str, Any]] = []  # 15 - 30 menit ke depan

    # 1. Baca dari reminders.json lokal
    rem_file = os.path.join(os.path.dirname(__file__), "reminders.json")
    if os.path.exists(rem_file):
        try:
            with open(rem_file, "r", encoding="utf-8") as f:
                reminders = json.load(f)
            for r in reminders:
                if r.get("status") != "pending":
                    continue
                due_ts = float(r.get("due_timestamp", 0))
                due_dt = datetime.datetime.fromtimestamp(due_ts, tz=WIB_TZ)
                target_str = str(r.get("target", "")).lower()
                creator_id = r.get("creator_id", "")

                # Filter apakah relevan untuk Direksi target (atau untuk semua/tim/channel)
                if target_user_id:
                    exec_prof = PILOT_EXECUTIVES.get(target_user_id, {})
                    aliases = exec_prof.get("aliases", [])
                    is_relevant = (
                        target_user_id.lower() in target_str
                        or creator_id == target_user_id
                        or any(a in target_str for a in aliases)
                        or target_str in ["tim", "channel", "semua", "here", "direksi", "leadership"]
                    )
                    if not is_relevant:
                        continue

                item = {
                    "id": r.get("id", f"rem_{int(due_ts)}"),
                    "title": r.get("message", "Agenda Terjadwal"),
                    "time_str": due_dt.strftime("%H:%M WIB"),
                    "date_str": due_dt.strftime("%d %b %Y"),
                    "due_timestamp": due_ts,
                    "source": "Kalender Pengingat Slack CDPK"
                }

                if due_dt.date() == today_date:
                    active_today.append(item)

                # Cek apakah jatuh dalam 15 - 30 menit ke depan (900 - 1800 detik)
                diff_sec = due_ts - now.timestamp()
                if 600 <= diff_sec <= 1860:
                    upcoming_soon.append(item)
        except Exception as e:
            logger.debug(f"Gagal mem-parsing reminders.json lokal: {e}")

    # 2. Agenda Rutin Eksekutif CDPK HQ (0 Token Local Calendar Rules)
    weekday = now.weekday()  # 0=Senin .. 4=Jumat
    if weekday == 0:  # Senin
        active_today.append({
            "id": f"routine_mon_{today_date.isoformat()}",
            "title": "Weekly Executive & Department Alignment (Sales, Technical, Finance & Import)",
            "time_str": "09:00 WIB",
            "date_str": now.strftime("%d %b %Y"),
            "due_timestamp": now.replace(hour=9, minute=0, second=0, microsecond=0).timestamp(),
            "source": "Agenda Rutin Mingguan CDPK HQ"
        })
    elif weekday == 4:  # Jumat
        active_today.append({
            "id": f"routine_fri_{today_date.isoformat()}",
            "title": "Review Pipeline Mingguan & Evaluasi Tender/Project berjalan",
            "time_str": "16:00 WIB",
            "date_str": now.strftime("%d %b %Y"),
            "due_timestamp": now.replace(hour=16, minute=0, second=0, microsecond=0).timestamp(),
            "source": "Agenda Rutin Mingguan CDPK HQ"
        })

    # Cek apakah agenda rutin masuk jendela 15-30 menit ke depan
    for ag in active_today:
        if str(ag.get("id", "")).startswith("routine_"):
            diff_sec = ag["due_timestamp"] - now.timestamp()
            if 600 <= diff_sec <= 1860:
                upcoming_soon.append(ag)

    active_today.sort(key=lambda x: x.get("due_timestamp", 0))
    return {"today": active_today, "upcoming_soon": upcoming_soon}


def send_morning_executive_briefing(client, target_only_uid: Optional[str] = None):
    """
    TAHAP 2 (Morning Executive Briefing jam 07:45 WIB — 0 Token Local Python):
    Mengirimkan jadwal agenda/meeting hari ini dan status kesiapan operasional ke DM jajaran Direksi & Corp Secretary.
    """
    now = get_now_wib()
    day_names = ["Senin", "Selasa", "Rabu", "Kamis", "Jumat", "Sabtu", "Minggu"]
    day_str = f"{day_names[now.weekday()]}, {now.strftime('%d %B %Y')}"

    targets = {target_only_uid: PILOT_EXECUTIVES[target_only_uid]} if (target_only_uid and target_only_uid in PILOT_EXECUTIVES) else PILOT_EXECUTIVES

    for exec_uid, prof in targets.items():
        try:
            sched = parse_local_schedules_zero_token(target_user_id=exec_uid)
            today_items = sched.get("today", [])

            if today_items:
                agenda_lines = []
                for idx, it in enumerate(today_items, 1):
                    agenda_lines.append(f"• *{idx}. [{it['time_str']}]* {it['title']} _({it['source']})_")
                agenda_block = "\n".join(agenda_lines)
            else:
                agenda_block = "• _Belum ada jadwal rapat/agenda spesifik yang tercatat untuk pagi ini. Anda dapat menjadwalkan agenda kapan saja melalui DM ini (contoh: \"Ingatkan saya meeting jam 14:00 WIB\")._"

            briefing_text = (
                f"☀️ *[MORNING EXECUTIVE BRIEFING — CDPK HQ]*\n"
                f"Selamat pagi, *{prof['short_name']}*! Berikut adalah ringkasan jadwal & kesiapan agenda Anda untuk *{day_str}*:\n\n"
                f"📅 *JADWAL & AGENDA HARI INI:*\n"
                f"{agenda_block}\n\n"
                f"🛡️ *STATUS SISTEM CO-PILOT:*\n"
                f"• *Smart Ghostwriter:* Aktif (Siap mengirimkan draf jawaban ke DM Anda jika Anda di-mention di channel)\n"
                f"• *Proactive Reminder:* Aktif (Notifikasi otomatis 15–30 menit sebelum agenda dimulai)\n"
                f"• *End-of-Day Digest:* Terjadwal pukul 17:30 WIB sore ini\n\n"
                f"Selamat beraktivitas dan semoga hari Anda produktif! 🚀"
            )

            im_res = client.conversations_open(users=exec_uid)
            dm_cid = im_res.get("channel", {}).get("id") or exec_uid
            client.chat_postMessage(channel=dm_cid, text=briefing_text, mrkdwn=True)
            logger.info(f"[MORNING BRIEFING] Berhasil dikirim ke {prof['short_name']} ({exec_uid})")
        except Exception as e:
            logger.error(f"Gagal mengirim Morning Briefing ke {exec_uid}: {e}")


def check_and_send_proactive_meeting_reminders(client):
    """
    TAHAP 2 (Proactive Reminder 15–30 menit sebelum agenda/meeting — 0 Token Local Python):
    Memeriksa setiap menit apakah ada agenda Direksi yang akan dimulai dalam 15–30 menit ke depan.
    """
    for exec_uid, prof in PILOT_EXECUTIVES.items():
        try:
            sched = parse_local_schedules_zero_token(target_user_id=exec_uid)
            for item in sched.get("upcoming_soon", []):
                dedup_key = f"{exec_uid}:{item['id']}"
                if dedup_key in _PROACTIVE_SENT_CACHE:
                    continue
                _PROACTIVE_SENT_CACHE.add(dedup_key)

                mins_left = max(1, int((item["due_timestamp"] - time.time()) / 60))
                rem_text = (
                    f"🔔 *[PROACTIVE EXECUTIVE REMINDER — {mins_left} MENIT SEBELUM AGENDA]*\n\n"
                    f"Halo *{prof['short_name']}*, mengingatkan bahwa dalam *~{mins_left} menit* lagi Anda memiliki agenda terjadwal:\n\n"
                    f"• 📌 *Agenda:* *{item['title']}*\n"
                    f"• 🕒 *Waktu:* {item['time_str']} ({item['date_str']})\n"
                    f"• 📂 *Sumber:* {item['source']}\n\n"
                    f"_Bila Anda membutuhkan data spesifikasi produk, rekap dokumen Drive, atau draf poin bahasan rapat secara cepat, silakan balas langsung di DM ini._"
                )
                im_res = client.conversations_open(users=exec_uid)
                dm_cid = im_res.get("channel", {}).get("id") or exec_uid
                client.chat_postMessage(channel=dm_cid, text=rem_text, mrkdwn=True)
                logger.info(f"[PROACTIVE REMINDER] Terkirim ke {prof['short_name']} untuk agenda {item['title']}")
        except Exception as e:
            logger.error(f"Gagal memeriksa proactive meeting reminder untuk {exec_uid}: {e}")


# ==============================================================================
# TAHAP 3: END-OF-DAY DIGEST (JAM 17:30 WIB — ZERO-TRUST FILTERED PER EXECUTIVE)
# ==============================================================================
def send_end_of_day_digest(client, ask_grok_fn=None, target_only_uid: Optional[str] = None):
    """
    TAHAP 3 (End-of-Day Digest jam 17:30 WIB):
    Mengirimkan ringkasan diskusi harian dan pending action items ke DM masing-masing Direksi.
    WAJIB MEMATUHI ZERO-TRUST MEMBERSHIP: Setiap Direksi HANYA menerima ringkasan dari channel
    yang mana beliau adalah anggota resminya (`verify_user_channel_membership`).
    """
    now = get_now_wib()
    start_of_day_ts = now.replace(hour=0, minute=0, second=0, microsecond=0).timestamp()
    date_label = now.strftime("%d %B %Y")

    # 1. Kumpulkan aktivitas pesan hari ini dari semua channel tempat bot berada
    ch_map = get_workspace_channels_map(client)
    bot_channels = []
    seen_cids = set()
    for meta in ch_map.values():
        cid = meta.get("id")
        if cid and cid not in seen_cids and meta.get("is_member"):
            seen_cids.add(cid)
            bot_channels.append(meta)

    channel_messages_today: Dict[str, List[str]] = {}
    bot_uid = ""
    try:
        bot_uid = client.auth_test().get("user_id", "")
    except Exception:
        pass

    for ch in bot_channels:
        cid = ch["id"]
        cname = ch["name"]
        try:
            h_res = client.conversations_history(channel=cid, oldest=str(start_of_day_ts), limit=40)
            msgs = h_res.get("messages", [])
            cleaned_lines = []
            for m in reversed(msgs):
                if m.get("bot_id") or m.get("user") == bot_uid or m.get("subtype"):
                    continue
                txt = re.sub(r"<@[A-Z0-9]+>", "", m.get("text", "")).strip()
                if len(txt) >= 10:
                    cleaned_lines.append(f"- {txt[:200]}")
            if cleaned_lines:
                channel_messages_today[cid] = cleaned_lines[-12:]
        except Exception as e:
            logger.debug(f"Gagal membaca history harian untuk #{cname} ({cid}): {e}")

    # 2. Susun dan kirimkan EOD Digest untuk masing-masing Pilot Executive sesuai keanggotaan channelnya
    targets = {target_only_uid: PILOT_EXECUTIVES[target_only_uid]} if (target_only_uid and target_only_uid in PILOT_EXECUTIVES) else PILOT_EXECUTIVES
    for exec_uid, prof in targets.items():
        try:
            allowed_summaries = []
            for ch in bot_channels:
                cid = ch["id"]
                cname = ch["name"]
                if cid not in channel_messages_today:
                    continue
                # ZERO-TRUST CHECK: Hanya sertakan channel jika eksekutif ini adalah anggota resminya!
                if not verify_user_channel_membership(client, exec_uid, cid):
                    continue
                lines = channel_messages_today[cid]
                allowed_summaries.append(f"*#{cname}* ({len(lines)} pesan aktif):\n" + "\n".join(lines[:6]))

            # Ambil pending reminders untuk eksekutif ini
            sched = parse_local_schedules_zero_token(target_user_id=exec_uid)
            pending_rems = sched.get("today", [])
            rem_lines = [f"• [{r['time_str']}] {r['title']}" for r in pending_rems] if pending_rems else ["• _Tidak ada pending reminder yang tertunda._"]

            if allowed_summaries and ask_grok_fn:
                raw_digest_input = "\n\n".join(allowed_summaries)
                eod_prompt = [
                    {
                        "role": "system",
                        "content": (
                            f"Anda adalah Executive AI Co-Pilot CDPK HQ untuk {prof['name']} ({prof['title']}). "
                            "Buat ringkasan eksekutif sore hari (End-of-Day Digest) yang sangat padat, rapi, dan fokus pada: "
                            "(1) Poin Diskusi Utama per Saluran, dan (2) Pending Action Items / Tindak Lanjut. "
                            "Gunakan format Slack mrkdwn (*bold* satu bintang, bullet •, tanpa tabel pipa)."
                        )
                    },
                    {
                        "role": "user",
                        "content": f"Berikut aktivitas diskusi hari ini ({date_label}) di saluran yang diikuti {prof['short_name']}:\n\n{raw_digest_input}"
                    }
                ]
                ai_summary = ask_grok_fn(eod_prompt, client=client, channel=None, thread_ts=None, user_id=exec_uid)
            elif allowed_summaries:
                ai_summary = "\n\n".join(allowed_summaries)
            else:
                ai_summary = "• _Hari ini tidak terdapat diskusi baru yang memerlukan tindak lanjut mendesak di saluran yang Anda ikuti._"

            eod_text = (
                f"🌇 *[END-OF-DAY EXECUTIVE DIGEST — {date_label}]*\n"
                f"Selamat sore, *{prof['short_name']}*! Berikut adalah rangkuman diskusi harian & tindak lanjut dari saluran resmi yang Anda ikuti:\n\n"
                f"📊 *RINGKASAN DISKUSI & ACTION ITEMS HARI INI:*\n"
                f"{ai_summary}\n\n"
                f"⏰ *STATUS AGENDA & PENGINGAT HARI INI:*\n"
                + "\n".join(rem_lines)
                + "\n\n_Selamat beristirahat! Grok CDPK tetap siaga 24/7 mendampingi Anda._ 🙏"
            )

            im_res = client.conversations_open(users=exec_uid)
            dm_cid = im_res.get("channel", {}).get("id") or exec_uid
            client.chat_postMessage(channel=dm_cid, text=eod_text, mrkdwn=True)
            logger.info(f"[EOD DIGEST] Berhasil dikirim ke {prof['short_name']} ({exec_uid})")
        except Exception as e:
            logger.error(f"Gagal mengirim EOD Digest ke {exec_uid}: {e}")


# ==============================================================================
# BACKGROUND SCHEDULER WORKER (07:45 WIB, 17:30 WIB, & PROACTIVE 15-30 MIN)
# ==============================================================================
def _load_scheduler_state() -> Dict[str, str]:
    with _SCHEDULER_LOCK:
        if not os.path.exists(_SCHEDULER_STATE_FILE):
            return {}
        try:
            with open(_SCHEDULER_STATE_FILE, "r", encoding="utf-8") as f:
                return json.load(f)
        except Exception:
            return {}


def _save_scheduler_state(state: Dict[str, str]):
    with _SCHEDULER_LOCK:
        try:
            os.makedirs(os.path.dirname(_SCHEDULER_STATE_FILE), exist_ok=True)
            with open(_SCHEDULER_STATE_FILE, "w", encoding="utf-8") as f:
                json.dump(state, f, indent=2)
        except Exception as e:
            logger.debug(f"Gagal menyimpan state scheduler Co-Pilot: {e}")


def _copilot_scheduler_loop(client, ask_grok_fn=None):
    logger.info("Executive Co-Pilot Scheduler (Tahap 2 & Tahap 3) aktif dan berjalan 24/7...")
    while True:
        try:
            now = get_now_wib()
            today_str = now.strftime("%Y-%m-%d")
            hh_mm = now.strftime("%H:%M")

            state = _load_scheduler_state()

            # 1. Morning Executive Briefing setiap pukul 07:45 WIB (Senin - Sabtu)
            if hh_mm == "07:45" and state.get("last_morning_briefing") != today_str:
                state["last_morning_briefing"] = today_str
                _save_scheduler_state(state)
                send_morning_executive_briefing(client)

            # 2. End-of-Day Digest setiap pukul 17:30 WIB (Senin - Sabtu)
            if hh_mm == "17:30" and state.get("last_eod_digest") != today_str:
                state["last_eod_digest"] = today_str
                _save_scheduler_state(state)
                send_end_of_day_digest(client, ask_grok_fn=ask_grok_fn)

            # 3. Proactive Meeting Reminder (15 - 30 menit sebelum agenda)
            check_and_send_proactive_meeting_reminders(client)

        except Exception as e:
            logger.error(f"Error pada loop scheduler Co-Pilot: {e}")

        time.sleep(30)


def start_copilot_worker(client, ask_grok_fn=None):
    """Menjalankan background worker Co-Pilot (Morning Briefing 07:45, Proactive Reminder, & EOD Digest 17:30)."""
    global _COPILOT_WORKER_STARTED
    if not _COPILOT_WORKER_STARTED:
        _COPILOT_WORKER_STARTED = True
        t = threading.Thread(target=_copilot_scheduler_loop, args=(client, ask_grok_fn), daemon=True)
        t.start()
        logger.info("Thread Executive Co-Pilot worker berhasil diinisialisasi.")
