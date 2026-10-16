import os
import re
import json
import time
import math
import base64
import requests
import urllib.request
import logging
import threading
from typing import Optional, Dict, Any, List
from http.server import HTTPServer, BaseHTTPRequestHandler
from dotenv import load_dotenv
from slack_bolt import App
from slack_bolt.adapter.socket_mode import SocketModeHandler
from openai import OpenAI
from doc_engine import generate_bom_excel, generate_proposal_docx, upload_document_to_slack, DOC_TOOLS
from reminder_engine import (
    add_reminder,
    list_active_reminders,
    cancel_reminder,
    start_reminder_worker,
    get_now_wib,
    REMINDER_TOOLS
)
from web_search_engine import perform_web_search, read_web_page_content, WEB_TOOLS
from gdrive_engine import search_google_drive, read_google_drive_file, GDRIVE_TOOLS

ALL_TOOLS = DOC_TOOLS + REMINDER_TOOLS + WEB_TOOLS + GDRIVE_TOOLS

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
    "Anda adalah Grok CDPK, Executive AI Strategic Advisor & Solutions Architect resmi CDPK HQ (PT Citradata Purnakharisma & Techsolutions). "
    "Anda mendampingi Direksi, Manajemen, dan Tim Profesional dalam perancangan solusi teknis nirkabel, arsitektur sistem, strategi tender bisnis, pembuatan dokumen resmi, dan pengingat operasional dengan komunikasi yang lugas, elegan, dan profesional."
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

def download_and_convert_media(client, files: list) -> list:
    """Mengunduh gambar atau mengekstrak halaman pertama PDF yang dilampirkan di Slack untuk Grok Vision menggunakan requests."""
    if not files:
        return []

    media_items = []
    token = getattr(client, "token", None) or os.environ.get("SLACK_BOT_TOKEN")

    for f in files:
        file_id = f.get("id")
        fname = f.get("name", "attachment")
        mimetype = f.get("mimetype", "")
        url = f.get("url_private_download") or f.get("url_private")

        # Jika metadata file belum lengkap, fetch via files.info API
        if not url and file_id:
            try:
                f_info = client.files_info(file=file_id).get("file", {})
                url = f_info.get("url_private_download") or f_info.get("url_private")
                mimetype = f_info.get("mimetype", mimetype)
                fname = f_info.get("name", fname)
            except Exception as e:
                logger.warning(f"Gagal mengambil detail files.info untuk {file_id}: {e}")

        if not url:
            continue

        # Deteksi fallback mimetype berdasarkan ekstensi
        fn_lower = fname.lower()
        if not mimetype or mimetype == "application/octet-stream":
            if fn_lower.endswith((".png", ".jpg", ".jpeg", ".webp", ".gif")):
                mimetype = f"image/{'jpeg' if fn_lower.endswith(('.jpg', '.jpeg')) else fn_lower.split('.')[-1]}"
            elif fn_lower.endswith(".pdf"):
                mimetype = "application/pdf"

        try:
            resp = requests.get(
                url,
                headers={"Authorization": f"Bearer {token}", "User-Agent": "cdpk-grok-slack-bot"},
                timeout=25
            )
            if resp.status_code != 200:
                logger.warning(f"HTTP {resp.status_code} saat mengunduh file {fname} dari Slack")
                continue

            data = resp.content
            if not data or b"<!DOCTYPE html>" in data[:100] or b"<html" in data[:100]:
                logger.warning(f"File {fname} mengembalikan HTML login alih-alih data binary valid")
                continue

            # 1. File berupa gambar langsung (PNG, JPEG, WebP, GIF)
            if mimetype.startswith("image/"):
                b64_str = base64.b64encode(data).decode("utf-8")
                media_items.append({
                    "type": "image_url",
                    "image_url": {"url": f"data:{mimetype};base64,{b64_str}"}
                })
                logger.info(f"Berhasil memuat gambar lampiran Slack: {fname} ({mimetype}, {len(data)} bytes)")

            # 2. File berupa dokumen PDF (skema blueprint / denah arsitektur)
            elif mimetype == "application/pdf" or fn_lower.endswith(".pdf"):
                try:
                    import fitz  # PyMuPDF
                    doc = fitz.open(stream=data, filetype="pdf")
                    if len(doc) > 0:
                        page = doc[0]
                        pix = page.get_pixmap(dpi=150)
                        png_bytes = pix.tobytes("png")
                        b64_str = base64.b64encode(png_bytes).decode("utf-8")
                        media_items.append({
                            "type": "image_url",
                            "image_url": {"url": f"data:image/png;base64,{b64_str}"}
                        })
                        logger.info(f"Berhasil merender halaman PDF {fname} ke gambar untuk Grok Vision")
                        doc.close()
                except Exception as e:
                    logger.warning(f"Gagal mengonversi PDF {fname} ke gambar via PyMuPDF: {e}")
        except Exception as e:
            logger.warning(f"Gagal mengunduh file lampiran {fname} dari Slack: {e}")

    return media_items

def get_media_items_for_message(client, channel: str, event: dict) -> list:
    """Mengekstrak seluruh media gambar/PDF dari pesan Slack (dari event langsung, conversations.replies, atau riwayat thread)."""
    # 1. Cek langsung dari event jika ada files
    event_files = event.get("files", [])
    if event_files:
        items = download_and_convert_media(client, event_files)
        if items:
            return items

    # 2. Ambil dari Slack API (karena Slack sering menghilangkan 'files' pada event app_mention)
    target_ts = event.get("ts")
    thread_ts = event.get("thread_ts") or target_ts

    try:
        res = client.conversations_replies(channel=channel, ts=thread_ts, limit=15)
        messages = res.get("messages", [])

        # Cari pada pesan pemicu (ts yang sama)
        for m in messages:
            if m.get("ts") == target_ts and m.get("files"):
                items = download_and_convert_media(client, m.get("files", []))
                if items:
                    logger.info(f"Berhasil mengekstrak media pada pesan pemicu mention (ts: {target_ts})")
                    return items

        # Jika belum ada, periksa pesan-pesan sebelumnya dalam thread (dari yang paling baru)
        auth_test_user = ""
        try:
            auth_test_user = client.auth_test().get("user_id", "")
        except Exception:
            pass

        for m in reversed(messages):
            if m.get("files") and m.get("user") != auth_test_user:
                items = download_and_convert_media(client, m.get("files", []))
                if items:
                    logger.info(f"Berhasil mengekstrak media dari konteks thread (ts: {m.get('ts')})")
                    return items
    except Exception as e:
        logger.warning(f"Gagal memeriksa conversations_replies untuk file lampiran: {e}")

    # 3. Failsafe: Cek conversations.history jika belum ditemukan
    if target_ts:
        try:
            h_res = client.conversations_history(channel=channel, latest=target_ts, inclusive=True, limit=2)
            for m in h_res.get("messages", []):
                if m.get("ts") == target_ts and m.get("files"):
                    items = download_and_convert_media(client, m.get("files", []))
                    if items:
                        logger.info(f"Berhasil mengekstrak media via conversations_history (ts: {target_ts})")
                        return items
        except Exception as e:
            logger.warning(f"Gagal memeriksa conversations_history untuk file lampiran: {e}")

    return []

def format_slack_text(text: str) -> str:
    """Mengonversi teks jawaban Grok menjadi format tampilan Slack Executive yang bersih dan rapi (tanpa tabel pipa dan tanpa istilah teknis file markdown)."""
    if not text:
        return ""

    # 1. Bersihkan penyebutan istilah teknis file markdown
    text = re.sub(r"basis data dokumen Markdown \(\.md\) resmi CDPK HQ", "basis pengetahuan resmi CDPK HQ", text, flags=re.IGNORECASE)
    text = re.sub(r"dokumen Markdown \(\.md\) resmi CDPK HQ", "basis pengetahuan resmi CDPK HQ", text, flags=re.IGNORECASE)
    text = re.sub(r"berkas Markdown \(\.md\)", "dokumen resmi", text, flags=re.IGNORECASE)
    text = re.sub(r"dokumen Markdown \(\.md\)", "dokumen resmi", text, flags=re.IGNORECASE)
    text = re.sub(r"\bberkas-berkas resmi berformat Markdown \(\.md\)", "arsip dokumen resmi", text, flags=re.IGNORECASE)
    text = re.sub(r"\b([a-zA-Z0-9_\-]+)\.md\b", r"*\1*", text)
    text = re.sub(r"\bSumber dokumen resmi:\s*", "📚 *Rujukan Resmi:* ", text, flags=re.IGNORECASE)

    # 2. Konversi tabel markdown pipa (| col1 | col2 |) menjadi bullet cards yang rapi di Slack
    lines = text.split("\n")
    out = []
    i = 0
    while i < len(lines):
        line = lines[i].strip()
        if line.startswith("|") and line.endswith("|") and i + 1 < len(lines):
            next_line = lines[i+1].strip()
            if next_line.startswith("|") and ("---" in next_line or "-:-" in next_line):
                headers = [h.strip() for h in line.strip("|").split("|")]
                i += 2
                table_rows = []
                while i < len(lines) and lines[i].strip().startswith("|") and lines[i].strip().endswith("|"):
                    row_vals = [v.strip() for v in lines[i].strip("|").split("|")]
                    table_rows.append(row_vals)
                    i += 1

                card_lines = []
                for idx, row in enumerate(table_rows, 1):
                    title_parts = []
                    detail_parts = []
                    for h, val in zip(headers, row):
                        if not val or val == "-":
                            continue
                        h_lower = h.lower()
                        if any(k in h_lower for k in ["no", "nomor"]):
                            continue
                        elif any(k in h_lower for k in ["komponen", "nama", "produk", "perangkat", "item", "description"]):
                            title_parts.append(val)
                        elif any(k in h_lower for k in ["model", "part number", "tipe", "type"]):
                            title_parts.append(f"`{val}`")
                        elif any(k in h_lower for k in ["qty", "kuantitas", "jumlah"]):
                            detail_parts.append(f"*Qty:* {val}")
                        elif any(k in h_lower for k in ["harga", "price"]):
                            detail_parts.append(f"*Harga:* {val}")
                        elif any(k in h_lower for k in ["keterangan", "fungsi", "lokasi", "notes"]):
                            detail_parts.append(f"_{val}_")
                        else:
                            detail_parts.append(f"*{h}:* {val}")

                    header_str = " — ".join(title_parts) if title_parts else f"Item {idx}"
                    card_lines.append(f"• *{idx}. {header_str}*")
                    if detail_parts:
                        card_lines.append(f"   └─ " + " | ".join(detail_parts))

                out.append("\n".join(card_lines))
                continue
        out.append(lines[i])
        i += 1
    text = "\n".join(out)

    # 3. Ubah heading markdown ### atau ## menjadi bold ber-emoji untuk Slack
    text = re.sub(r"^###\s+(.+)$", r"🔹 *\1*", text, flags=re.MULTILINE)
    text = re.sub(r"^##\s+(.+)$", r"📌 *\1*", text, flags=re.MULTILINE)
    text = re.sub(r"^#\s+(.+)$", r"🚀 *\1*", text, flags=re.MULTILINE)

    # 4. Ubah **bold** ganda menjadi *bold* tunggal khas Slack mrkdwn
    text = re.sub(r"\*\*([^\*]+)\*\*", r"*\1*", text)

    # 5. Hilangkan backtick pada kutipan dokumen yang kaku
    text = re.sub(r"`\*([^\*]+)\*`", r"*\1*", text)

    # 6. Konversi tautan markdown [Label](url) menjadi format tautan Slack resmi <url|Label>
    text = re.sub(r'\[([^\]]+)\]\((https?://[^\)]+)\)', r'<\2|\1>', text)

    return text

