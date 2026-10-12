#!/usr/bin/env python3
"""
CDPK HQ Knowledge Base Ingestion Pipeline
Menyinkronkan dokumen dari Google Drive (termasuk folder Shortcuts),
mengekstraksi dan menstrukturkan dokumen menggunakan Google Gemini 3.8 Flash,
lalu menyimpannya sebagai Markdown (.md) terstruktur di folder knowledge/.

Mandat Tugas Gemini:
1. Salin Lengkap (tanpa menghilangkan fakta/rincian/angka & TANPA SENSOR)
2. Ringkasan Eksekutif (Executive Summary)
3. Struktur Dokumen Rapi (Heading, Bullet, Table)
4. FAQ Otomatis Karyawan (Antisipasi pertanyaan tim di Slack)
5. Metadata Sumber Dokumen & Tingkat Akses (Direksi, Finance, Semua)
"""

import os
import sys
import io
import json
import urllib.request
import urllib.parse
import re
from datetime import datetime

try:
    from google.oauth2.credentials import Credentials
    from googleapiclient.discovery import build
except ImportError:
    Credentials = None
    build = None

try:
    import pypdf
except ImportError:
    pypdf = None

try:
    import docx
except ImportError:
    docx = None

FOLDER_ID = os.environ.get("GDRIVE_FOLDER_ID", "1oF8gzaqV1UUdug08KlkKAPomjHsbRL4q")
GEMINI_API_KEY = os.environ.get("GEMINI_API_KEY")
KNOWLEDGE_DIR = os.path.join(os.path.dirname(os.path.dirname(__file__)), "knowledge")

GEMINI_PROMPT_TEMPLATE = """Anda adalah Analis & Editor Basis Pengetahuan Resmi untuk CDPK HQ.
Tugas Anda adalah memproses dokumen kantor berikut dan mengubahnya menjadi berkas Markdown (.md) resmi berkualitas tinggi.

PANDUAN STRUKTUR OUTPUT MARKDOWN:
1. METADATA HEADER (YAML Frontmatter):
---
sumber_dokumen: "{source_filename}"
folder_asal: "{folder_name}"
tanggal_ekstraksi: "{extraction_date}"
tingkat_akses: "{tingkat_akses}"
---

ATURAN KLASIFIKASI TINGKAT AKSES:
- "DIREKSI_SAJA": Dokumen dari folder "Slack - Khusus Direksi" ATAU dokumen membahas tentang "Gaji" / kompensasi.
- "FINANCE_DAN_DIREKSI": Dokumen dari folder "Slack - Finance", "Finance and Accounting", atau "Order Management".
- "SEMUA_MEMBER": Seluruh dokumen umum lainnya (FMTCS, IMS, Operasional, Sales, POCStar, dll).

2. JUDUL UTAMA (# [Judul Dokumen yang Jelas])

3. ## 📌 Executive Summary
Tuliskan 3 - 5 poin inti paling penting dari dokumen ini secara padat dan lugas.

4. ## 📖 Salinan Lengkap & Terstruktur
Salin dan tata ulang SELURUH isi dokumen asli secara lengkap tanpa memangkas fakta penting.
- Gunakan hierarki heading yang rapi (###, ####).
- Ubah daftar atau poin-poin menjadi bullet list yang bersih.
- Ubah data tabular atau perbandingan menjadi Tabel Markdown yang rapi.
- PENTING: JANGAN LAKUKAN SENSOR terhadap data angka, gaji, margin, atau rincian spesifik. Salin apa adanya secara akurat karena kontrol akses pengguna diatur secara dinamis oleh sistem.

5. ## ❓ Antisipasi Pertanyaan Karyawan (FAQ Otomatis)
Buatkan minimal 3 - 7 pasang Pertanyaan & Jawaban (Q&A) yang paling mungkin ditanyakan oleh staf/karyawan di Slack mengenai dokumen ini. Gunakan gaya bahasa alami sehari-hari.

6. ## 📚 Glosarium & Istilah Penting
Jika ada singkatan atau terminologi teknis/internal (misal: SLA, KPI, CDPK, SOP, ATEX, Ex), buatkan daftar definisi ringkasnya.

Hasilkan Markdown murni tanpa pembuka/penutup percakapan tambahan.
"""

def determine_access_level(source_filename: str, folder_path: str) -> str:
    """Menentukan klasifikasi izin akses dokumen berdasarkan nama folder dan judul."""
    fn_lower = source_filename.lower()
    fp_lower = folder_path.lower()

    if "khusus direksi" in fp_lower or "folder direksi" in fp_lower or "gaji" in fn_lower:
        return "DIREKSI_SAJA"
    if any(k in fp_lower for k in ["finance", "accounting", "order management"]):
        return "FINANCE_DAN_DIREKSI"
    return "SEMUA_MEMBER"

