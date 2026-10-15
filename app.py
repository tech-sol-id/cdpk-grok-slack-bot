import os
import re
import json
import math
import base64
import requests
import urllib.request
import logging
import threading
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

ALL_TOOLS = DOC_TOOLS + REMINDER_TOOLS

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

    return text

def ask_grok(messages: list, client=None, channel: str = None, thread_ts: str = None, user_id: str = None) -> str:
    """Mengirim pesan ke xAI Grok API dengan dukungan Tool Calling untuk Dokumen & Reminder."""
    try:
        response = ai_client.chat.completions.create(
            model=XAI_MODEL,
            messages=messages,
            tools=ALL_TOOLS,
            tool_choice="auto",
            temperature=0.7,
        )
        msg = response.choices[0].message

        # Jika Grok memanggil tool (generate dokumen atau reminder)
        if msg.tool_calls:
            tool_call_messages = list(messages)
            tool_call_messages.append(msg)
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

                tool_call_messages.append({
                    "role": "tool",
                    "tool_call_id": tc.id,
                    "content": tool_output_str
                })

            final_resp = ai_client.chat.completions.create(
                model=XAI_MODEL,
                messages=tool_call_messages,
                temperature=0.7,
            )
            content = final_resp.choices[0].message.content or ""
            if uploaded_notices:
                content += "\n\n" + "\n".join(uploaded_notices)
            return format_slack_text(content)

        return format_slack_text(msg.content or "")
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

    # Normalisasi teks query (contoh i.safe, i-safe -> isafe)
    cleaned_query = query.lower()
    cleaned_query = re.sub(r'i[\.\-_ ]safe', 'isafe', cleaned_query)

    raw_tokens = [t.lower() for t in re.findall(r'[a-zA-Z0-9]+', cleaned_query) if len(t) >= 2]
    stop_words = {
        "apa", "dan", "yang", "di", "ke", "dari", "ini", "itu", "untuk", "pada", "adalah",
        "saya", "bisa", "bagaimana", "apakah", "ttg", "tentang", "jelaskan", "tolong", "info", "kasih",
        "minta", "berikan", "kirim", "lihat", "cari", "tampilkan", "sebutkan", "dong", "ya", "mohon", "cek"
    }
    search_tokens = [t for t in raw_tokens if t not in stop_words and len(t) >= 3]
    if not search_tokens:
        search_tokens = raw_tokens

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
    for st in search_tokens:
        if st in brand_aliases:
            expanded_tokens.extend(brand_aliases[st])

    # Deteksi kode model/produk (mengandung kombinasi huruf & angka, misal 'is540', 'is440', 'slr5000', 'rg170')
    product_codes = [t for t in expanded_tokens if any(c.isdigit() for c in t) and any(c.isalpha() for c in t)]

    # Sinonim istilah teknis dari Bahasa Indonesia ke Bahasa Inggris untuk dokumen internasional
    synonyms = {
        "spesifikasi": ["specification", "specifications", "technical features", "datasheet", "features"],
        "spek": ["specification", "specifications", "technical features", "datasheet"],
        "brosur": ["brochure", "flyer"],
        "panduan": ["manual", "guide", "operating manual"],
        "instruksi": ["instructions", "safety"],
        "topologi": ["topology", "das", "riser", "omu", "oru", "antenna", "splitter", "coupler", "coverage"],
        "desain": ["design", "das", "omu", "oru", "architecture", "diagram"],
        "gambar": ["diagram", "schematic", "blueprint", "plan", "riser"],
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
        "🔒 SUMBER DATA PERUSAHAAN & INTEGRITAS PENGETAHUAN CDPK HQ:\n"
        "1. SUMBER DATA PERUSAHAAN: Untuk arsip perusahaan, profil, laporan keuangan, data karyawan, dan spesifikasi produk internal, dasarkan pada arsip pengetahuan resmi CDPK HQ di bawah ini.\n"
        "2. DOMAIN BISNIS RESMI: CDPK HQ bergerak di bidang SOLUSI KOMUNIKASI RADIO NIRKABEL PROFESIONAL (Motorola Solutions, FMTCS Solutions, POCStar, Tramigo), PERALATAN OUTDOOR & DIVING (Skywoods), serta PERANGKAT INTRINSICALLY SAFE ATEX/EX (i.Safe Mobile).\n"
        "3. ANTI-HALUSINASI SINGKATAN/ISTILAH: DILARANG mengartikan singkatan internal/produk (seperti FMTCS, IMS, FMTCS-LRF, POCStar, MCX, DMR, DAS, ATEX, HazLoc) ke bidang lain di luar bisnis telekomunikasi CDPK HQ. FMTCS adalah penyedia solusi sistem komunikasi nirkabel dan DAS mitra resmi CDPK HQ.\n"
        "4. ANALISIS MULTIMODAL BLUEPRINT & GAMBAR: Jika pengguna melampirkan gambar skema, blueprint, denah, atau riser diagram kabel, Anda WAJIB menganalisis secara visual gambar tersebut, mengidentifikasi arsitektur gedung/lantai/riser, serta merekomendasikan solusi sistem DAS & radio CDPK HQ (FMTCS / Motorola).\n"
        "5. JIKA INFORMASI ARSIP TIDAK DITEMUKAN: Hanya jika pengguna menanyakan fakta/arsip internal perusahaan yang tidak ada di data arsip dan tidak melampirkan gambar untuk dianalisis, nyatakan: 'Informasi arsip tersebut tidak ditemukan dalam basis pengetahuan resmi CDPK HQ.'\n"
        "6. REFERENSI RESMI: Jika merujuk dokumen tertentu, sebutkan nama subjek dokumen secara wajar tanpa menyebut ekstensi teknis file."
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
        f"   - Jika pengguna meminta membatalkan pengingat, PANGGIL TOOL 'cancel_reminder'."
    )

    prompt_parts = [
        SYSTEM_PROMPT,
        rbac_instruction,
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
    messages = [{"role": "system", "content": get_effective_system_prompt(user_access, query=query)}]
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
            {"role": "system", "content": get_effective_system_prompt(user_access, query=user_text)},
            {"role": "user", "content": user_content}
        ]

    # Dapatkan jawaban dari Grok (dengan dukungan tool calling untuk Dokumen & Reminder)
    reply = ask_grok(conversation, client=client, channel=channel, thread_ts=thread_ts, user_id=user_id)

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
    media_items = get_media_items_for_message(client, event["channel"], event)

    if not user_text and not media_items:
        return

    if not user_text and media_items:
        user_text = "Mohon pelajari dan analisis spesifikasi dari gambar/dokumen teknis yang saya lampirkan ini, serta berikan rekomendasi solusi yang tepat sesuai standar CDPK HQ."

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

    user_content = [{"type": "text", "text": user_text}] + media_items if media_items else user_text

    conversation = [
        {"role": "system", "content": get_effective_system_prompt(user_access, query=user_text)},
        {"role": "user", "content": user_content}
    ]

    reply = ask_grok(conversation, client=client, channel=event["channel"], thread_ts=None, user_id=user_id)
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

    # Aktifkan scheduler background worker pengingat tim 24/7
    start_reminder_worker(app.client)

    logger.info("Memulai Grok Slack Bot dalam Socket Mode...")
    handler = SocketModeHandler(app, SLACK_APP_TOKEN)
    handler.start()

