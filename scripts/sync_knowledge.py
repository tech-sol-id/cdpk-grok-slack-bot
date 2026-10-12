#!/usr/bin/env python3
"""
CDPK HQ Knowledge Base Ingestion Pipeline
Menyinkronkan dokumen dari Google Drive, mengekstrak dan merapikannya
menjadi format Markdown (.md) menggunakan Google Gemini AI, lalu menyimpannya di knowledge/.
"""

import os
import sys
import json
import urllib.request
import urllib.parse
import re

FOLDER_ID = os.environ.get("GDRIVE_FOLDER_ID", "1oF8gzaqV1UUdug08KlkKAPomjHsbRL4q")
GEMINI_API_KEY = os.environ.get("GEMINI_API_KEY")
KNOWLEDGE_DIR = os.path.join(os.path.dirname(os.path.dirname(__file__)), "knowledge")

def call_gemini(prompt: str, text_content: str) -> str:
    """Memanggil Gemini 3.8 Flash untuk merapikan teks dokumen menjadi Markdown."""
    if not GEMINI_API_KEY:
        print("Peringatan: GEMINI_API_KEY tidak ditemukan!")
        return text_content

    url = f"https://generativelanguage.googleapis.com/v1beta/models/gemini-3.8-flash:generateContent?key={GEMINI_API_KEY}"
    payload = {
        "contents": [
            {
                "parts": [
                    {"text": prompt},
                    {"text": f"\n\n--- DOKUMEN ASLI ---\n{text_content}"}
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
        with urllib.request.urlopen(req, timeout=60) as resp:
            data = json.loads(resp.read().decode("utf-8"))
            candidates = data.get("candidates", [])
            if candidates:
                parts = candidates[0].get("content", {}).get("parts", [])
                for part in parts:
                    if "text" in part:
                        return part["text"]
    except Exception as e:
        print(f"Gagal memanggil Gemini API: {e}")
    return text_content

def sanitize_filename(name: str) -> str:
    """Membersihkan nama file agar aman digunakan di sistem berkas."""
    name = re.sub(r"[^\w\s-]", "", name).strip().lower()
    return re.sub(r"[-\s]+", "_", name)

def main():
    print(f"Memulai pipeline Knowledge Ingestion untuk folder: {FOLDER_ID}")
    os.makedirs(KNOWLEDGE_DIR, exist_ok=True)
    
    if not GEMINI_API_KEY:
        print("ERROR: GEMINI_API_KEY wajib diisi.")
        sys.exit(1)
        
    print("Pipeline siap dijalankan di cloud.")

if __name__ == "__main__":
    main()