def call_gemini(source_filename: str, folder_name: str, raw_content: str) -> str:
    """Memanggil Gemini 3.8 Flash untuk memproses dokumen menjadi Markdown lengkap."""
    if not GEMINI_API_KEY:
        print("Peringatan: GEMINI_API_KEY tidak ditemukan!")
        return raw_content

    extraction_date = datetime.now().strftime("%Y-%m-%d")
    tingkat_akses = determine_access_level(source_filename, folder_name)

    system_instruction = GEMINI_PROMPT_TEMPLATE.format(
        source_filename=source_filename,
        folder_name=folder_name,
        extraction_date=extraction_date,
        tingkat_akses=tingkat_akses
    )

    # Batasi raw_content maksimal ~120,000 karakter agar tidak melebihi buffer single prompt
    truncated_content = raw_content[:120000]
    if len(raw_content) > 120000:
        truncated_content += "\n\n[...Konten panjang dipotong untuk optimalisasi token...]"

    url = f"https://generativelanguage.googleapis.com/v1beta/models/gemini-3.8-flash:generateContent?key={GEMINI_API_KEY}"
    payload = {
        "contents": [
            {
                "parts": [
                    {"text": system_instruction},
                    {"text": f"\n\n--- DOKUMEN MENTAH DARI GOOGLE DRIVE ---\n{truncated_content}"}
                ]
            }
        ]
    }

    req = urllib.request.Request(
        url,
        data=json.dumps(payload).encode("utf-8"),
        headers={"Content-Type": "application/json"},
        method="POST"
    )

    try:
        with urllib.request.urlopen(req, timeout=120) as resp:
            data = json.loads(resp.read().decode("utf-8"))
            candidates = data.get("candidates", [])
            if candidates:
                parts = candidates[0].get("content", {}).get("parts", [])
                result_text = "".join([part.get("text", "") for part in parts])
                if result_text.strip():
                    return result_text.strip()
    except Exception as e:
        print(f"Error saat memanggil Gemini API untuk {source_filename}: {e}")
    
    return raw_content

def sanitize_filename(name: str) -> str:
    """Membersihkan nama file agar aman disimpan di sistem berkas."""
    name = os.path.splitext(name)[0]
    name = re.sub(r"[^\w\s-]", "", name).strip().lower()
    return re.sub(r"[-\s]+", "_", name) + ".md"

def get_drive_service():
    """Menginisialisasi Google Drive API v3 client menggunakan credential cloud atau lokal."""
    if not Credentials or not build:
        raise RuntimeError("google-api-python-client atau google-auth belum terpasang.")

    creds_json = os.environ.get("GDRIVE_CREDENTIALS_JSON")
    data = None
    if creds_json:
        try:
            data = json.loads(creds_json)
        except Exception as e:
            print(f"Error parsing GDRIVE_CREDENTIALS_JSON: {e}")

    if not data:
        local_paths = [
            os.path.expanduser("~/.gemini/antigravity/plugin_data/gdrive/token_hq@techsolutions.id.json"),
            os.path.expanduser("~/.gemini/antigravity/plugin_data/gdrive/token.json")
        ]
        for p in local_paths:
            if os.path.exists(p):
                with open(p, "r", encoding="utf-8") as f:
                    data = json.load(f)
                break

    if not data:
        raise RuntimeError("Credential Google Drive tidak ditemukan di env atau folder lokal!")

    token_info = data.get("token", {})
    creds = Credentials(
        token=token_info.get("access_token"),
        refresh_token=token_info.get("refresh_token"),
        token_uri="https://oauth2.googleapis.com/token",
        client_id=data.get("client_id"),
        client_secret=data.get("client_secret"),
        scopes=data.get("scopes", ["https://www.googleapis.com/auth/drive"])
    )
    return build("drive", "v3", credentials=creds)

def extract_file_content(service, file_id: str, mime_type: str, file_name: str) -> str:
    """Mengekstraksi konten teks dari berbagai tipe file Google Drive."""
    try:
        if mime_type == "application/vnd.google-apps.document":
            res = service.files().export_media(fileId=file_id, mimeType="text/plain").execute()
            return res.decode("utf-8", errors="ignore")

        elif mime_type == "application/vnd.google-apps.spreadsheet":
            res = service.files().export_media(fileId=file_id, mimeType="text/csv").execute()
            return res.decode("utf-8", errors="ignore")

        elif mime_type in ("text/plain", "text/markdown", "text/csv"):
            res = service.files().get_media(fileId=file_id, supportsAllDrives=True).execute()
            return res.decode("utf-8", errors="ignore")

        elif mime_type == "application/pdf" and pypdf:
            res = service.files().get_media(fileId=file_id, supportsAllDrives=True).execute()
            reader = pypdf.PdfReader(io.BytesIO(res))
            pages_text = []
            max_pages = min(30, len(reader.pages))
            for i in range(max_pages):
                text = reader.pages[i].extract_text() or ""
                if text.strip():
                    pages_text.append(f"--- Halaman {i+1} ---\n{text}")
            return "\n\n".join(pages_text)

        elif mime_type == "application/vnd.openxmlformats-officedocument.wordprocessingml.document" and docx:
            res = service.files().get_media(fileId=file_id, supportsAllDrives=True).execute()
            doc = docx.Document(io.BytesIO(res))
            paragraphs = [p.text for p in doc.paragraphs if p.text.strip()]
            return "\n\n".join(paragraphs)

        elif mime_type in (
            "application/vnd.google-apps.presentation",
            "application/vnd.openxmlformats-officedocument.presentationml.presentation",
            "application/vnd.openxmlformats-officedocument.spreadsheetml.sheet"
        ):
            print(f"Skipping binary slide/sheet non-exportable: {file_name}")
            return ""

    except Exception as e:
        print(f"Gagal mengekstrak {file_name} ({mime_type}): {e}")

    return ""

