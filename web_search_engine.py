import os
import re
import logging
import urllib.parse
import requests
from bs4 import BeautifulSoup

logger = logging.getLogger("slack-grok-bot")

def perform_web_search(query: str, max_results: int = 3) -> str:
    """
    Melakukan pencarian live di internet menggunakan engine DDGS (dengan fallback Wikipedia API)
    serta menerapkan proteksi penghemat token (maksimal 1.500 karakter / ~300 token).
    """
    if not query:
        return "Query pencarian tidak boleh kosong."

    clean_query = query.strip()
    logger.info(f"Menjalankan live web search untuk query: '{clean_query}'")

    results = []

    # 1. Metode Utama: DDGS (DuckDuckGo Search Engine)
    try:
        try:
            from ddgs import DDGS
        except ImportError:
            from duckduckgo_search import DDGS
        with DDGS() as ddgs:
            raw_results = list(ddgs.text(clean_query, max_results=max_results))
            for item in raw_results:
                title = item.get("title", "").strip()
                link = item.get("href", "").strip()
                body = item.get("body", "").strip()
                if title:
                    results.append({"title": title, "url": link, "snippet": body})
    except Exception as e:
        logger.warning(f"DDGS search mengalami kendala ({e}), mencoba fallback...")

    # 2. Metode Fallback: Wikipedia Summary API (id.wikipedia lalu en.wikipedia jika kosong)
    if not results:
        for lang in ["id", "en"]:
            try:
                wiki_url = f"https://{lang}.wikipedia.org/w/api.php?action=query&list=search&srsearch={urllib.parse.quote(clean_query)}&format=json"
                r = requests.get(wiki_url, headers={"User-Agent": "cdpk-grok-slack-bot/1.0"}, timeout=6)
                if r.status_code == 200:
                    data = r.json()
                    items = data.get("query", {}).get("search", [])
                    for it in items[:max_results]:
                        title = it.get("title", "")
                        raw_snippet = it.get("snippet", "")
                        clean_snippet = re.sub(r'<[^>]+>', '', raw_snippet).strip()
                        page_url = f"https://{lang}.wikipedia.org/wiki/{urllib.parse.quote(title)}"
                        results.append({"title": title, "url": page_url, "snippet": clean_snippet})
                    if results:
                        break
            except Exception as e:
                logger.warning(f"Wikipedia {lang} fallback search gagal: {e}")

    if not results:
        return f"Tidak ditemukan hasil pencarian web yang relevan untuk query: '{clean_query}'."

    # Format hasil dengan pembatasan token ketat (Token Guard)
    lines = [f"Hasil pencarian web untuk '{clean_query}':\n"]
    for idx, r in enumerate(results[:max_results], 1):
        lines.append(f"{idx}. {r['title']}")
        lines.append(f"   URL: {r['url']}")
        lines.append(f"   Cuplikan: {r['snippet'][:250]}\n")

    output = "\n".join(lines).strip()
    # Pangkas keras maksimal 1.500 karakter untuk melindungi kuota token
    return output[:1500]

def read_web_page_content(url: str, max_chars: int = 1800) -> str:
    """
    Mengunduh dan mengekstrak teks bersih dari sebuah halaman website
    dengan proteksi token guard (maksimal 1.800 karakter / ~350-400 token).
    """
    if not url or not url.startswith(("http://", "https://")):
        return "URL website tidak valid. Pastikan dimulai dengan http:// atau https://"

    logger.info(f"Mengunduh dan membaca halaman web: {url}")
    headers = {
        "User-Agent": "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/122.0.0.0 Safari/537.36",
        "Accept": "text/html,application/xhtml+xml,application/xml;q=0.9,*/*;q=0.8",
        "Accept-Language": "id-ID,id;q=0.9,en-US;q=0.8,en;q=0.7",
    }

    try:
        resp = requests.get(url, headers=headers, timeout=12)
        if resp.status_code != 200:
            return f"Gagal membaca URL (HTTP {resp.status_code}): {url}"

        # Parse HTML menggunakan BeautifulSoup dan eliminasi elemen non-konten
        soup = BeautifulSoup(resp.text, "html.parser")
        for tag in soup(["script", "style", "nav", "footer", "header", "noscript", "aside", "svg", "form"]):
            tag.decompose()

        # Ekstrak judul halaman jika ada
        title = soup.title.string.strip() if soup.title and soup.title.string else ""

        # Bersihkan whitespace berlebih
        raw_text = soup.get_text(separator=" ")
        clean_text = re.sub(r'\s+', ' ', raw_text).strip()

        if not clean_text:
            return f"Halaman web berhasil diakses namun tidak mengandung teks konten yang dapat dibaca: {url}"

        # Format ringkasan dengan pembatasan token guard
        summary_header = f"Konten dari URL ({url})"
        if title:
            summary_header += f" - Judul: '{title}'"

        result = f"{summary_header}:\n{clean_text[:max_chars]}"
        return result

    except requests.exceptions.Timeout:
        return f"Gagal membaca web: Request timeout (website terlalu lambat merespons): {url}"
    except Exception as e:
        logger.warning(f"Gagal mengekstrak web {url}: {e}")
        return f"Terjadi kendala saat membaca halaman web {url}: {str(e)}"

# Definisi Function Calling Tools untuk OpenAI / xAI Grok API
WEB_TOOLS = [
    {
        "type": "function",
        "function": {
            "name": "perform_web_search",
            "description": "Lakukan live web search di internet untuk mendapatkan informasi eksternal terkini, berita, harga pasar, spesifikasi perangkat kompetitor, atau regulasi yang tidak ada di arsip internal CDPK HQ.",
            "parameters": {
                "type": "object",
                "properties": {
                    "query": {
                        "type": "string",
                        "description": "Kata kunci pencarian spesifik (contoh: 'harga motorola slr5000', 'spesifikasi conquest s23', 'regulasi frekuensi kominfo')"
                    }
                },
                "required": ["query"]
            }
        }
    },
    {
        "type": "function",
        "function": {
            "name": "read_web_page_content",
            "description": "Membaca dan mengekstrak ringkasan isi halaman web dari URL tautan (http/https) yang diberikan pengguna di Slack.",
            "parameters": {
                "type": "object",
                "properties": {
                    "url": {
                        "type": "string",
                        "description": "URL lengkap website yang ingin dibaca (contoh: 'https://isafe-mobile.com/...')"
                    }
                },
                "required": ["url"]
            }
        }
    }
]
