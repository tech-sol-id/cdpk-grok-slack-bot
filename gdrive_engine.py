import os
import re
import json
import time
import logging
import requests
from typing import Optional, Dict, Any, List

logger = logging.getLogger("slack-grok-bot")

# In-memory cache untuk OAuth access token agar tidak berulang kali memanggil OAuth endpoint
_TOKEN_CACHE: Dict[str, Dict[str, Any]] = {}

# ID Shared Drive khusus Direksi
BOD_DRIVE_ID = "0AD2z884cgWxCUk9PVA"

# Kelompok Kata Kunci Konfidensial DIREKSI SAJA
DIREKSI_ONLY_KEYWORDS = [
    "corporate", "direksi", "bod drive", "hrd", "personalia", "legalitas", "akta",
    "gaji", "payroll", "salary", "upah", "dividen", "bonus", "pajak direksi", "saham"
]

# Kelompok Kata Kunci FINANCE & ORDER MANAGEMENT
FINANCE_KEYWORDS = [
    "finance", "accounting", "keuangan", "order management", "invoice", "faktur",
    "kas kecil", "laba rugi", "neraca", "rekening", "po customer", "purchase order"
]

# Kelompok Dokumen UMUM Resmi CDPK HQ:
# ATEX, FMTCS, i.Safe Mobile, IMS, Marketing, OPERATIONS, POCStar, SafeUEM, Sales, RugGear, dll.

def get_account_credential(account_key: str) -> Optional[Dict[str, str]]:
    """
    Mengambil kredensial OAuth untuk akun tertentu:
    - account_key: 'citradata', 'techsolutions', atau 'personal'
    Mencari dari Environment Variable terlebih dahulu (untuk server Render),
    kemudian fallback ke direktori lokal ~/.gemini/antigravity/plugin_data/gdrive/.
    """
    key_norm = account_key.lower().strip()
    env_map = {
        "citradata": "GDRIVE_CITRADATA_CRED",
        "techsolutions": "GDRIVE_TECHSOLUTIONS_CRED",
        "personal": "GDRIVE_PERSONAL_CRED",
        "adrian": "GDRIVE_PERSONAL_CRED"
    }

    env_var_name = env_map.get(key_norm)
    if env_var_name and os.environ.get(env_var_name):
        try:
            cred = json.loads(os.environ[env_var_name])
            if cred.get("client_id") and cred.get("client_secret") and cred.get("refresh_token"):
                return cred
        except Exception as e:
            logger.warning(f"Gagal mem-parsing env var {env_var_name}: {e}")

    # Fallback ke file token lokal di ~/.gemini/antigravity/plugin_data/gdrive/
    local_files = {
        "citradata": os.path.expanduser("~/.gemini/antigravity/plugin_data/gdrive/token_adrian@citradata.id.json"),
        "techsolutions": os.path.expanduser("~/.gemini/antigravity/plugin_data/gdrive/token_hq@techsolutions.id.json"),
        "personal": os.path.expanduser("~/.gemini/antigravity/plugin_data/gdrive/token_adrian.kansil@gmail.com.json"),
        "adrian": os.path.expanduser("~/.gemini/antigravity/plugin_data/gdrive/token_adrian.kansil@gmail.com.json")
    }

    file_path = local_files.get(key_norm)
    if file_path and os.path.exists(file_path):
        try:
            with open(file_path, "r", encoding="utf-8") as f:
                d = json.load(f)
            tok = d.get("token", {})
            return {
                "client_id": d.get("client_id"),
                "client_secret": d.get("client_secret"),
                "refresh_token": tok.get("refresh_token") if isinstance(tok, dict) else d.get("refresh_token"),
                "email": d.get("email", "")
            }
        except Exception as e:
            logger.warning(f"Gagal membaca token file lokal {file_path}: {e}")

    return None