def ask_grok(messages: list, client=None, channel: str = None, thread_ts: str = None, user_id: str = None) -> str:
    """Mengirim pesan ke xAI Grok API dengan dukungan Tool Calling untuk Dokumen & Reminder."""
    try:
        response = None
        for attempt in range(3):
            try:
                response = ai_client.chat.completions.create(
                    model=XAI_MODEL,
                    messages=messages,
                    tools=ALL_TOOLS,
                    tool_choice="auto",
                    temperature=0.7,
                )
                break
            except Exception as e:
                if "429" in str(e) or "capacity" in str(e).lower():
                    logger.warning(f"xAI API 429 capacity spike (attempt {attempt+1}/3), retrying in 2.5s...")
                    time.sleep(2.5)
                else:
                    raise e

        if not response:
            return "⚠️ Server Grok sedang mengalami lonjakan beban kapasitas sementara. Mohon coba ulangi dalam beberapa saat."

        msg = response.choices[0].message

        # Jika Grok memanggil tool (generate dokumen atau reminder)
        if msg.tool_calls:
            tool_call_messages = list(messages)
            tool_call_messages.append(msg)
            u_access = get_user_access_level(client, user_id) if client and user_id else {"level": "STANDARD"}
            u_level = u_access.get("level", "STANDARD")
            uploaded_notices = []

            for tc in msg.tool_calls:
                fn_name = tc.function.name
                fn_args = json.loads(tc.function.arguments)
                tool_output_str = ""

                # 1. Tool Dokumen: Excel BOM
                if fn_name == "generate_bom_excel":
                    pname = fn_args.get("project_name", "Proyek_CDPK")
                    cname = fn_args.get("client_name", "")
                    items = fn_args.get("items", [])
                    fpath = generate_bom_excel(pname, cname, items)
                    fname = os.path.basename(fpath)
                    tool_output_str = f"File Excel BOM '{fname}' berhasil dibuat."
                    if client and channel:
                        ok = upload_document_to_slack(
                            client, channel, thread_ts, fpath,
                            title=f"BOM Excel - {pname}",
                            initial_comment=f"📊 *File Excel Bill of Materials (BOM) resmi CDPK HQ* untuk proyek *{pname}* telah selesai dibuat dan siap diunduh:"
                        )
                        if ok:
                            uploaded_notices.append(f"• File Excel BOM: `{fname}` (telah diunggah ke chat)")
                        else:
                            uploaded_notices.append(f"• File Excel BOM `{fname}` berhasil dibuat di server.")

                # 2. Tool Dokumen: Word Proposal
                elif fn_name == "generate_proposal_docx":
                    pname = fn_args.get("project_name", "Proyek_CDPK")
                    cname = fn_args.get("client_name", "")
                    scope = fn_args.get("scope_summary", "")
                    topo = fn_args.get("topology_description", "")
                    items = fn_args.get("items", [])
                    notes = fn_args.get("technical_notes", "")
                    fpath = generate_proposal_docx(pname, cname, scope, topo, items, notes)
                    fname = os.path.basename(fpath)
                    tool_output_str = f"Dokumen Word Proposal '{fname}' berhasil dibuat."
                    if client and channel:
                        ok = upload_document_to_slack(
                            client, channel, thread_ts, fpath,
                            title=f"Proposal Teknis Word - {pname}",
                            initial_comment=f"📄 *Dokumen Proposal Desain Teknis Word (.docx) resmi CDPK HQ* untuk proyek *{pname}* telah selesai dibuat dan siap diunduh:"
                        )
                        if ok:
                            uploaded_notices.append(f"• Dokumen Word Proposal: `{fname}` (telah diunggah ke chat)")
                        else:
                            uploaded_notices.append(f"• Dokumen Word `{fname}` berhasil dibuat di server.")

                # 3. Tool Reminder: Set Reminder
                elif fn_name == "set_reminder":
                    target = fn_args.get("target", "tim")
                    rem_msg = fn_args.get("reminder_message", "")
                    delay_sec = fn_args.get("delay_seconds", 60)
                    target_time_desc = fn_args.get("target_time_description", "")
                    recurrence = fn_args.get("recurrence", "none")
                    rem_obj = add_reminder(
                        creator_id=user_id or "",
                        channel=channel or "",
                        target=target,
                        message=rem_msg,
                        delay_seconds=delay_sec,
                        target_time_description=target_time_desc,
                        recurrence=recurrence,
                        thread_ts=thread_ts
                    )
                    tool_output_str = (
                        f"Pengingat berhasil dijadwalkan (ID: {rem_obj['id']}) untuk {target} "
                        f"pada {rem_obj['due_time_str']} (deskripsi: {rem_obj['target_time_description']})."
                    )

                # 4. Tool Reminder: List Reminders
                elif fn_name == "list_reminders":
                    active_rems = list_active_reminders(channel=channel)
                    if not active_rems:
                        tool_output_str = "Saat ini tidak ada pengingat aktif yang terjadwal di channel ini."
                    else:
                        lines = ["Daftar pengingat aktif saat ini:"]
                        for idx, r in enumerate(active_rems, 1):
                            lines.append(
                                f"{idx}. [{r['id']}] Target: {r['target']} | Pesan: \"{r['message']}\" "
                                f"| Jadwal: {r['due_time_str']} (ulang: {r['recurrence']})"
                            )
                        tool_output_str = "\n".join(lines)

                # 5. Tool Reminder: Cancel Reminder
                elif fn_name == "cancel_reminder":
                    rem_ident = fn_args.get("reminder_id", "")
                    success = cancel_reminder(rem_ident, channel=channel)
                    if success:
                        tool_output_str = f"Pengingat '{rem_ident}' berhasil dibatalkan."
                    else:
                        tool_output_str = f"Pengingat '{rem_ident}' tidak ditemukan di daftar aktif."

                # 6. Tool Web Search: Live Internet Search
                elif fn_name == "perform_web_search":
                    query_term = fn_args.get("query", "")
                    tool_output_str = perform_web_search(query_term)

                # 7. Tool Web Search: Read Web Page Content
                elif fn_name == "read_web_page_content":
                    target_url = fn_args.get("url", "")
                    tool_output_str = read_web_page_content(target_url)

                # 8. Tool Google Drive: Search Google Drive
                elif fn_name == "search_google_drive":
                    g_query = fn_args.get("query", "")
                    g_acc = fn_args.get("account", "all")
                    tool_output_str = search_google_drive(g_query, account=g_acc, user_access=u_access)

                # 9. Tool Google Drive: Read Google Drive File
                elif fn_name == "read_google_drive_file":
                    fid = fn_args.get("file_id", "")
                    g_acc = fn_args.get("account", "citradata")
                    tool_output_str = read_google_drive_file(fid, account=g_acc, user_access=u_access)

                tool_call_messages.append({
                    "role": "tool",
                    "tool_call_id": tc.id,
                    "content": tool_output_str
                })

            final_resp = None
            for attempt in range(3):
                try:
                    final_resp = ai_client.chat.completions.create(
                        model=XAI_MODEL,
                        messages=tool_call_messages,
                        temperature=0.7,
                    )
                    break
                except Exception as e:
                    if "429" in str(e) or "capacity" in str(e).lower():
                        logger.warning(f"xAI final completion 429 spike (attempt {attempt+1}/3), retrying in 2.5s...")
                        time.sleep(2.5)
                    else:
                        raise e

            if not final_resp:
                return "⚠️ Server Grok sedang mengalami lonjakan beban kapasitas sementara. Mohon coba ulangi dalam beberapa saat."

            content = final_resp.choices[0].message.content or ""
            if uploaded_notices:
                content += "\n\n" + "\n".join(uploaded_notices)
            return format_slack_text(content)

        return format_slack_text(msg.content or "")
    except Exception as e:
        logger.error(f"Error memanggil xAI API: {e}")
        return f"⚠️ Terjadi kendala saat menghubungi Grok API: `{str(e)}`"

def extract_smart_snippet(content: str, query_tokens: list, max_length: int = 7500) -> str:
    """Mengekstrak cuplikan cerdas yang berfokus pada bagian dokumen dengan kemunculan kata kunci terbanyak."""
    # Untuk file data tabel/rekap/analisis karyawan (panjang sedang tapi sangat padat), jangan potong agar tidak kehilangan baris data
    header_peek = content[:400].lower()
    if len(content) <= 25000 and any(h in header_peek for h in ["employee id", "nama pegawai", "gaji bruto", "ptkp status", "nip,status"]):
        return content

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
    window_span = 3000

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

def retrieve_relevant_knowledge(query: str, user_level: str = "STANDARD", top_k: int = 8, user_name: str = "") -> str:
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

    # Normalisasi teks query (contoh i.safe, i-safe -> isafe)
    cleaned_query = query.lower()
    cleaned_query = re.sub(r'i[\.\-_ ]safe', 'isafe', cleaned_query)

    raw_tokens = [t.lower() for t in re.findall(r'[a-zA-Z0-9]+', cleaned_query) if len(t) >= 2]
    stop_words = {
        "apa", "dan", "yang", "di", "ke", "dari", "ini", "itu", "untuk", "pada", "adalah",
        "saya", "bisa", "bagaimana", "apakah", "ttg", "tentang", "jelaskan", "tolong", "info", "kasih",
        "minta", "berikan", "kirim", "lihat", "cari", "tampilkan", "sebutkan", "dong", "ya", "mohon", "cek",
        "data", "arsip", "dokumen", "file", "berkas", "semua", "ada", "gak", "nggak", "nya",
        "pak", "bu", "bapak", "ibu", "nomer", "nomor", "siapa", "berapa"
    }
    search_tokens = [t for t in raw_tokens if t not in stop_words and len(t) >= 3]
    if not search_tokens:
        search_tokens = [t for t in raw_tokens if t not in stop_words] or raw_tokens

    # Jika kueri mengandung kata personal ('saya', 'ku', 'milik'), sertakan token nama user
    name_tokens = []
    if user_name and any(w in cleaned_query for w in ["saya", "ku", "pribadi", "diri", "milik"]):
        name_tokens = [t.lower() for t in re.findall(r'[a-zA-Z0-9]+', user_name) if len(t) >= 3 and t.lower() not in {"pak", "ibu", "bapak", "anggota", "tim"}]
        search_tokens.extend(name_tokens)

    # Kamus alias merek & lini produk CDPK HQ
    brand_aliases = {
        "isafe": ["is540", "is440", "is940", "is945", "is530", "i_safe", "isafe", "atex", "iecex", "intrinsically", "zone"],
        "conquest": ["conquest", "ex201", "s23", "s29", "rugged"],
        "ruggear": ["rg880", "rg725", "rg655", "rg170", "ruggear"],
        "motorola": ["slr5000", "slr8000", "r7", "mototrbo", "xir", "repeater"],
        "fmtcs": ["omub", "orub", "das", "coupler", "splitter", "fmtcs", "lrf"],
        "skywoods": ["diving", "outdoor", "flashlight", "senter"],
        "tramigo": ["mcptt", "t360", "mission critical"],
        "pocstar": ["poc", "ptt", "broadband", "walkie-talkie"],
    }

    expanded_tokens = list(search_tokens)
    if name_tokens:
        expanded_tokens.extend(name_tokens)
    for st in search_tokens:
        if st in brand_aliases:
            expanded_tokens.extend(brand_aliases[st])

    # Deteksi kode model/produk (mengandung kombinasi huruf & angka, misal 'is540', 'is440', 'slr5000', 'rg170')
    product_codes = [t for t in expanded_tokens if any(c.isdigit() for c in t) and any(c.isalpha() for c in t)]

    # Sinonim istilah teknis dari Bahasa Indonesia ke Bahasa Inggris untuk dokumen internasional & istilah HR/Finance
    synonyms = {
        "spesifikasi": ["specification", "specifications", "technical features", "datasheet", "features"],
        "spek": ["specification", "specifications", "technical features", "datasheet"],
        "brosur": ["brochure", "flyer"],
        "panduan": ["manual", "guide", "operating manual"],
        "instruksi": ["instructions", "safety"],
        "topologi": ["topology", "das", "riser", "omu", "oru", "antenna", "splitter", "coupler", "coverage"],
        "desain": ["design", "das", "omu", "oru", "architecture", "diagram"],
        "gambar": ["diagram", "schematic", "blueprint", "plan", "riser"],
        # HR, Gaji, Payroll & Absensi
        "salary": ["gaji", "payroll", "upah", "thp", "remunerasi", "penghasilan", "tunjangan", "rekap_gaji"],
        "gaji": ["salary", "payroll", "upah", "thp", "remunerasi", "penghasilan", "tunjangan", "rekap", "rekap_gaji"],
        "payroll": ["salary", "gaji", "upah", "thp", "remunerasi", "rekap_gaji"],
        "upah": ["gaji", "salary", "payroll", "thp", "tunjangan"],
        "thp": ["take home pay", "gaji", "salary", "payroll", "penghasilan"],
        "tunjangan": ["allowance", "gaji", "salary", "makan", "transport", "jabatan"],
        "absensi": ["kehadiran", "presensi", "attendance", "absen", "cuti", "izin", "sakit", "terlambat", "talenta", "mekari", "ketidakhadiran"],
        "kehadiran": ["absensi", "presensi", "attendance", "absen", "cuti", "izin", "sakit", "terlambat", "talenta", "mekari", "ketidakhadiran"],
        "absen": ["absensi", "kehadiran", "presensi", "attendance", "cuti", "izin", "terlambat"],
        "presensi": ["absensi", "kehadiran", "attendance", "absen"],
        "karyawan": ["employee", "pegawai", "staf", "staff", "personalia", "hrd", "sdm"],
        "pegawai": ["karyawan", "employee", "staf", "staff", "personalia", "hrd", "sdm"],
        "personalia": ["karyawan", "pegawai", "hrd", "absensi", "gaji"],
        "hrd": ["personalia", "karyawan", "pegawai", "absensi", "talenta"],
        "nip": ["employee id", "nik", "nomor induk", "employee_analysis", "data karyawan", "pegawai", "rekap_gaji"],
        "nik": ["nip", "employee id", "nomor induk", "employee_analysis", "ktp"],
        "ktp": ["nik", "identitas", "employee_analysis"],
        "npwp": ["pajak", "employee_analysis"],
    }
    for st in list(expanded_tokens):
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

                # 5. Boost dokumen profil/overview HANYA jika kueri menanyakan profil/tentang perusahaan
                if any(w in cleaned_query for w in ["profil", "profile", "tentang cdpk", "tentang perusahaan", "sejarah", "overview", "latar belakang"]):
                    if any(w in fn_lower for w in ["cdpk_overview", "profile", "company_profile"]):
                        score += 250.0

                # 6. Boost dokumen gaji jika kueri menyangkut gaji/salary/payroll
                if any(w in cleaned_query for w in ["gaji", "salary", "payroll", "upah", "thp", "remunerasi"]):
                    if any(w in fn_lower for w in ["rekap_gaji", "gaji", "payroll"]):
                        score += 350.0

                # 7. Boost dokumen absensi/karyawan jika kueri menyangkut absensi/karyawan
                if any(w in cleaned_query for w in ["absen", "absensi", "kehadiran", "presensi", "talenta"]):
                    if any(w in fn_lower for w in ["rekap_gaji", "employee", "karyawan", "personalia", "peraturan_perusahaan"]):
                        score += 250.0

                # 8. Boost dokumen data karyawan & personalia jika kueri menyangkut NIP/NIK/KTP/karyawan
                if any(w in cleaned_query for w in ["nip", "nik", "ktp", "npwp", "karyawan", "pegawai", "staf", "staff", "personalia", "identitas"]):
                    if any(w in fn_lower for w in ["employee_analysis", "rekap_gaji", "karyawan", "personalia"]):
                        score += 350.0

                if score > 0:
                    category = first_segment.upper() if first_segment != "." else "UMUM"
                    snippet = extract_smart_snippet(content, expanded_tokens + product_codes, max_length=7500)
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