def crawl_drive(service, folder_id: str, folder_path: str = "Root", visited: set = None, max_depth: int = 3):
    """Menelusuri folder dan shortcut Google Drive secara rekursif."""
    if visited is None:
        visited = set()

    if folder_id in visited or max_depth < 0:
        return

    visited.add(folder_id)
    print(f"\n📂 Memindai: {folder_path} (ID: {folder_id})")

    page_token = None
    while True:
        try:
            res = service.files().list(
                q=f"'{folder_id}' in parents and trashed=false",
                fields="nextPageToken, files(id, name, mimeType, shortcutDetails)",
                supportsAllDrives=True,
                includeItemsFromAllDrives=True,
                pageSize=100,
                pageToken=page_token
            ).execute()
        except Exception as e:
            print(f"Gagal membaca folder {folder_path}: {e}")
            break

        files = res.get("files", [])
        for item in files:
            f_id = item["id"]
            f_name = item["name"]
            f_mime = item["mimeType"]
            sc = item.get("shortcutDetails")

            # 1. Penanganan Shortcut
            if sc:
                target_id = sc.get("targetId")
                target_mime = sc.get("targetMimeType")
                if target_mime == "application/vnd.google-apps.folder":
                    crawl_drive(service, target_id, f"{folder_path} / {f_name}", visited, max_depth - 1)
                else:
                    process_file(service, target_id, target_mime, f_name, folder_path)

            # 2. Penanganan Folder Biasa
            elif f_mime == "application/vnd.google-apps.folder":
                crawl_drive(service, f_id, f"{folder_path} / {f_name}", visited, max_depth - 1)

            # 3. Penanganan File Biasa
            else:
                process_file(service, f_id, f_mime, f_name, folder_path)

        page_token = res.get("nextPageToken")
        if not page_token:
            break

def get_target_subfolder(access_level: str) -> str:
    """Mengembalikan nama subfolder khusus berdasarkan kategori hak akses."""
    if access_level == "DIREKSI_SAJA":
        return "direksi"
    elif access_level == "FINANCE_DAN_DIREKSI":
        return "finance"
    return "umum"

def process_file(service, file_id: str, mime_type: str, file_name: str, folder_path: str):
    """Mengekstrak dan mengubah file menjadi berkas Markdown pengetahuan terstruktur via Gemini."""
    if file_name.startswith(".") or file_name.lower() in ("desktop.ini", "thumbs.db", ".ds_store"):
        return

    print(f"  📄 Memproses dokumen: {file_name} ({mime_type})")
    raw_text = extract_file_content(service, file_id, mime_type, file_name)

    if not raw_text or len(raw_text.strip()) < 40:
        print(f"     ⏭️ Dilewati (konten teks terlalu singkat atau kosong).")
        return

    access_level = determine_access_level(file_name, folder_path)
    subfolder = get_target_subfolder(access_level)
    target_dir = os.path.join(KNOWLEDGE_DIR, subfolder)
    os.makedirs(target_dir, exist_ok=True)

    print(f"     🤖 Mengonversi dengan Gemini 3.8 Flash (Tingkat Akses: {access_level} -> {subfolder}/)...")
    md_content = call_gemini(file_name, folder_path, raw_text)

    safe_name = sanitize_filename(file_name)
    target_path = os.path.join(target_dir, safe_name)

    with open(target_path, "w", encoding="utf-8") as f:
        f.write(md_content)

    print(f"     ✅ Berhasil disimpan ke: knowledge/{subfolder}/{safe_name}")

def main():
    print(f"[{datetime.now().strftime('%Y-%m-%d %H:%M:%S')}] Memulai CDPK HQ Knowledge Ingestion Pipeline")
    print(f"Target Root Folder ID: {FOLDER_ID}")
    for sub in ["direksi", "finance", "umum"]:
        os.makedirs(os.path.join(KNOWLEDGE_DIR, sub), exist_ok=True)

    if not GEMINI_API_KEY:
        print("ERROR: GEMINI_API_KEY belum dikonfigurasi.")
        sys.exit(1)

    try:
        service = get_drive_service()
        print("Koneksi Google Drive API berhasil diinisialisasi.")
        crawl_drive(service, FOLDER_ID, "Root Knowledge")
        print(f"\n🎉 Ingestion selesai! Dokumen tersimpan di: {KNOWLEDGE_DIR}")
    except Exception as e:
        print(f"ERROR kritis dalam pipeline: {e}")
        sys.exit(1)

if __name__ == "__main__":
    main()