def get_access_token(account_key: str) -> Optional[str]:
    """Mengembalikan access token yang valid untuk akun tertentu (dengan caching otomatis)."""
    now = time.time()
    cached = _TOKEN_CACHE.get(account_key)
    if cached and cached.get("access_token") and cached.get("expires_at", 0) > now + 120:
        return cached["access_token"]

    cred = get_account_credential(account_key)
    if not cred or not cred.get("refresh_token"):
        logger.warning(f"Kredensial Google Drive untuk akun '{account_key}' tidak ditemukan.")
        return None

    try:
        r = requests.post(
            "https://oauth2.googleapis.com/token",
            data={
                "client_id": cred["client_id"],
                "client_secret": cred["client_secret"],
                "refresh_token": cred["refresh_token"],
                "grant_type": "refresh_token"
            },
            timeout=10
        )
        if r.status_code == 200:
            res_data = r.json()
            access_tok = res_data["access_token"]
            expires_in = res_data.get("expires_in", 3600)
            _TOKEN_CACHE[account_key] = {
                "access_token": access_tok,
                "expires_at": now + expires_in
            }
            logger.info(f"Berhasil me-refresh access token Google Drive ({account_key})")
            return access_tok
        else:
            logger.error(f"Gagal me-refresh OAuth token ({account_key}): HTTP {r.status_code} - {r.text}")
    except Exception as e:
        logger.error(f"Exception saat me-refresh token Google Drive ({account_key}): {e}")

    return None