# Profil Anggota Terdaftar Resmi CDPK HQ (disinkronkan dengan data database payroll & karyawan)
USER_OFFICIAL_PROFILES = {
    "U0C1PULSVUK": {"name": "Gamaliel Alexander Emil Waney (Pak Gama)", "role": "DIREKSI", "email": "gama@citradata.id", "title": "Direktur"},
    "U0C2CR9NAF7": {"name": "Adrian Bany Kansil (Pak Adrian)", "role": "DIREKSI", "email": "adrian@citradata.id", "title": "Vice Director", "is_adrian": True},
    "U0C5FJNKXJR": {"name": "Janice Jacob Kayan (Bu Janice)", "role": "DIREKSI", "email": "janice@citradata.id", "title": "Direktur Utama"},
    "U0C6VQR8RT7": {"name": "Jap Yacob Kayan / Richard (Pak Richard)", "role": "DIREKSI", "email": "rjap@citradata.id", "title": "Direktur"},
    "U0C6LAR079B": {"name": "Nada Najiha (Bu Nada)", "role": "CORP_SECRETARY", "email": "ho@citradata.id", "title": "Corporate Secretary"},
    "U0C6KD2P527": {"name": "Oey Sin Seng / Sen Sen (Pak Sen Sen)", "role": "FINANCE", "email": "sensen@citradata.id", "title": "Finance & Accounting Manager"},
    "U0C6V9YCYLC": {"name": "Ririn (Bu Ririn)", "role": "FINANCE", "email": "office@citradata.id", "title": "Finance & Office"},
    "U0C502ZV7FA": {"name": "Villa Aulia (Bu Villa)", "role": "FINANCE", "email": "finance@techsolutions.id", "title": "Finance Techsolutions"},
}

# ==============================================================================
# CHANNEL PRIVACY GUARD & DATA LOSS PREVENTION (DLP)
# ==============================================================================
LEADERSHIP_CHANNELS = {"leadership", "c0c27cr4b5y"}
FINANCE_CHANNELS = {"leadership", "c0c27cr4b5y", "grp-finance", "tch-finance"}

SENSITIVE_DIREKSI_KEYWORDS = [
    "corporate", "direksi", "bod drive", "hrd", "personalia", "legalitas", "akta",
    "gaji", "payroll", "salary", "upah", "dividen", "komisi", "bonus", "saham",
    "remunerasi", "persuratan", "surat keputusan", "surat kuasa", "notulen", "rups",
    "nip", "nik", "ktp", "npwp", "karyawan", "pegawai", "nomor induk", "data pribadi",
    "profil karyawan", "rekap gaji", "slip gaji", "thp", "cuti karyawan", "absensi karyawan",
    "kontak karyawan", "alamat karyawan"
]

SENSITIVE_FINANCE_KEYWORDS = [
    "finance", "accounting", "keuangan", "order management", "invoice", "faktur",
    "kas kecil", "laba rugi", "neraca", "rekening", "po customer", "purchase order"
]

_CHANNEL_NAME_CACHE = {"c0c27cr4b5y": "leadership"}

def get_channel_identifier(client, channel_id: str) -> str:
    """Mengambil nama channel secara cerdas (dengan caching) untuk verifikasi DLP."""
    if not channel_id:
        return ""
    if channel_id.startswith("D"):
        return "im"
    ch_key = channel_id.lower()
    if ch_key in _CHANNEL_NAME_CACHE:
        return _CHANNEL_NAME_CACHE[ch_key]
    try:
        if client:
            info = client.conversations_info(channel=channel_id).get("channel", {})
            c_name = info.get("name", "").lower()
            if c_name:
                _CHANNEL_NAME_CACHE[ch_key] = c_name
                return c_name
    except Exception as e:
        logger.debug(f"conversations_info gagal untuk {channel_id}: {e}")
    return ch_key

def check_user_has_permission(user_level: str, is_direksi_req: bool, is_finance_req: bool, text_lower: str) -> bool:
    """Mengecek apakah pengguna memiliki hak akses/wewenang sesuai role ke data yang diminta."""
    if user_level == "DIREKSI":
        return True

    if is_direksi_req:
        if user_level == "CORP_SECRETARY":
            # Corporate Secretary BISA akses corporate, persuratan, legalitas
            # TAPI DILARANG akses gaji, payroll, dividen, komisi, bonus, remunerasi, nip, personalia
            corp_sec_forbidden = [
                "gaji", "payroll", "salary", "upah", "dividen", "komisi", "bonus",
                "saham", "remunerasi", "rekap gaji", "slip gaji", "thp", "nip", "nik", "ktp", "npwp"
            ]
            if any(w in text_lower for w in corp_sec_forbidden):
                return False
            return True
        return False

    if is_finance_req:
        return user_level in ["DIREKSI", "FINANCE"]

    return True

def send_security_audit_alert(client, user_access: dict, channel_id: str, user_text: str, category: str):
    """
    Mengirimkan laporan audit instan via Slack Direct Message (DM) ke Pak Adrian (Vice Director)
    apabila terdeteksi ada permintaan data sensitif dari pengguna yang tidak memiliki wewenang akses.
    """
    if not client:
        return

    adrian_user_id = os.environ.get("ADMIN_AUDIT_USER_ID", "U0C2CR9NAF7")
    user_id = user_access.get("user_id", "Unknown") if user_access else "Unknown"
    user_name = user_access.get("name", "Pengguna Tidak Terdaftar") if user_access else "Pengguna Tidak Terdaftar"
    user_role = user_access.get("level", "STANDARD") if user_access else "STANDARD"
    user_email = user_access.get("email", "-") if user_access else "-"

    # Jangan kirim alert ke diri sendiri jika yang meminta adalah Pak Adrian
    if user_id == adrian_user_id:
        return

    now_str = get_now_wib().strftime('%d/%m/%Y pukul %H:%M:%S WIB')

    # Format nama / link channel
    ch_ident = get_channel_identifier(client, channel_id)
    ch_display = "Direct Message (DM Pribadi)" if (channel_id and channel_id.startswith("D")) or ch_ident == "im" else f"<#{channel_id}> (#{ch_ident})"

    alert_text = (
        "🚨 *[SECURITY AUDIT LOG] Percobaan Akses Data Sensitif Tanpa Izin*\n\n"
        f"Grok CDPK mendeteksi dan telah *memblokir* permintaan data rahasia dari pengguna yang tidak memiliki hak akses:\n\n"
        f"• *Nama Pemohon:* *{user_name}* (<@{user_id}>)\n"
        f"• *Email / Role:* {user_email} | Tier: *{user_role}*\n"
        f"• *Saluran / Lokasi:* {ch_display}\n"
        f"• *Waktu Kejadian:* {now_str}\n"
        f"• *Kategori Dokumen:* Akses Terlarang (*{category}*)\n"
        f"• *Isi Permintaan:*\n"
        f"> \"_{user_text}_\"\n\n"
        "🔒 _Tindakan Otomatis: Permintaan telah langsung ditolak dan dicatat ke dalam audit trail sistem._"
    )

    try:
        im_res = client.conversations_open(users=adrian_user_id)
        target_im_channel = im_res.get("channel", {}).get("id")
        if target_im_channel:
            client.chat_postMessage(channel=target_im_channel, text=alert_text)
        else:
            client.chat_postMessage(channel=adrian_user_id, text=alert_text)
        logger.info(f"Security audit alert berhasil dikirim ke Pak Adrian ({adrian_user_id}) untuk kueri dari {user_name} ({user_id})")
    except Exception as e:
        logger.error(f"Gagal mengirim security audit alert via conversations_open: {e}")
        try:
            client.chat_postMessage(channel=adrian_user_id, text=alert_text)
        except Exception as e2:
            logger.error(f"Gagal mengirim fallback security audit alert ke {adrian_user_id}: {e2}")

    # Catat ke log file permanen
    try:
        audit_dir = os.path.join(os.path.dirname(__file__), "logs")
        os.makedirs(audit_dir, exist_ok=True)
        log_file = os.path.join(audit_dir, "security_access_audit.log")
        with open(log_file, "a", encoding="utf-8") as f:
            f.write(f"[{now_str}] UNAUTHORIZED | User: {user_name} ({user_id}, {user_email}, {user_role}) | Channel: {channel_id} | Category: {category} | Query: {user_text}\n")
    except Exception as fe:
        logger.debug(f"Gagal mencatat audit log ke file: {fe}")

