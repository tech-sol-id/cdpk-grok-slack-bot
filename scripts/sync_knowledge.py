#!/usr/bin/env python3
"""
CDPK HQ Knowledge Base Ingestion Pipeline
Menyinkronkan dokumen dari Google Drive (termasuk folder Shortcuts),
mengekstraksi dan menstrukturkan dokumen menggunakan Google Gemini 3.8 Flash,
lalu menyimpannya sebagai Markdown (.md) terstruktur di folder knowledge/.

Mandat Tugas Gemini:
1. Salin Lengkap (tanpa menghilangkan fakta/rincian/angka)
2. Ringkasan Eksekutif (Executive Summary)
3. Struktur Dokumen Rapi (Heading, Bullet, Table)
4. FAQ Otomatis Karyawan (Antisipasi pertanyaan tim)
5. Metadata Sumber Dokumen (Referensi asal)
"""

import os
import sys
import json
import urllib.request
import urllib.parse
import re
from datetime import datetime

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
kategori: "Kebijakan & SOP CDPK HQ"
---

2. JUDUL UTAMA (# [Judul Dokumen yang Jelas])

3. ## 📌 Executive Summary
Tuliskan 3 - 5 poin inti paling penting dari dokumen ini secara padat dan lugas.

4. ## 📖 Salinan Lengkap & Terstruktur
Salin dan tata ulang SELURUH isi dokumen asli secara lengkap tanpa memangkas fakta penting.
- Gunakan hierarki heading yang rapi (###, ####).
- Ubah daftar atau poin-poin menjadi bullet list yang bersih.
- Ubah data tabular atau perbandingan menjadi Tabel Markdown yang rapi.
- PENTING: JANGAN LAKUKAN SENSOR terhadap data angka, gaji, atau rincian spesifik. Salin apa adanya secara akurat karena kontrol akses pengguna akan diatur secara dinamis oleh sistem.

5. ## ❓ Antisipasi Pertanyaan Karyawan (FAQ Otomatis)
Buatkan minimal 3 - 7 pasang Pertanyaan & Jawaban (Q&A) yang paling mungkin ditanyakan oleh staf/karyawan di Slack mengenai dokumen ini. Gunakan gaya bahasa alami sehari-hari.

6. ## 📚 Glosarium & Istilah Penting
Jika ada singkatan atau terminologi teknis/internal (misal: SLA, KPI, CDPK, SOP), buatkan daftar definisi ringkasnya.

Hasilkan Markdown murni tanpa pembuka/penutup percakapan tambahan.
"""

def call_gemini(source_filename: str, folder_name: str, raw_content: str) -> str:
    """Memanggil Gemini 3.8 Flash untuk memproses dokumen menjadi Markdown lengkap."""
    if not GEMINI_API_KEY:
        print("Peringatan: GEMINI_API_KEY tidak ditemukan!")
        return raw_content

    extraction_date = datetime.now().strftime("%Y-%m-%d")
    system_instruction = GEMINI_PROMPT_TEMPLATE.format(
        source_filename=source_filename,
        folder_name=folder_name,
        extraction_date=extraction_date
    )

    url = f"https://generativelanguage.googleapis.com/v1beta/models/gemini-3.8-flash:generateContent?key={GEMINI_API_KEY}"
    payload = {
        "contents": [
            {
                "parts": [
                    {"text": system_instruction},
                    {"text": f"\n\n--- DOKUMEN MENTAH DARI GOOGLE DRIVE ---\n{raw_content}"}
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

def main():
    print(f"[{datetime.now().strftime('%Y-%m-%d %H:%M:%S')}] Memulai Knowledge Ingestion Pipeline")
    print(f"Target Root Folder ID: {FOLDER_ID}")
    os.makedirs(KNOWLEDGE_DIR, exist_ok=True)

    if not GEMINI_API_KEY:
        print("ERROR: GEMINI_API_KEY belum dikonfigurasi.")
        sys.exit(1)

    print("Pipeline siap memproses dokumen & shortcut Google Drive.")

if __name__ == "__main__":
    main()