def search_google_drive(query: str, account: str = "all", max_results: int = 5, user_access: dict = None) -> str:
    """
    Mencari file dan dokumen di Google Drive resmi CDPK HQ.
    Ketentuan Hak Akses & Scope:
    1. Akun Personal (adrian.kansil@gmail.com): DIBATASI KHUSUS HANYA UNTUK USER ADRIAN.
    2. Scope Pencarian: HANYA Shared Drives / Team Drive untuk selain Adrian (DILARANG mencari di My Drive).
    3. Klasifikasi Tier:
       - DIREKSI: Dokumen Umum, Finance, Corporate, Direksi/BOD Drive, HRD, Personalia, Legalitas, Gaji.
       - FINANCE: Dokumen Umum, Finance & Accounting, Order Management. (Dilarang Corporate/Direksi/HRD/Legalitas/Gaji).
       - UMUM: HANYA Dokumen Umum (ATEX, FMTCS, i.Safe Mobile, IMS, Marketing, OPERATIONS, POCStar, SafeUEM, Sales, RugGear, dll).
    """
    if not query:
        return "Query pencarian Google Drive tidak boleh kosong."

    user_access = user_access or {}
    user_level = user_access.get("level", "STANDARD") or "STANDARD"
    is_adrian = bool(
        user_access.get("is_adrian") or
        user_access.get("user_id") == "U0C2CR9NAF7" or
        "adrian@citradata.id" in user_access.get("email", "").lower()
    )

    clean_query = query.strip().replace("'", "\\'")
    q_lower = clean_query.lower()

    # --- PENEGAKAN HAK AKSES PADA QUERY INPUT ---
    if user_level != "DIREKSI":
        # Blocklist untuk selain Direksi (Finance & Umum)
        if any(w in q_lower for w in DIREKSI_ONLY_KEYWORDS):
            return "🔒 *Akses Ditolak:* Dokumen kelompok Corporate, Folder Direksi, HRD, Personalia, Legalitas, dan Penggajian (Gaji) bersifat konfidensial dan HANYA dapat diakses oleh jajaran Direksi CDPK HQ."

        # Blocklist tambahan untuk Umum (Staf Biasa)
        if user_level == "STANDARD":
            if any(w in q_lower for w in FINANCE_KEYWORDS):
                return "🔒 *Akses Ditolak:* Dokumen Finance & Accounting serta Order Management bersifat konfidensial dan hanya dapat diakses oleh Tim Finance atau Direksi CDPK HQ."

    # --- PENEGAKAN AKUN PERSONAL (HANYA ADRIAN) ---
    acc_lower = account.lower().strip()
    if acc_lower in ["personal", "adrian"]:
        if not is_adrian:
            return "🔒 *Akses Ditolak:* Akun Google Drive Personal (adrian.kansil@gmail.com) dibatasi secara khusus dan HANYA boleh diakses oleh Pak Adrian."
        accounts_to_check = [("personal", "Personal Adrian (adrian.kansil@gmail.com)")]
    elif acc_lower in ["citradata", "kerja", "kantor", "cdpk"]:
        accounts_to_check = [("citradata", "Citradata HQ")]
    elif acc_lower in ["techsolutions", "ts"]:
        accounts_to_check = [("techsolutions", "Techsolutions")]
    else:  # default 'all'
        accounts_to_check = [
            ("citradata", "Citradata HQ"),
            ("techsolutions", "Techsolutions")
        ]
        # Sertakan akun personal HANYA jika penanya adalah Pak Adrian
        if is_adrian:
            accounts_to_check.append(("personal", "Personal Adrian"))

    all_matches = []

    for acc_key, acc_label in accounts_to_check:
        tok = get_access_token(acc_key)
        if not tok:
            continue

        headers = {"Authorization": f"Bearer {tok}"}
        drive_q = f"name contains '{clean_query}' and trashed = false"

        try:
            r = requests.get(
                "https://www.googleapis.com/drive/v3/files",
                headers=headers,
                params={
                    "q": drive_q,
                    "fields": "files(id, name, mimeType, webViewLink, size, modifiedTime, driveId, teamDriveId)",
                    "pageSize": max_results * 2,  # ambil buffer untuk filtering scope
                    "supportsAllDrives": "true",
                    "includeItemsFromAllDrives": "true",
                    "orderBy": "modifiedTime desc"
                },
                timeout=12
            )
            if r.status_code == 200:
                files = r.json().get("files", [])
                for f in files:
                    drive_id = f.get("driveId") or f.get("teamDriveId")
                    # PENEGAKAN ATURAN SCOPE:
                    # User selain Adrian HANYA boleh mengakses Shared Drives / Team Drive (DILARANG My Drive)
                    if not is_adrian and not drive_id:
                        continue

                    all_matches.append({
                        "id": f.get("id"),
                        "name": f.get("name"),
                        "mimeType": f.get("mimeType", ""),
                        "link": f.get("webViewLink", ""),
                        "size": f.get("size", "0"),
                        "modified": f.get("modifiedTime", "")[:10],
                        "driveId": drive_id,
                        "account": acc_label
                    })
            else:
                logger.warning(f"Drive search gagal untuk {acc_key}: HTTP {r.status_code} - {r.text}")
        except Exception as e:
            logger.warning(f"Error saat mencari file Drive di {acc_key}: {e}")

    # --- PENEGAKAN HAK AKSES PADA DAFTAR BERKAS HASIL PENCARIAN ---
    filtered_matches = []
    for item in all_matches:
        fn_low = item["name"].lower()
        drive_id = item.get("driveId")

        # 1. Non-Direksi dilarang mengakses berkas di BOD Drive atau berkas dengan kata kunci Direksi/HRD/Legal/Gaji
        if user_level != "DIREKSI":
            if drive_id == BOD_DRIVE_ID:
                continue
            if any(w in fn_low for w in DIREKSI_ONLY_KEYWORDS):
                continue

            # 2. Staf Umum dilarang mengakses berkas kategori Finance & Order Management
            if user_level == "STANDARD":
                if any(w in fn_low for w in FINANCE_KEYWORDS):
                    continue

        filtered_matches.append(item)

    if not filtered_matches:
        scope_desc = "Shared Drives resmi CDPK" if not is_adrian else "Google Drive CDPK"
        return f"Tidak ditemukan berkas di {scope_desc} yang sesuai dengan wewenang akses Anda untuk kata kunci '*{clean_query}*'."

    # Format keluaran rapi untuk Slack dengan pembatasan token ketat (Token Guard)
    scope_title = "Shared Drives CDPK" if not is_adrian else "Google Drive CDPK"
    lines = [f"📂 Hasil pencarian berkas di *{scope_title}* untuk '*{clean_query}*':\n"]

    for idx, item in enumerate(filtered_matches[:max_results], 1):
        # Format ukuran file
        size_str = ""
        try:
            bytes_val = int(item["size"])
            if bytes_val > 1024 * 1024:
                size_str = f" ({bytes_val / (1024*1024):.1f} MB)"
            elif bytes_val > 1024:
                size_str = f" ({bytes_val / 1024:.0f} KB)"
        except Exception:
            pass

        # Format tipe dokumen
        mime = item["mimeType"]
        type_icon = "📄"
        type_name = "Berkas"
        if "spreadsheet" in mime or "sheet" in mime:
            type_icon = "📊"
            type_name = "Spreadsheet"
        elif "pdf" in mime:
            type_icon = "📕"
            type_name = "PDF"
        elif "document" in mime or "word" in mime:
            type_icon = "📝"
            type_name = "Dokumen"

        drive_tag = "Shared Drive" if item.get("driveId") else "My Drive (Pribadi)"

        lines.append(f"{idx}. {type_icon} *{item['name']}*{size_str}")
        lines.append(f"   • Tipe: {type_name} | Scope: {drive_tag} | Update: {item['modified']}")
        lines.append(f"   • ID: `{item['id']}`")
        if item["link"]:
            lines.append(f"   • Buka Berkas: <{item['link']}|Akses Dokumen di Google Drive>\n")
        else:
            lines.append("\n")

    output = "\n".join(lines).strip()
    return output[:1500]