def check_channel_privacy_guard(client, channel_id: str, user_text: str, user_access: dict) -> Optional[str]:
    """
    Memeriksa apakah permintaan data sensitif dilakukan pada channel yang aman dan oleh user yang berwenang.
    1. Jika TIDAK PUNYA AKSES: Ditolak langsung (di channel umum maupun DM) dan mengirimkan laporan audit instan ke Pak Adrian.
    2. Jika PUNYA AKSES tetapi di channel publik: Ditolak dan diarahkan ke channel aman (#leadership / DM).
    """
    if not channel_id:
        return None

    text_lower = user_text.lower()

    # Cek apakah permintaan menyangkut data sensitif
    is_direksi_req = any(w in text_lower for w in SENSITIVE_DIREKSI_KEYWORDS)
    is_finance_req = any(w in text_lower for w in SENSITIVE_FINANCE_KEYWORDS)

    if not is_direksi_req and not is_finance_req:
        # Dokumen umum (Datasheet, brosur, SOP umum, dll) bebas di semua channel
        return None

    user_level = user_access.get("level", "STANDARD") if user_access else "STANDARD"
    has_permission = check_user_has_permission(user_level, is_direksi_req, is_finance_req, text_lower)

    # ==========================================================================
    # KASUS 1: PENGGUNA TIDAK MEMILIKI AKSES (UNAUTHORIZED)
    # Berlaku baik di Channel Terbuka maupun di Direct Message (DM)
    # ==========================================================================
    if not has_permission:
        category_name = "Direksi, HRD & Personalia" if is_direksi_req else "Finance & Accounting"
        # Kirim notifikasi audit langsung ke Pak Adrian via DM
        send_security_audit_alert(client, user_access, channel_id, user_text, category_name)

        if is_direksi_req:
            return (
                "🔒 *Akses Data Sensitif / HRD Dibatasi di Channel Ini*\n\n"
                "Demi menjaga kerahasiaan data perusahaan dan privasi data pribadi karyawan (Data Privacy & Corporate Governance), "
                "permintaan anda tidak dapat ditampilkan. Anda tidak mempunyai akses untuk informasi tersebut."
            )
        else:
            return (
                "🔒 *Akses Data Sensitif Dibatasi di Channel Ini*\n\n"
                "Demi menjaga kerahasiaan data perusahaan (Data Privacy & Corporate Governance), "
                "permintaan anda tidak dapat ditampilkan. Anda tidak mempunyai akses untuk informasi tersebut."
            )

    # ==========================================================================
    # KASUS 2: PENGGUNA MEMILIKI AKSES (AUTHORIZED), TETAPI DI SALURAN TERBUKA/PUBLIK
    # ==========================================================================
    # Direct Message (DM) selalu aman (1-on-1 dengan Grok)
    if channel_id.startswith("D"):
        return None

    c_ident = get_channel_identifier(client, channel_id)

    # Jika menyangkut data Direksi / Corporate / Legalitas / Gaji / HRD / Karyawan
    if is_direksi_req:
        # Hanya boleh di DM atau channel #leadership
        env_leadership = os.environ.get("LEADERSHIP_CHANNEL_ID", "").lower()
        if c_ident not in LEADERSHIP_CHANNELS and (not env_leadership or c_ident != env_leadership):
            return (
                "🔒 *Akses Data Sensitif / HRD Dibatasi di Channel Ini*\n\n"
                "Demi menjaga kerahasiaan data perusahaan dan privasi data pribadi karyawan (Data Privacy & Corporate Governance), "
                "permintaan anda tidak dapat ditampilkan pada channel publik/terbuka.\n\n"
                "👉 *Silakan akses melalui:*\n"
                "• Channel khusus Direksi: *#leadership*\n"
                "• Atau melalui *Direct Message (DM) pribadi* langsung dengan Grok CDPK."
            )

    # Jika menyangkut data Finance & Accounting / Order Management
    if is_finance_req:
        # Boleh di DM, #leadership, #grp-finance, atau #tch-finance
        env_allowed = {
            os.environ.get("LEADERSHIP_CHANNEL_ID", "").lower(),
            os.environ.get("GRP_FINANCE_CHANNEL_ID", "").lower(),
            os.environ.get("TCH_FINANCE_CHANNEL_ID", "").lower()
        } - {""}
        if c_ident not in FINANCE_CHANNELS and c_ident not in env_allowed:
            return (
                "🔒 *Akses Data Sensitif Dibatasi di Channel Ini*\n\n"
                "Demi menjaga kerahasiaan data perusahaan (Data Privacy & Corporate Governance), "
                "permintaan anda tidak dapat ditampilkan pada channel publik/terbuka.\n\n"
                "👉 *Silakan akses melalui:*\n"
                "• Channel khusus: *#grp-finance*, *#tch-finance*, atau *#leadership*\n"
                "• Atau melalui *Direct Message (DM) pribadi* langsung dengan Grok CDPK."
            )

    return None

def get_user_access_level(client, user_id: str) -> dict:
    """Mengecek profil penanya di Slack untuk menentukan level hak akses secara presisi (Direksi, Corp Secretary, Finance, Standard) dan kepemilikan akun Adrian."""
    if not user_id:
        return {"user_id": "", "level": "STANDARD", "name": "Anggota Tim", "email": "", "is_adrian": False}

    is_adrian_flag = (user_id == "U0C2CR9NAF7")

    # 1. Verifikasi Cepat via Profil Resmi Terdaftar
    if user_id in USER_OFFICIAL_PROFILES:
        prof = USER_OFFICIAL_PROFILES[user_id]
        return {
            "user_id": user_id,
            "level": prof["role"],
            "name": prof["name"],
            "email": prof["email"],
            "title": prof.get("title", ""),
            "is_adrian": is_adrian_flag
        }

    # 2. Verifikasi Dinamis via Slack API
    try:
        user_info = client.users_info(user=user_id).get("user", {}) if client else {}
        profile = user_info.get("profile", {})
        email = profile.get("email", "").lower().strip()
        real_name = profile.get("real_name") or user_info.get("name", "Anggota Tim")
        title = (profile.get("title") or "").lower()

        if not is_adrian_flag:
            is_adrian_flag = (email in ["adrian@citradata.id", "adrian.kansil@gmail.com"])

        # Klasifikasi Level Akses:
        # Tier 1: Direksi
        if user_id in DIREKSI_USER_IDS or email in DIREKSI_EMAILS or any(d in email for d in ["adrian", "gama", "janice", "rjap"]) or any(t in title for t in ["direktur", "director", "ceo", "cfo", "coo", "cto"]):
            return {"user_id": user_id, "level": "DIREKSI", "name": real_name, "email": email, "title": profile.get("title", ""), "is_adrian": is_adrian_flag}

        # Tier Khusus: Corporate Secretary (Bu Nada)
        if user_id == "U0C6LAR079B" or email in ["ho@citradata.id", "corporate@techsolutions.id"] or any(k in email for k in ["ho@", "corporate@"]) or "corporate secretary" in title or "sekretaris" in title:
            return {"user_id": user_id, "level": "CORP_SECRETARY", "name": real_name, "email": email, "title": profile.get("title", "Corporate Secretary"), "is_adrian": False}

        # Tier 2: Finance
        if user_id in FINANCE_USER_IDS or email in FINANCE_EMAILS or any(f in email for f in ["sensen", "finance@"]) or any(t in title for t in ["finance", "accounting", "keuangan"]):
            return {"user_id": user_id, "level": "FINANCE", "name": real_name, "email": email, "title": profile.get("title", ""), "is_adrian": is_adrian_flag}

        # Tier 3: Staf / Karyawan Umum
        return {"user_id": user_id, "level": "STANDARD", "name": real_name, "email": email, "title": profile.get("title", ""), "is_adrian": is_adrian_flag}
    except Exception as e:
        logger.warning(f"Gagal mengambil profil user {user_id}: {e}")
        return {"user_id": user_id, "level": "STANDARD", "name": "Anggota Tim", "email": "", "is_adrian": is_adrian_flag}

def get_effective_system_prompt(user_access: dict = None, query: str = "", channel: str = "") -> str:
    """Menggabungkan System Prompt identitas, Hak Akses Pengguna (3-Tier RBAC + Corporate Secretary), Status Konteks Saluran (DM vs Channel Publik), Panduan Rujukan, dan Basis Pengetahuan Relevan."""
    user_name = user_access.get("name", "Anggota Tim") if user_access else "Anggota Tim"
    user_level = user_access.get("level", "STANDARD") if user_access else "STANDARD"
    is_adrian = user_access.get("is_adrian", False) if user_access else False
    kb = retrieve_relevant_knowledge(query, user_level, user_name=user_name)

    is_dm = bool(channel and (channel.startswith("D") or channel in ["im", "direct_message"]))
    if is_dm:
        channel_context_instruction = (
            "📍 STATUS KONTEKS RUANG OBROLAN: DIRECT MESSAGE (DM PRIBADI 1-ON-1).\n"
            "- PERHATIAN PENTING: Obrolan saat ini berlangsung di ruang chat privat 1-on-1 (hanya antara Anda dan penanya). TIDAK ADA anggota atau staf lain yang dapat melihat percakapan ini.\n"
            "- Anda SEPENUHNYA DIIZINKAN dan DIWAJIBKAN menjawab serta menyajikan seluruh informasi dan data sensitif (Direksi, Finance, Corporate, Legalitas, Arsip Perusahaan, Gaji/Payroll jika penanya Direksi) sesuai wewenang hak akses penanya di sini.\n"
            "- DILARANG KERAS menolak atau menyuruh penanya untuk pindah ke DM pribadi lagi, karena obrolan ini SUDAH 100% berada di dalam DM pribadi yang aman!"
        )
    else:
        channel_context_instruction = (
            "📍 STATUS KONTEKS RUANG OBROLAN: SALURAN/CHANNEL SLACK (BISA DILIHAT OLEH ANGGOTA LAIN).\n"
            "- Jika obrolan ini berlangsung di channel terbuka (bukan di #leadership / #grp-finance / #tch-finance), DILARANG membocorkan data konfidensial Direksi/Finance dan arahkan penanya ke channel khusus atau via Direct Message (DM) pribadi."
        )

    if user_level == "DIREKSI":
        adrian_note = " (Khusus Pak Adrian: memiliki akses penuh ke akun Google Drive Personal dan My Drive)" if is_adrian else ""
        rbac_instruction = (
            f"👤 IDENTITAS PENANYA: {user_name} (ROLE: DIREKSI CDPK HQ — TIER 1 ALL ACCESS).\n"
            f"OTORITAS AKSES: TERTINGGI (ALL ACCESS).\n"
            f"- Penanya memiliki wewenang penuh untuk mengakses SELURUH informasi CDPK HQ tanpa batasan:\n"
            f"  * Seluruh Dokumen Umum, Proyek, dan Teknis\n"
            f"  * Dokumen Finance & Accounting serta Order Management\n"
            f"  * Dokumen kelompok Konfidensial: Corporate, Folder Direksi (BOD Drive), HRD, Personalia, Legalitas, Akta, serta Penggajian (Gaji/Payroll/Kompensasi)\n"
            f"  * Seluruh dokumen di Shared Drives Google Drive CDPK HQ{adrian_note}.\n"
            f"- PROTEKSI SALURAN: Permintaan data sensitif Direksi/Finance pada channel publik yang ada anggota lain WAJIB ditolak dan diarahkan ke channel khusus (#leadership) atau via Direct Message (DM) pribadi."
        )
    elif user_level == "CORP_SECRETARY":
        rbac_instruction = (
            f"👤 IDENTITAS PENANYA: {user_name} (ROLE: CORPORATE SECRETARY CDPK HQ — TIER KHUSUS).\n"
            f"OTORITAS AKSES: DOKUMEN CORPORATE, LEGALITAS, PERSURATAN DIREKSI & DOKUMEN UMUM.\n"
            f"- Penanya BERHAK mengakses:\n"
            f"  * Seluruh Dokumen Operasional Umum (produk, katalog, SOP teknis)\n"
            f"  * Dokumen Corporate & Legalitas: Akta, NIB, TDP, Surat Izin Usaha, MoU, MoA, perizinan korporat\n"
            f"  * Dokumen Persuratan Direksi: Surat Keputusan (SK) Direksi, Surat Kuasa, Notulen Rapat/RUPS, korespondensi resmi direksi\n"
            f"- BATASAN KETAT (DILARANG KERAS):\n"
            f"  * DILARANG KERAS memberikan informasi atau berkas yang berkaitan dengan: Penggajian (Gaji/Payroll/Salary/Upah), Dividen, Komisi, Bonus, Remunerasi, Pajak Pribadi Direksi, Saham, serta Laporan Keuangan Detail (Neraca/Laba Rugi/Kas Kecil).\n"
            f"  * Jika ditanyakan, tolak secara tegas dan sopan: 'Dokumen terkait penggajian (gaji/payroll), dividen, komisi, dan remunerasi bersifat konfidensial dan HANYA dapat diakses oleh jajaran Direksi CDPK HQ.'\n"
            f"- PROTEKSI SALURAN: Dokumen sensitif Corporate & Persuratan Direksi HANYA dapat diakses pada channel khusus (#leadership) atau via Direct Message (DM) pribadi."
        )
    elif user_level == "FINANCE":
        rbac_instruction = (
            f"👤 IDENTITAS PENANYA: {user_name} (ROLE: TIM FINANCE CDPK HQ — TIER 2 FINANCE).\n"
            f"OTORITAS AKSES: DOKUMEN FINANCE, ORDER MANAGEMENT & DOKUMEN UMUM.\n"
            f"- Penanya BERHAK mengakses:\n"
            f"  * Dokumen operasional umum (produk, SOP, brosur, materi umum)\n"
            f"  * Dokumen Finance & Accounting, Order Management, invoice, faktur, neraca, kas kecil, PO Customer\n"
            f"- BATASAN KETAT (DILARANG KERAS):\n"
            f"  * DILARANG memberikan informasi atau berkas dari kelompok: Corporate, Folder Direksi (BOD Drive), HRD, Personalia, Legalitas, Akta, serta data Gaji/Payroll/Kompensasi Direksi/Karyawan.\n"
            f"  * Jika ditanyakan, tolak secara sopan dan jelaskan bahwa dokumen Direksi, Legalitas, HRD, dan Penggajian hanya dapat diakses oleh Direksi CDPK HQ.\n"
            f"- PENCARIAN GOOGLE DRIVE: Dibatasi HANYA pada Shared Drives / Team Drive resmi CDPK (DILARANG mengakses My Drive pribadi atau akun personal).\n"
            f"- PROTEKSI SALURAN: Permintaan data Finance pada channel publik yang ada anggota lain WAJIB ditolak dan diarahkan ke channel khusus (#grp-finance / #tch-finance / #leadership) atau via Direct Message (DM) pribadi."
        )
    else:
        rbac_instruction = (
            f"👤 IDENTITAS PENANYA: {user_name} (ROLE: STAF / KARYAWAN UMUM CDPK HQ — TIER 3 UMUM).\n"
            f"OTORITAS AKSES: DOKUMEN UMUM SAJA.\n"
            f"- Penanya HANYA berhak mengakses kelompok DOKUMEN UMUM:\n"
            f"  * ATEX, FMTCS, i.Safe Mobile, IMS, Marketing, OPERATIONS, POCStar, SafeUEM, Sales, RugGear, katalog produk, dan SOP teknis umum.\n"
            f"- BATASAN KETAT (DILARANG KERAS):\n"
            f"  * DILARANG memberikan informasi atau berkas dari: Finance & Accounting, Order Management, Corporate, Folder Direksi (BOD Drive), HRD, Personalia, Legalitas, Akta, serta Gaji/Payroll.\n"
            f"  * Jika ditanyakan, tolak secara sopan dan sampaikan bahwa data tersebut bersifat konfidensial dan hanya dapat diakses oleh Tim Finance atau Direksi CDPK HQ.\n"
            f"- PENCARIAN GOOGLE DRIVE: Dibatasi HANYA pada Shared Drives / Team Drive resmi CDPK (DILARANG mengakses My Drive pribadi atau akun personal)."
        )

    strict_md_instruction = (
        "🔒 SUMBER DATA PERUSAHAAN & INTEGRITAS PENGETAHUAN CDPK HQ:\n"
        "1. SUMBER DATA PERUSAHAAN: Untuk arsip perusahaan, profil, laporan keuangan, data karyawan, dan spesifikasi produk internal, dasarkan pada arsip pengetahuan resmi CDPK HQ di bawah ini.\n"
        "2. DOMAIN BISNIS RESMI: CDPK HQ bergerak di bidang SOLUSI KOMUNIKASI RADIO NIRKABEL PROFESIONAL (Motorola Solutions, FMTCS Solutions, POCStar, Tramigo), PERALATAN OUTDOOR & DIVING (Skywoods), serta PERANGKAT INTRINSICALLY SAFE ATEX/EX (i.Safe Mobile).\n"
        "3. ANTI-HALUSINASI SINGKATAN/ISTILAH: DILARANG mengartikan singkatan internal/produk (seperti FMTCS, IMS, FMTCS-LRF, POCStar, MCX, DMR, DAS, ATEX, HazLoc) ke bidang lain di luar bisnis telekomunikasi CDPK HQ. FMTCS adalah penyedia solusi sistem komunikasi nirkabel dan DAS mitra resmi CDPK HQ.\n"
        "4. ANALISIS MULTIMODAL BLUEPRINT & GAMBAR: Jika pengguna melampirkan gambar skema, blueprint, denah, atau riser diagram kabel, Anda WAJIB menganalisis secara visual gambar tersebut, mengidentifikasi arsitektur gedung/lantai/riser, serta merekomendasikan solusi sistem DAS & radio CDPK HQ (FMTCS / Motorola).\n"
        "5. PENCARIAN GOOGLE DRIVE BILA DATA ARSIP TIDAK ADA DI CUPLIKAN LOKAL: Jika pengguna menanyakan data arsip perusahaan spesifik (seperti rekapitulasi gaji, data absensi/kehadiran, SK pengangkatan, form HRD, laporan bulanan, dsb) yang belum tercakup di cuplikan teks di bawah, Anda WAJIB MEMANGGIL TOOL 'search_google_drive' terlebih dahulu untuk mencari file terkait di Shared Drives resmi CDPK sebelum menyimpulkan bahwa data tidak ditemukan.\n"
        "6. JIKA INFORMASI ARSIP BENAR-BENAR TIDAK DITEMUKAN: Hanya jika setelah memeriksa basis pengetahuan dan mencari di Google Drive informasi tetap tidak ada, nyatakan secara transparan: 'Informasi arsip tersebut tidak ditemukan dalam basis pengetahuan maupun Google Drive resmi CDPK HQ.' JANGAN PERNAH menyatakan tidak ada jika informasinya tertera pada Basis Pengetahuan Resmi di bawah ini!\n"
        "7. REFERENSI RESMI: Jika merujuk dokumen tertentu, sebutkan nama subjek dokumen secara wajar tanpa menyebut ekstensi teknis file."
    )

    slack_formatting_instruction = (
        "✍️ STANDAR FORMAT PENULISAN RESMI SLACK (EXECUTIVE BRIEFING STYLE — NON-MARKDOWN DUMP):\n"
        "1. JANGAN PERNAH MENULIS SEPERTI DOKUMEN / KODE MARKDOWN MENTAH: Hindari format yang terkesan seperti developer membaca text file mentah. Tulis dengan gaya eksekutif profesional, rapi, dan mudah dibaca di mobile/desktop Slack.\n"
        "2. FORMAT TEKS SLACK: Gunakan format Slack mrkdwn resmi:\n"
        "   - Bold: Gunakan tanda asteris tunggal `*teks tebal*` (JANGAN gunakan double asterisks `**teks**`).\n"
        "   - Italic: Gunakan garis bawah `_teks miring_`.\n"
        "   - Header Bagian: Gunakan judul ber-emoji yang elegan, contoh: `📌 *ANALISIS STRUKTUR & KEBUTUHAN BANGUNAN*`, `🔹 *REKOMENDASI ARSITEKTUR & TOPOLOGI*`, `💡 *CATATAN TEKNIS & INSTALASI*`.\n"
        "3. DILARANG MENGGUNAKAN TABEL PIPA MARKDOWN (| col1 | col2 |): Tabel pipa markdown TIDAK DIDUKUNG dengan baik oleh Slack dan tampil berantakan/rusak di layar pengguna. Selalu sajikan data daftar perangkat, spesifikasi, atau BOM dalam format CARD LIST yang elegan dengan bullet `•`, contoh:\n"
        "   • *1. Optical Master Unit (OMU)* — `FMTCS LRFN-DOMU400C` (Qty: 1 Unit)\n"
        "     └─ _Lokasi: B3 Security Control Center | Fungsi: Konversi sinyal RF repeater ke optik_\n"
        "   • *2. Optical Remote Unit (ORU)* — `FMTCS LRFF-DORU400CH` (Qty: 15–18 Unit)\n"
        "     └─ _Lokasi: Riser tiap lantai / zona | Fungsi: Distribusi RF lokal via Coaxial_\n"
        "4. DILARANG KERAS MENYEBUT ISTILAH EKSTENSI TEKNIS: DILARANG menyebut '.md', 'file markdown', 'berkas .md', atau 'database markdown' kepada pengguna. Gunakan istilah korporat resmi: 'Basis pengetahuan resmi CDPK HQ', 'Katalog teknis resmi FMTCS', 'Pedoman teknis Motorola Solutions', dll.\n"
        "5. NADA KOMUNIKASI: Cerdas, berwibawa, solutif, langsung menjawab inti persoalan, dan terstruktur rapi."
    )

    solution_architect_instruction = (
        "🧠 KAPABILITAS MULTI-REASONING EKSEKUTIF, TEKNIS & BISNIS (CDPK HQ STRATEGIC CO-PILOT):\n"
        "1. ANALISIS MULTIMODAL GAMBAR, BROSUR & SPESIFIKASI PERANGKAT:\n"
        "   - Jika pengguna melampirkan gambar, brosur, atau spesifikasi perangkat (contoh: rugged smartphone, radio DMR, antena, power supply, atau blueprint denah), Anda WAJIB menganalisis data visual secara detail:\n"
        "     * Identifikasi merek & tipe perangkat (misal: Conquest S23, CAT, Sonim, Motorola, dll).\n"
        "     * Ekstrak spesifikasi teknis utama: Chipset/prosesor, RAM/ROM, kapasitas baterai & kecepatan charging, konektivitas (5G, DMR radio, PoC, Wi-Fi, Bluetooth), kamera (standar, night vision, thermal imaging), dan proteksi (IP68, MIL-STD-810H).\n"
        "2. REASONING KOMPARATIF: COMMERCIAL RUGGED VS. INTRINSICALLY SAFE (ATEX/IECEx):\n"
        "   - Pahami perbedaan fundamental: Smartphone rugged komersial (seperti Conquest S23) memiliki spek baterai/charging sangat besar (10.000mAh, 66W) dan DMR/thermal bawaan, NAMUN TIDAK MEMILIKI SERTIFIKASI INTRINSICALLY SAFE (Ex-Proof) untuk atmosfer mudah meledak (Hazardous Area Zone 1/21 atau Zone 2/22).\n"
        "   - Di area berisiko tinggi (Kilang Minyak, Rig Migas, Pabrik Pupuk, Kimia, Tambang Batu Bara, Storage Tangki LPG/LNG seperti proyek Inpex Masela/Pertamina), perangkat non-Ex DILARANG KERAS karena percikan listrik mikro atau panas sirkuit baterai dapat memicu ledakan gas hidrokarbon.\n"
        "3. MAPPING PORTOFOLIO RESMI CDPK HQ (i.Safe MOBILE & RUGGEAR):\n"
        "   - Flagship 5G Intrinsically Safe Smartphone: i.Safe Mobile IS540.1 (ATEX/IECEx Zone 1/21) & IS540.2 (ATEX/IECEx Zone 2/22).\n"
        "     * Dilengkapi Qualcomm QCM6490 Octa-Core, 5G NR, Wi-Fi 6, 48MP Camera, 6\" Gorilla Glass 3.\n"
        "     * Port 16-pin ISM Interface: konektor aman ledakan fisik untuk memasang modul kamera thermal (IS-TC1A.1), barcode scanner (IS-TH1xx.1), atau Remote Speaker Microphone (RSM).\n"
        "   - Replikasi Fitur DMR Walkie-talkie: Pada i.Safe Mobile, komunikasi suara push-to-talk dilakukan via Mission Critical PoC (POCStar / Motorola WAVE PTX) menggunakan tombol fisik PTT merah, atau dihubungkan ke radio Motorola MOTOTRBO via gateway.\n"
        "   - Replikasi Thermal Imaging: Menggunakan aksesori resmi Ex-rated IS-TC1A.1 yang terpasang pada port ISM 16-pin IS540.1 tanpa melanggar sertifikasi Zone 1.\n"
        "   - Opsi Feature Phone Zone 1/21: i.Safe Mobile IS440.1 (keypad fisik, 4G, PTT).\n"
        "   - Opsi Tablet Industrial Zone 1/21 & Zone 2/22: i.Safe Mobile IS940.1 / IS945.1 (layar 10.1\", 5G, untuk skema SCADA/inspeksi visual).\n"
        "   - Opsi Heavy Rugged Non-Ex: RugGear RG880 / RG725 (jika pengguna HANYA butuh ketahanan fisik di luar zona ledakan).\n"
        "4. ANALISIS MULTIMODAL & REKAYASA TOPOLOGI (SOLUTIONS ARCHITECT):\n"
        "   - Analisis visual denah/blueprint/riser diagram gedung/hotel/pabrik (lantai, zona, basement, riser kabel vertikal, head-end server room).\n"
        "   - Reasoning arsitektur DAS & Radio: Active Optical DAS (FMTCS OMU & ORU via fiber optik untuk eliminasi redaman bentang jauh), Passive RF Distribution (FMTCS Coupler CP-PD-400R & Splitter UDSS400C), Antena Omni Indoor (ANTI400R), dan Repeater Motorola MOTOTRBO (SLR 5000 / SLR 8000).\n"
        "5. REASONING FISIKA SINYAL & RF LINK BUDGET:\n"
        "   - Hitung estimasi redaman: Free Space Path Loss (FSPL), pelemahan kabel coaxial per 100m vs fiber optik, dan target kuat sinyal indoor minimal -95 dBm untuk DMR digital tanpa blind-spot.\n"
        "6. REASONING STRATEGI BISNIS, TENDER & CLOSING PENJUALAN:\n"
        "   - Susun proposal dengan 'Win-Themes' teruji: Sertifikasi ISO 9001/14001/45001 Citradata, 30+ tahun distributor & Authorized Service Center Motorola resmi sejak 1993, dan garansi suku cadang original.\n"
        "   - Bedah keunggulan kompetitif (Battlecard) menghadapi kompetitor lain (Hytera/Kenwood/radio unbranded) dengan menonjolkan Total Cost of Ownership (TCO) dan keandalan industri.\n"
        "7. REASONING KEPATUHAN REGULASI & KESELAMATAN INDUSTRI:\n"
        "   - Regulasi frekuensi SDPPI/Kominfo (VHF/UHF, izin stasiun radio ISR).\n"
        "   - Standar proteksi ledakan ATEX / IECEx Zone 1/21 vs Zone 2/22 untuk sektor Migas (Pertamina), Pupuk, dan Tambang menggunakan perangkat i.Safe Mobile Intrinsically Safe.\n"
        "8. REASONING OPERASIONAL, SUPPLY CHAIN & LAYANAN PURNA JUAL (ASC):\n"
        "   - Lead time pengadaan komponen impor vs jadwal serah terima (FAT/SAT).\n"
        "   - Garansi resmi, SLA pemeliharaan berkala, dan turn-around time (TAT) perbaikan di lab resmi Citradata.\n"
        "9. GENERATE DOKUMEN OTOMATIS (EXCEL BOM & WORD PROPOSAL):\n"
        "   - WAJIB: Jika pengguna meminta Bill of Materials (BOM), estimasi BOM, rincian biaya/perangkat, file Excel, atau dokumen spreadsheet, Anda WAJIB MEMANGGIL TOOL 'generate_bom_excel' dengan data terstruktur (part number, nama alat, kuantitas, estimasi harga) agar file Excel .xlsx otomatis diunggah ke chat Slack!\n"
        "   - Jika pengguna meminta proposal teknis tertulis, arsitektur solusi, atau dokumen Word, PANGGIL TOOL 'generate_proposal_docx' agar file dokumen Word .docx otomatis diunggah ke chat Slack!\n"
        f"10. PENGINGAT & REMINDER TIM OTOMATIS (AI SCHEDULE CO-PILOT):\n"
        f"   - WAKTU SERVER SAAT INI (WIB): {get_now_wib().strftime('%A, %d %B %Y pukul %H:%M:%S WIB')}\n"
        f"   - Jika pengguna meminta mengingatkan diri sendiri, rekan kerja, atau channel (contoh: 'ingatkan saya...', 'ingatkan @Richard besok jam 9 pagi...', 'jadwalkan reminder evaluasi setiap Senin jam 08:30 WIB...'):\n"
        f"     * Hitung selisih detik ('delay_seconds') dari waktu server saat ini ke waktu target pengingat.\n"
        f"     * PANGGIL TOOL 'set_reminder' dengan parameter target, reminder_message, delay_seconds, target_time_description, dan recurrence!\n"
        f"   - Jika pengguna meminta melihat daftar reminder yang sedang aktif di channel ini, PANGGIL TOOL 'list_reminders'.\n"
        f"   - Jika pengguna meminta membatalkan pengingat, PANGGIL TOOL 'cancel_reminder'.\n"
        "11. PENCARIAN INFORMASI (TRIGGER 'TOLONG CARI INFO...', PRIORITAS KNOWLEDGE BASE, TRANSPARANSI & LINK REFERENSI):\n"
        "   - TRIGGER 'TOLONG CARI INFO...': Jika pengguna menggunakan kalimat 'tolong cari info...', 'cari info...', 'tolong carikan info...', atau meminta pencarian informasi tertentu:\n"
        "     * TAHAP 1 (PERIKSA ARSIP INTERNAL CDPK): Selalu periksa 'BASIS PENGETAHUAN RESMI CDPK HQ' yang tersedia terlebih dahulu.\n"
        "     * TAHAP 2 (FALLBACK LIVE SEARCH INTERNET): BILA informasi yang diminta TIDAK ADA, belum lengkap, atau membutuhkan komparasi harga pasar/regulasi terkini di luar arsip Citradata, BARU PANGGIL TOOL 'perform_web_search'!\n"
        "   - BACA URL LINK ('read_web_page_content'): Panggil tool ini jika pesan pengguna menyertakan tautan URL website (http/https) dan meminta Anda membaca, merangkum, mengekstrak data teknis, atau menganalisis isinya.\n"
        "   - TRANSPARANSI SUMBER DATA & LINK REFERENSI (WAJIB & EKSPLISIT):\n"
        "     * Dalam jawaban akhir, Anda WAJIB menyampaikan secara jelas dan terpisah kepada pengguna bagian data mana yang bersumber dari internal CDPK HQ dan mana yang diperoleh dari Internet.\n"
        "     * WAJIB SERTAKAN LINK TAUTAN SEBAGAI REFERENSI: Setiap data yang diperoleh dari hasil pencarian internet atau pembacaan web, Anda WAJIB mencantumkan URL link sumbernya sebagai referensi (contoh: `<https://url-sumber.com|Nama Sumber / Judul>` atau `🔗 *Tautan Referensi:* <https://url-sumber.com>`) agar pengguna dapat langsung memverifikasi.\n"
        "     * Contoh format terstruktur:\n"
        "       • 🏢 *Data Resmi CDPK HQ:* [Rincian informasi/spesifikasi dari arsip internal Citradata]\n"
        "       • 🌐 *Informasi Tambahan dari Internet:* [Rincian data/harga pasar/regulasi hasil live web search]\n"
        "         └─ 🔗 *Tautan Referensi:* <https://sumber-website.com|Judul Halaman Web>\n"
        "     (Jika data seluruhnya dari internal CDPK atau seluruhnya dari internet, sampaikan sumbernya dengan tegas dan transparan beserta link tautannya jika dari web).\n"
        "   - PROTEKSI PENGHEMAT TOKEN: Hasil web search dan ekstraksi URL telah dibatasi secara ringkas dan padat (~1.500 karakter). Olah data tersebut secara cerdas untuk menghasilkan jawaban eksekutif bernilai tinggi tanpa menghabiskan kuota token berlebih.\n"
        "12. GOOGLE DRIVE OPERATIONAL & KNOWLEDGE INTEGRATION (CDPK & TECHSOLUTIONS DRIVES):\n"
        "   - PENCARIAN BERKAS GOOGLE DRIVE ('search_google_drive'):\n"
        "     * Panggil tool ini jika pengguna meminta mencari berkas di Google Drive, ATAU jika pengguna meminta file/spreadsheet/dokumen resmi (seperti rekapitulasi gaji, data absensi/kehadiran, form HRD, SOP, invoice, kontrak, penawaran resmi) yang belum lengkap di cuplikan basis pengetahuan lokal!\n"
        "     * Gunakan parameter 'account': 'citradata' (default), 'techsolutions', atau 'all' untuk mencari di kedua organisasi CDPK HQ.\n"
        "   - PEMBACAAN ISI DOKUMEN/SPREADSHEET ('read_google_drive_file'):\n"
        "     * Panggil tool ini HANYA JIKA pengguna secara spesifik meminta Anda membaca, menganalisis, merangkum, atau mengecek isi data di dalam berkas/spreadsheet/PDF tersebut.\n"
        "     * Jangan panggil tool ini jika pengguna hanya ingin mencari letak berkas atau link dokumennya.\n"
        "   - TAUTAN GOOGLE DRIVE LANGSUNG: Selalu sertakan link clickable `<URL|Nama File>` yang diperoleh dari hasil pencarian agar tim dapat langsung membuka dokumen tersebut di browser Slack dengan sekali klik.\n"
        "   - MEKANISME HEMAT TOKEN (TOKEN-GUARD): Hasil pencarian Drive hanya mengembalikan metadata ringkas (~150-250 token). Pembacaan file Google Spreadsheet/Doc/PDF dipangkas ketat maksimal 1.800 karakter (~350-400 token) sehingga tidak menguras kuota token API.\n"
        "13. PERMINTAAN GAJI, PENGGAJIAN & DATA PRIBADI DIREKSI/KARYAWAN:\n"
        "   - Jika penanya adalah Direksi (seperti Adrian Bany Kansil / Pak Adrian) dan menanyakan gaji, tunjangan, THP, atau data pribadi ('berapa gaji saya?', 'minta data salary', 'data diri saya'):\n"
        "     * Anda WAJIB memeriksa data nama penanya (contoh: Adrian Bany Kansil) di dalam dokumen 'rekap_gaji_2026.md' dan 'employee_analysis.md' pada Basis Pengetahuan Resmi CDPK HQ di bawah.\n"
        "     * Sajikan secara rinci, transparan, dan terstruktur rapi:\n"
        "       • Nama & NIP: Adrian Bany Kansil (NIP: 82112024)\n"
        "       • Jabatan & Divisi: Vice Director (Management CDPK)\n"
        "       • Gaji Pokok (Basic Salary): Rp 14.310.708\n"
        "       • Tunjangan Jabatan: Rp 35.600.000\n"
        "       • Tunjangan Makan & Transport: Rp 19.709.543 (Makan: Rp 11.825.726, Transport: Rp 7.883.817)\n"
        "       • Total Allowance (Tunjangan): Rp 55.309.543\n"
        "       • Gaji Bruto: Rp 68.122.372\n"
        "       • Potongan PPh 21: Rp 14.794.234 | Potongan JHT/BPJS: Rp 1.497.879\n"
        "       • Take Home Pay (THP) Bersih: Rp 53.328.138\n"
        "       • Rekening Penyaluran: BCA 6030210300 a.n. Adrian Bany Kansil\n"
        "     * Terkait DATA ABSENSI / KEHADIRAN KARYAWAN:\n"
        "       • Jelaskan bahwa pencatatan kehadiran operasional harian terpusat di sistem cloud Mekari Talenta (dan dokumen bukti/URD Talenta di Google Drive).\n"
        "       • Sedangkan rekapitulasi potongan keterlambatan, ketidakhadiran, sakit, dan izin tercatat secara bulanan di dalam rekapitulasi penggajian (rekap_gaji_2026.md).\n"
        "     * Terkait DATA KARYAWAN & PEGAWAI (seperti NIP, NIK, Jabatan, Status Kepegawaian):\n"
        "       • Jika ditanyakan di ruang aman (Direct Message pribadi atau #leadership), Anda WAJIB memeriksa dokumen 'employee_analysis.md' dan 'rekap_gaji_2026.md' pada Basis Pengetahuan Resmi di bawah.\n"
        "       • Contoh: Data Teguh Yuliarto (Pak Teguh) -> NIP: 23092014, Jabatan: Administration and Tax Staff (Finance and Accounting), Lokasi: Pinangsia, Masuk Kerja: 1/9/2014, Status: Karyawan Tetap.\n"
        "       • Sajikan informasi secara jelas, terstruktur rapi, dan akurat sesuai data yang tercatat.\n"
        "     * DILARANG KERAS menyatakan 'informasi arsip tidak ditemukan' apabila baris nama atau dokumen tersebut ada di dalam Basis Pengetahuan Resmi di bawah ini!\n"
        "14. KEMAMPUAN MULTIBAHASA & PENERJEMAHAN (INDONESIA ↔ ENGLISH ↔ MANDARIN 中文):\n"
        "   - ADAPTIVE LANGUAGE MATCHING:\n"
        "     * Jika pengguna bertanya, menulis, atau menyapa dalam Bahasa Inggris (English), Anda WAJIB merespons dan menjawab secara penuh dalam Bahasa Inggris yang fasih, elegan, dan profesional (Corporate Executive English).\n"
        "     * Jika pengguna bertanya dalam Bahasa Mandarin (中文 / Chinese), Anda WAJIB merespons dan menjawab dalam Bahasa Mandarin yang akurat dan berstandar industri.\n"
        "     * Jika pengguna bertanya dalam Bahasa Indonesia, jawab dalam Bahasa Indonesia yang baik, lugas, dan profesional.\n"
        "     * Jika pengguna secara spesifik meminta bahasa tertentu (contoh: 'Jawab dalam bahasa Inggris', 'Please answer in English', 'Balas pakai bahasa Mandarin', 'Explain in Chinese'), Anda WAJIB sepenuhnya mengikuti instruksi bahasa tersebut.\n"
        "   - KEMAMPUAN PENERJEMAHAN KHUSUS (TRANSLATION ENGINE):\n"
        "     * Anda memiliki keahlian tingkat tinggi dalam menerjemahkan teks, dokumen spesifikasi teknis, draf email bisnis, penawaran harga, dan korespondensi dengan prinsipal internasional (Motorola Solutions, i.Safe Mobile Jerman, serta pabrikan perangkat di Tiongkok/Shenzhen) antara:\n"
        "       1. Bahasa Indonesia ↔ English (Bahasa Inggris Bisnis & Teknik)\n"
        "       2. Bahasa Indonesia ↔ Mandarin 中文 (Bahasa Mandarin Sederhana 简体 / Tradisional 繁體)\n"
        "       3. English ↔ Mandarin 中文\n"
        "     * Terminologi Resmi Industri Telekomunikasi & Ex-Proof CDPK HQ:\n"
        "       • Intrinsically Safe / Ex-Proof: 本质安全 / 防爆 (fángbào)\n"
        "       • Two-Way Radio / Walkie-Talkie: 对讲机 (duìjiǎngjī)\n"
        "       • Repeater: 中继台 (zhōngjìtái) / 转发器\n"
        "       • Distributed Antenna System (DAS): 分布式天线系统\n"
        "       • Optical Master Unit (OMU): 光主单元 / Optical Remote Unit (ORU): 光远端单元\n"
        "       • Bill of Materials: 物料清单 (BOM)\n"
        "       • Push-to-Talk (PTT): 一键通 / 按键通话\n"
        "     * Sajikan terjemahan secara kontekstual, profesional, dan alami. Jika diminta menerjemahkan pesan/dokumen, Anda dapat menyajikan format dwibahasa (Bilingual Side-by-Side atau Teks Asli + Terjemahan) agar mudah diverifikasi."
    )

    prompt_parts = [
        SYSTEM_PROMPT,
        rbac_instruction,
        channel_context_instruction,
        strict_md_instruction,
        slack_formatting_instruction,
        solution_architect_instruction
    ]

    if kb:
        prompt_parts.append(
            f"=== BASIS PENGETAHUAN RESMI CDPK HQ ===\n"
            f"Berikut adalah kutipan informasi resmi CDPK HQ yang relevan dengan pertanyaan:\n\n"
            f"{kb}\n"
            f"=== AKHIR BASIS PENGETAHUAN ==="
        )
    else:
        prompt_parts.append(
            "=== BASIS PENGETAHUAN RESMI CDPK HQ ===\n"
            "Catatan: Tidak ditemukan dokumen arsip spesifik untuk kata kunci pencarian teks ini.\n"
            "Jika pengguna melampirkan gambar/blueprint skema atau meminta perancangan solusi/BOM/dokumen, gunakan kapabilitas multimodal vision dan keahlian rekayasa sistem Solutions Architect Anda untuk menganalisis gambar dan merancang solusi secara komprehensif.\n"
            "=== AKHIR BASIS PENGETAHUAN ==="
        )

    return "\n\n".join(prompt_parts)