def read_google_drive_file(file_id: str, account: str = "citradata", max_chars: int = 1800, user_access: dict = None) -> str:
    """
    Membaca dan mengekstrak isi teks/ringkasan data dari berkas Google Drive
    dengan verifikasi ketat Hak Akses 3-Tier RBAC dan Scope Shared Drive.
    """
    if not file_id:
        return "ID file Google Drive tidak boleh kosong."

    user_access = user_access or {}
    user_level = user_access.get("level", "STANDARD") or "STANDARD"
    is_adrian = bool(
        user_access.get("is_adrian") or
        user_access.get("user_id") == "U0C2CR9NAF7" or
        "adrian@citradata.id" in user_access.get("email", "").lower()
    )

    clean_file_id = file_id.strip()

    # --- PENEGAKAN AKSES AKUN PERSONAL ---
    if account.lower() in ["personal", "adrian"] and not is_adrian:
        return "🔒 *Akses Ditolak:* Berkas pada akun Personal (adrian.kansil@gmail.com) dibatasi khusus dan HANYA boleh diakses oleh Pak Adrian."

    # Cek token akun yang sesuai
    acc_key = "citradata" if account.lower() not in ["techsolutions", "personal"] else account.lower()
    tok = get_access_token(acc_key)
    if not tok:
        for fallback_acc in ["techsolutions", "personal"]:
            tok = get_access_token(fallback_acc)
            if tok:
                acc_key = fallback_acc
                break

    if not tok:
        return f"Gagal mengakses Google Drive: Tidak dapat mengautentikasi akun '{account}'."

    headers = {"Authorization": f"Bearer {tok}"}

    # 1. Ambil metadata file terlebih dahulu
    try:
        m_res = requests.get(
            f"https://www.googleapis.com/drive/v3/files/{clean_file_id}",
            headers=headers,
            params={"fields": "id, name, mimeType, webViewLink, size, driveId, teamDriveId", "supportsAllDrives": "true"},
            timeout=10
        )
        if m_res.status_code != 200:
            return f"Gagal mengambil metadata file Google Drive `{clean_file_id}` (HTTP {m_res.status_code})."
        meta = m_res.json()
    except Exception as e:
        return f"Terjadi kesalahan saat memeriksa file Google Drive `{clean_file_id}`: {e}"

    fname = meta.get("name", "Dokumen")
    mime = meta.get("mimeType", "")
    link = meta.get("webViewLink", "")
    drive_id = meta.get("driveId") or meta.get("teamDriveId")
    fn_low = fname.lower()

    # --- PENEGAKAN ATURAN SCOPE (HANYA SHARED DRIVE UNTUK SELAIN ADRIAN) ---
    if not is_adrian and not drive_id:
        return f"🔒 *Akses Ditolak:* Dokumen '*{fname}*' berada di My Drive pribadi. Pengguna selain Pak Adrian hanya berhak mengakses dokumen pada Shared Drives / Team Drive resmi CDPK HQ."

    # --- PENEGAKAN ATURAN HAK AKSES TIER PADA BERKAS ---
    if user_level != "DIREKSI":
        # Dilarang buka berkas BOD Drive atau nama mengandung Corporate/Direksi/HRD/Legalitas/Gaji
        if drive_id == BOD_DRIVE_ID or any(w in fn_low for w in DIREKSI_ONLY_KEYWORDS):
            return f"🔒 *Akses Ditolak:* Dokumen '*{fname}*' merupakan kelompok dokumen konfidensial Direksi/Corporate/HRD/Legalitas/Gaji dan HANYA dapat dibuka oleh jajaran Direksi CDPK HQ."

        # Staf Umum dilarang buka berkas Finance & Order Management
        if user_level == "STANDARD":
            if any(w in fn_low for w in FINANCE_KEYWORDS):
                return f"🔒 *Akses Ditolak:* Dokumen '*{fname}*' merupakan berkas Finance & Accounting / Order Management dan HANYA dapat dibuka oleh Tim Finance atau Direksi CDPK HQ."

    logger.info(f"Membaca file Drive '{fname}' ({mime}) [User Level: {user_level}, is_adrian: {is_adrian}]")

    # 2. Kasus A: Google Spreadsheet (Export ke CSV dan ambil baris awal)
    if mime == "application/vnd.google-apps.spreadsheet":
        try:
            exp_res = requests.get(
                f"https://www.googleapis.com/drive/v3/files/{clean_file_id}/export",
                headers=headers,
                params={"mimeType": "text/csv"},
                timeout=15
            )
            if exp_res.status_code == 200:
                raw_lines = exp_res.text.splitlines()
                valid_lines = [l for l in raw_lines if l.strip().replace(",", "")]
                preview_lines = valid_lines[:15]
                content_preview = "\n".join(preview_lines)
                res = (
                    f"📊 *Ringkasan Isi Spreadsheet:* <{link}|{fname}>\n"
                    f"• *Pratinjau Data (15 Baris Pertama):*\n```\n{content_preview[:max_chars]}\n```"
                )
                return res[:max_chars + 300]
        except Exception as e:
            logger.warning(f"Gagal mengekspor Google Sheet {clean_file_id}: {e}")

    # 3. Kasus B: Google Document (Export ke text/plain)
    elif mime == "application/vnd.google-apps.document":
        try:
            exp_res = requests.get(
                f"https://www.googleapis.com/drive/v3/files/{clean_file_id}/export",
                headers=headers,
                params={"mimeType": "text/plain"},
                timeout=15
            )
            if exp_res.status_code == 200:
                text_content = exp_res.text.strip()
                res = (
                    f"📝 *Ringkasan Dokumen Google Docs:* <{link}|{fname}>\n"
                    f"• *Isi Teks Dokumen:*\n{text_content[:max_chars]}"
                )
                return res[:max_chars + 200]
        except Exception as e:
            logger.warning(f"Gagal mengekspor Google Doc {clean_file_id}: {e}")

    # 4. Kasus C: Dokumen PDF (Unduh binary dan ekstrak teks via PyMuPDF)
    elif "pdf" in mime or fname.lower().endswith(".pdf"):
        try:
            down_res = requests.get(
                f"https://www.googleapis.com/drive/v3/files/{clean_file_id}",
                headers=headers,
                params={"alt": "media", "supportsAllDrives": "true"},
                timeout=20
            )
            if down_res.status_code == 200:
                import fitz  # PyMuPDF
                doc = fitz.open(stream=down_res.content, filetype="pdf")
                extracted_pages = []
                for p_idx in range(min(3, len(doc))):
                    page_text = doc[p_idx].get_text().strip()
                    if page_text:
                        extracted_pages.append(f"--- Halaman {p_idx+1} ---\n{page_text}")
                doc.close()
                combined_text = "\n\n".join(extracted_pages).strip()
                if combined_text:
                    res = (
                        f"📕 *Ekstraksi Teks PDF:* <{link}|{fname}>\n"
                        f"• *Cuplikan Konten:*\n{combined_text[:max_chars]}"
                    )
                else:
                    res = (
                        f"📕 *Berkas PDF:* <{link}|{fname}>\n"
                        f"• Catatan: Berkas PDF ini berisi gambar/grafik teknis tanpa lapisan teks digital. Silakan akses langsung tautan dokumen di atas."
                    )
                return res[:max_chars + 200]
        except Exception as e:
            logger.warning(f"Gagal mengekstrak teks PDF {clean_file_id}: {e}")

    # 5. Fallback Default
    return (
        f"📄 *Berkas Google Drive Ditemukan:* <{link}|{fname}>\n"
        f"• Tipe MIME: `{mime}`\n"
        f"• File ini siap diakses langsung oleh tim melalui tautan di atas."
    )