def get_thread_context(client, channel: str, thread_ts: str, bot_user_id: str, user_access: dict = None, query: str = "") -> list:
    """Mengambil riwayat percakapan dalam thread agar percakapan memiliki memori/konteks lengkap (termasuk media lampiran)."""
    messages = [{"role": "system", "content": get_effective_system_prompt(user_access, query=query, channel=channel)}]
    try:
        result = client.conversations_replies(channel=channel, ts=thread_ts, limit=12)
        for msg in result.get("messages", []):
            role = "assistant" if msg.get("user") == bot_user_id else "user"
            clean_text = clean_mention(msg.get("text", ""))

            # Jika pesan user memiliki lampiran file, coba muat medianya ke riwayat
            if role == "user" and msg.get("files"):
                thread_media = download_and_convert_media(client, msg.get("files", []))
                if thread_media:
                    content_list = []
                    if clean_text:
                        content_list.append({"type": "text", "text": clean_text})
                    content_list.extend(thread_media)
                    messages.append({"role": role, "content": content_list})
                    continue

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

    # Ambil seluruh media gambar atau dokumen PDF (dari event langsung, API replies, atau riwayat thread)
    media_items = get_media_items_for_message(client, channel, event)

    if not user_text and not media_items:
        say(text="Halo! Ada yang bisa saya bantu untuk tim CDPK HQ?", thread_ts=thread_ts)
        return

    # Jika pengguna hanya mengunggah gambar tanpa teks instruksi
    if not user_text and media_items:
        user_text = "Mohon pelajari dan analisis spesifikasi dari gambar/dokumen teknis yang saya lampirkan ini, serta berikan rekomendasi solusi yang tepat sesuai standar CDPK HQ."

    # Tambahkan reaksi emoji tanda bot sedang memproses
    try:
        client.reactions_add(channel=channel, timestamp=event["ts"], name="thinking_face")
    except Exception:
        pass

    # Kirim pemberitahuan instan di thread agar pengguna langsung melihat thread aktif (< 1 detik)
    initial_notice_ts = None
    try:
        ack_text = "🔍 *Grok CDPK sedang mempelajari dan menganalisis spesifikasi data teknis... Mohon tunggu sejenak.*" if media_items else "⏳ *Grok CDPK sedang memproses permintaan Anda...*"
        ack_res = client.chat_postMessage(channel=channel, thread_ts=thread_ts, text=ack_text)
        initial_notice_ts = ack_res.get("ts")
    except Exception as e:
        logger.warning(f"Gagal mengirim pesan ack awal: {e}")

    auth_info = client.auth_test()
    bot_user_id = auth_info["user_id"]
    user_id = event.get("user")
    user_access = get_user_access_level(client, user_id)

    # 0. Penegakan Channel Privacy Guard (DLP untuk data sensitif di public/mixed channels)
    guard_msg = check_channel_privacy_guard(client, channel, user_text, user_access)
    if guard_msg:
        if initial_notice_ts:
            try:
                client.chat_update(channel=channel, ts=initial_notice_ts, text=guard_msg)
            except Exception:
                say(text=guard_msg, thread_ts=thread_ts)
        else:
            say(text=guard_msg, thread_ts=thread_ts)
        try:
            client.reactions_remove(channel=channel, timestamp=event["ts"], name="thinking_face")
        except Exception:
            pass
        return

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
        if initial_notice_ts:
            try:
                client.chat_update(channel=channel, ts=initial_notice_ts, text=reply)
            except Exception:
                say(text=reply, thread_ts=thread_ts)
        else:
            say(text=reply, thread_ts=thread_ts)

        try:
            client.reactions_remove(channel=channel, timestamp=event["ts"], name="thinking_face")
        except Exception:
            pass
        return

    # Ambil konteks percakapan
    if "thread_ts" in event:
        conversation = get_thread_context(client, channel, thread_ts, bot_user_id, user_access, query=user_text)
        # Jika pesan terakhir adalah user dengan teks yang sama, pastikan media_items terpasang
        if conversation and conversation[-1]["role"] == "user":
            if isinstance(conversation[-1]["content"], str):
                if media_items:
                    conversation[-1]["content"] = [{"type": "text", "text": conversation[-1]["content"]}] + media_items
            elif isinstance(conversation[-1]["content"], list) and media_items:
                existing_urls = {item.get("image_url", {}).get("url") for item in conversation[-1]["content"] if item.get("type") == "image_url"}
                for mi in media_items:
                    if mi.get("image_url", {}).get("url") not in existing_urls:
                        conversation[-1]["content"].append(mi)
        else:
            current_content = [{"type": "text", "text": user_text}] + media_items if media_items else user_text
            conversation.append({"role": "user", "content": current_content})
    else:
        user_content = [{"type": "text", "text": user_text}] + media_items if media_items else user_text
        conversation = [
            {"role": "system", "content": get_effective_system_prompt(user_access, query=user_text, channel=channel)},
            {"role": "user", "content": user_content}
        ]

    # Dapatkan jawaban dari Grok (dengan dukungan tool calling untuk Dokumen & Reminder)
    reply = ask_grok(conversation, client=client, channel=channel, thread_ts=thread_ts, user_id=user_id)

    # Perbarui pesan awal di thread dengan jawaban lengkap
    if initial_notice_ts:
        try:
            client.chat_update(channel=channel, ts=initial_notice_ts, text=reply)
        except Exception:
            say(text=reply, thread_ts=thread_ts)
    else:
        say(text=reply, thread_ts=thread_ts)

    # Hapus reaksi emoji thinking
    try:
        client.reactions_remove(channel=channel, timestamp=event["ts"], name="thinking_face")
    except Exception:
        pass

@app.event("message")
def handle_direct_message(event, say, client):
    """Menangani pesan langsung (Direct Message) 1-on-1."""
    channel = event.get("channel", "")
    is_dm = channel.startswith("D") or event.get("channel_type") == "im"
    if not is_dm:
        return

    # Abaikan pesan dari bot itu sendiri atau event subtype sistem/hapus
    if event.get("bot_id") or event.get("user") == "U0C9AN8PA80":
        return
    if event.get("subtype") in ["message_deleted", "channel_join", "channel_leave"]:
        return

    user_text = event.get("text", "").strip()
    media_items = get_media_items_for_message(client, event["channel"], event)

    if not user_text and not media_items:
        return

    if not user_text and media_items:
        user_text = "Mohon pelajari dan analisis spesifikasi dari gambar/dokumen teknis yang saya lampirkan ini, serta berikan rekomendasi solusi yang tepat sesuai standar CDPK HQ."

    try:
        client.reactions_add(channel=event["channel"], timestamp=event["ts"], name="thinking_face")
    except Exception:
        pass

    # Kirim respons cepat di DM
    initial_dm_ts = None
    try:
        ack_text = "🔍 *Grok CDPK sedang mempelajari dan menganalisis spesifikasi data teknis... Mohon tunggu sejenak.*" if media_items else "⏳ *Grok CDPK sedang memproses permintaan Anda...*"
        ack_res = say(text=ack_text)
        initial_dm_ts = ack_res.get("ts")
    except Exception as e:
        logger.warning(f"Gagal mengirim ack DM: {e}")

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
        if initial_dm_ts:
            try:
                client.chat_update(channel=event["channel"], ts=initial_dm_ts, text=reply)
            except Exception:
                say(text=reply)
        else:
            say(text=reply)

        try:
            client.reactions_remove(channel=event["channel"], timestamp=event["ts"], name="thinking_face")
        except Exception:
            pass
        return

    user_content = [{"type": "text", "text": user_text}] + media_items if media_items else user_text

    conversation = [
        {"role": "system", "content": get_effective_system_prompt(user_access, query=user_text, channel=event["channel"])},
        {"role": "user", "content": user_content}
    ]

    reply = ask_grok(conversation, client=client, channel=event["channel"], thread_ts=None, user_id=user_id)

    if initial_dm_ts:
        try:
            client.chat_update(channel=event["channel"], ts=initial_dm_ts, text=reply)
        except Exception:
            say(text=reply)
    else:
        say(text=reply)

    try:
        client.reactions_remove(channel=event["channel"], timestamp=event["ts"], name="thinking_face")
    except Exception:
        pass