# Definisi Function Calling Tools untuk Grok API
GDRIVE_TOOLS = [
    {
        "type": "function",
        "function": {
            "name": "search_google_drive",
            "description": "Mencari berkas, dokumen, spreadsheet stok, datasheet teknis, atau proposal di Shared Drives resmi CDPK HQ (Citradata dan Techsolutions) berdasarkan kata kunci pencarian. Sesuai regulasi, pencarian pada My Drive dan akun personal hanya diperbolehkan untuk Pak Adrian.",
            "parameters": {
                "type": "object",
                "properties": {
                    "query": {
                        "type": "string",
                        "description": "Kata kunci pencarian nama atau subjek dokumen (contoh: 'stock', 'p8668i', 'phe onwj', 'pricing ruggear', 'datasheet repeater')"
                    },
                    "account": {
                        "type": "string",
                        "enum": ["all", "citradata", "techsolutions", "personal"],
                        "description": "Akun Google Drive target. Gunakan 'citradata' (default), 'techsolutions', atau 'all'. Opsi 'personal' hanya dapat diakses oleh Pak Adrian."
                    }
                },
                "required": ["query"]
            }
        }
    },
    {
        "type": "function",
        "function": {
            "name": "read_google_drive_file",
            "description": "Membaca dan merangkum isi data dari sebuah file Google Drive (Google Sheet, Google Doc, atau PDF) menggunakan ID berkas yang diperoleh dari pencarian.",
            "parameters": {
                "type": "object",
                "properties": {
                    "file_id": {
                        "type": "string",
                        "description": "ID unik file Google Drive (contoh: '1-0oZE_SZ6_mjLXvDylldFMBvd0-GAFwo')"
                    },
                    "account": {
                        "type": "string",
                        "enum": ["citradata", "techsolutions", "personal"],
                        "description": "Akun Google Drive pemilik berkas (default 'citradata')"
                    }
                },
                "required": ["file_id"]
            }
        }
    }
]