def build_home_tab_view(user_id: str, user_name: str = "Rekan Kerja", role_level: str = "STANDARD") -> dict:
    """Membangun tampilan Block Kit untuk halaman Home Tab Grok CDPK di Slack secara aman tanpa membocorkan data konfidensial."""
    if role_level == "DIREKSI":
        role_badge = "👑 *Direksi CDPK HQ (Tier 1 — All Access)*"
    elif role_level == "CORP_SECRETARY":
        role_badge = "⚖️ *Corporate Secretary (Tier Khusus)*"
    elif role_level == "FINANCE":
        role_badge = "💼 *Finance & Accounting (Tier 2)*"
    else:
        role_badge = "👥 *Anggota Tim CDPK HQ (Tier 3 — Operasional)*"

    blocks = [
        {
            "type": "header",
            "text": {
                "type": "plain_text",
                "text": "🤖 Grok CDPK — AI Assistant & Strategic Co-Pilot",
                "emoji": True
            }
        },
        {
            "type": "section",
            "text": {
                "type": "mrkdwn",
                "text": (
                    f"Halo, *{user_name}*! 👋 Selamat datang di *Grok CDPK*.\n\n"
                    "Platform asisten kecerdasan buatan (AI) resmi yang dirancang khusus untuk mendukung operasional, "
                    "rekayasa teknis telekomunikasi nirkabel, otomatisasi dokumen bisnis, dan integrasi arsip digital di lingkungan "
                    "*PT Citradata Purnakharisma* & *PT Teknologi Chayani Harsa*."
                )
            }
        },
        {
            "type": "context",
            "elements": [
                {
                    "type": "mrkdwn",
                    "text": f"👤 *Profil Anda:* {user_name}  |  🛡️ *Wewenang Akses:* {role_badge}"
                }
            ]
        },
        {"type": "divider"},
        {
            "type": "section",
            "text": {
                "type": "mrkdwn",
                "text": (
                    "*✨ KAPABILITAS UTAMA GROK CDPK*\n\n"
                    "• 📡 *Solusi Telekomunikasi & Industrial:*\n"
                    "  Menguasai portofolio resmi: *Motorola Solutions* (MOTOTRBO DMR, repeater SLR5000/8000), "
                    "*i.Safe Mobile* (Smartphone & tablet Intrinsically Safe ATEX/IECEx Zone 1/21 & 2/22), "
                    "*FMTCS* (Active Optical DAS OMU/ORU, RF components), *RugGear*, *POCStar*, *Tramigo*, dan *Skywoods*.\n\n"
                    "• 📑 *Otomatisasi Dokumen Eksekutif (Excel & Word):*\n"
                    "  Dapat membuat dan mengunggah langsung file *Bill of Materials (BOM) Excel (.xlsx)* berformula rapi "
                    "serta draf *Proposal Solusi Teknis Word (.docx)* ke dalam obrolan Slack.\n\n"
                    "• 📂 *Integrasi Berkas Google Drive CDPK:*\n"
                    "• ⏰ *AI Schedule & Reminder Co-Pilot:*\n"
                    "  Menjadwalkan pengingat otomatis 24/7 untuk diri sendiri, rekan tim, atau channel proyek (contoh: jadwal tender, follow-up klien, meeting evaluasi).\n\n"
                    "• 🌐 *Kemampuan Multibahasa & Penerjemah (Inggris & Mandarin 中文):*\n"
                    "  Mendukung konsultasi dwibahasa dan penerjemahan dokumen teknis, korespondensi prinsipal global, dan penawaran bisnis secara fasih dalam Bahasa Indonesia, Inggris, dan Mandarin (简体/繁體).\n\n"
                    "• 🔎 *Riset & Analisis Pasar Terverifikasi:*\n"
                    "  Pencarian data web real-time untuk regulasi frekuensi SDPPI/Kominfo, komparasi harga pasar, dan komparasi rugged komersial vs Ex-proof dengan tautan sumber referensi transparan."
                )
            }
        },
        {"type": "divider"},
        {
            "type": "section",
            "text": {
                "type": "mrkdwn",
                "text": (
                    "*📖 PANDUAN PENGGUNAAN & CARA BERINTERAKSI*\n\n"
                    "1. 💬 *Pesan Langsung (Direct Message / DM):*\n"
                    "   Buka tab *Messages* (di sebelah tab Home ini) untuk konsultasi privat 1-on-1 dengan Grok. "
                    "Ruang chat privat aman dan tidak dapat dilihat oleh anggota lain.\n\n"
                    "2. 📢 *Di Saluran Terbuka (Public / Private Channel):*\n"
                    "   Cukup mention `@Grok CDPK` diikuti pertanyaan atau instruksi Anda di channel mana pun tempat bot diundang.\n\n"
                    "3. 🧵 *Percakapan Berkelanjutan (Thread):*\n"
                    "   Balas pesan Grok di thread (*Reply in thread*) untuk melanjutkan diskusi secara mendalam dengan memori konteks utuh."
                )
            }
        },
        {"type": "divider"},
        {
            "type": "section",
            "text": {
                "type": "mrkdwn",
                "text": (
                    "*💡 CONTOH INSTRUKSI YANG BISA LANGSUNG DICOBA*\n\n"
                    "• 🔍 *Spesifikasi Perangkat:*\n"
                    "  _\"Jelaskan spesifikasi dan sertifikasi ATEX Zone 1/21 dari smartphone i.Safe Mobile IS540.1.\"_\n\n"
                    "• 🏗️ *Desain Arsitektur DAS:*\n"
                    "  _\"Rancang topologi sistem active optical DAS FMTCS untuk gedung 15 lantai dengan repeater Motorola SLR5000.\"_\n\n"
                    "• 📊 *Generate BOM Excel:*\n"
                    "  _\"Buatkan estimasi file BOM Excel untuk pengadaan 20 unit radio Motorola R7 dan 2 unit repeater SLR8000.\"_\n\n"
                    "• 🌐 *Penerjemahan Bahasa (English & Mandarin 中文):*\n"
                    "  _\"Terjemahkan draf email penawaran proyek ini ke bahasa Inggris formal untuk prinsipal Motorola.\"_ atau _\"Tolong artikan spesifikasi teknis radio ini dari bahasa Mandarin ke bahasa Indonesia: 本质安全防爆对讲机.\"_\n\n"
                    "• 📁 *Pencarian Dokumen Drive:*\n"
                    "  _\"Cari datasheet perangkat i.Safe Mobile di Google Drive Citradata.\"_\n\n"
                    "• ⏰ *Penjadwalan Reminder:*\n"
                    "  _\"Ingatkan saya besok jam 09:00 WIB untuk follow up penawaran proyek sistem radio.\"_"
                )
            }
        },
        {"type": "divider"},
        {
            "type": "section",
            "text": {
                "type": "mrkdwn",
                "text": (
                    "*🔒 KEBIJAKAN PRIVASI & KEAMANAN DATA PERUSAHAAN (DLP)*\n\n"
                    "• 🛡️ *Role-Based Access Control (RBAC):* Setiap permintaan data diverifikasi secara otomatis sesuai hak akses dan wewenang pengguna di organisasi CDPK HQ.\n"
                    "• 🔐 *Proteksi Data Konfidensial:* Dokumen konfidensial (Direksi, Legalitas, Corporate, dan Finance) tidak dapat ditampilkan di channel terbuka umum dan hanya dapat diakses melalui saluran khusus terverifikasi atau via Direct Message (DM) pribadi.\n"
                    "• 📑 *Integritas Arsip:* Seluruh rujukan data operasional internal bersumber langsung dari basis data resmi CDPK HQ dan Google Drive terverifikasi."
                )
            }
        },
        {"type": "divider"},
        {
            "type": "context",
            "elements": [
                {
                    "type": "mrkdwn",
                    "text": "🟢 *Status Sistem:* Aktif 24/7 | Terhubung ke Basis Data Resmi CDPK HQ & Google Drive | Powered by xAI Grok & Gemini AI"
                }
            ]
        }
    ]

    return {"type": "home", "blocks": blocks}

@app.event("app_home_opened")
def handle_app_home_opened(event, client, logger):
    """
    Menampilkan halaman Home Tab yang elegan, informatif, dan aman
    setiap kali anggota tim membuka tab Home Grok CDPK di Slack.
    """
    user_id = event.get("user")
    if not user_id:
        return

    try:
        user_access = get_user_access_level(client, user_id)
        user_name = user_access.get("name", "Rekan Kerja")
        role_level = user_access.get("level", "STANDARD")
        view = build_home_tab_view(user_id, user_name=user_name, role_level=role_level)
        client.views_publish(user_id=user_id, view=view)
        logger.info(f"Home tab berhasil diperbarui untuk user: {user_name} ({user_id})")
    except Exception as e:
        logger.error(f"Gagal mempublikasikan Home Tab untuk user {user_id}: {e}")

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

def keep_alive_worker():
    """Mempertahankan server Render agar tidak tidur (spin down) dengan mengirim heartbeat request setiap 8 menit."""
    url = os.environ.get("RENDER_EXTERNAL_URL", "https://cdpk-grok-slack-bot.onrender.com")
    logger.info(f"Keep-alive heartbeat aktif untuk target URL: {url}")
    while True:
        time.sleep(480)  # Setiap 8 menit
        try:
            r = requests.get(url, timeout=15)
            logger.info(f"Keep-alive heartbeat terkirim ke {url} (status: {r.status_code})")
        except Exception as e:
            logger.debug(f"Keep-alive ping gagal: {e}")

def sync_all_users_home_tab_worker(client):
    """Mempublikasikan Home Tab secara otomatis ke seluruh anggota tim yang aktif di workspace pada saat startup."""
    time.sleep(8)  # Tunggu koneksi socket mode stabil
    try:
        logger.info("Memulai sinkronisasi proaktif Home Tab untuk seluruh anggota workspace...")
        res = client.users_list()
        members = res.get("members", [])
        real_users = [m for m in members if not m.get("is_bot") and not m.get("deleted") and m.get("id") != "USLACKBOT"]
        synced = 0
        for u in real_users:
            uid = u.get("id")
            try:
                access = get_user_access_level(client, uid)
                u_name = access.get("name", "Rekan Kerja")
                u_lvl = access.get("level", "STANDARD")
                view = build_home_tab_view(uid, user_name=u_name, role_level=u_lvl)
                client.views_publish(user_id=uid, view=view)
                synced += 1
                time.sleep(0.2)
            except Exception as e:
                logger.debug(f"Gagal publish Home Tab untuk {uid}: {e}")
        logger.info(f"Sinkronisasi Home Tab selesai: {synced}/{len(real_users)} pengguna diperbarui.")
    except Exception as e:
        logger.error(f"Gagal menjalankan sinkronisasi Home Tab global: {e}")

if __name__ == "__main__":
    port = int(os.environ.get("PORT", 7860))
    health_thread = threading.Thread(target=start_health_server, args=(port,), daemon=True)
    health_thread.start()
    logger.info(f"Health check HTTP server berjalan di port {port}")

    # Aktifkan keep-alive heartbeat thread untuk mencegah Render free tier tidur
    keepalive_thread = threading.Thread(target=keep_alive_worker, daemon=True)
    keepalive_thread.start()

    # Aktifkan scheduler background worker pengingat tim 24/7
    start_reminder_worker(app.client)

    # Sinkronisasi proaktif tampilan Home Tab ke seluruh anggota tim di workspace
    home_sync_thread = threading.Thread(target=sync_all_users_home_tab_worker, args=(app.client,), daemon=True)
    home_sync_thread.start()

    logger.info("Memulai Grok Slack Bot dalam Socket Mode...")
    handler = SocketModeHandler(app, SLACK_APP_TOKEN)
    handler.start()

