# Product Requirement Document (PRD): Grok Slack Bot untuk CDPK HQ

## 1. Ringkasan Eksekutif (Executive Summary)
Proyek ini bertujuan mengintegrasikan kecerdasan buatan Grok (melalui xAI API) ke dalam workspace Slack **CDPK HQ**. Bot ini akan berperan sebagai asisten AI cerdas terpusat yang dapat diakses oleh seluruh anggota tim CDPK HQ melalui mention di channel maupun pesan langsung (Direct Message / DM).

---

## 2. Masalah & Solusi
* **Masalah:** Langganan Grok/X Premium bersifat personal untuk satu akun pengguna dan tidak bisa dibagikan langsung ke workspace Slack tim.
* **Solusi:** Membangun *Custom Slack App* berbasis **Socket Mode** yang terhubung ke **xAI API (Grok)**, memungkinkan seluruh anggota tim berkolaborasi dengan AI menggunakan satu akun organisasi yang terkelola.

---

## 3. Arsitektur Teknis

### 3.1 Komponen Sistem
```
[Slack User (CDPK HQ)]
       │
       ▼ (Mention / DM)
[Slack Socket Mode Connection] (Websocket aman, tanpa butuh IP publik / ngrok)
       │
       ▼
[Slack Bolt Python App]
       │
       ▼ (HTTP REST call)
[xAI API Endpoint (https://api.x.ai/v1)]
       │
       ▼ (Response text)
[Slack Bolt Python App]
       │
       ▼ (Reply di thread / DM)
[Slack User (CDPK HQ)]
```

### 3.2 Stack Teknologi
* **Bahasa & Framework:** Python 3.10+ / `slack-bolt` (menggunakan `SocketModeHandler`)
* **AI Client:** `openai` SDK (dikonfigurasi dengan `base_url="https://api.x.ai/v1"`)
* **Model AI:** `grok-2` (untuk penalaran kompleks) atau `grok-2-mini` (untuk respons cepat & hemat token)
* **Manajemen Environment:** `python-dotenv`

---

## 4. Fitur Utama (Core Features)

1. **Mention di Channel (`@Grok AI`):**
   * Bot merespons pertanyaan di public/private channel.
   * **Thread Reply:** Bot otomatis membalas di dalam *thread* agar tidak mengotori channel utama.
   * **Context Awareness:** Bot membaca riwayat pesan dalam thread untuk menjaga konteks percakapan multi-turn.
2. **Direct Message (DM):**
   * Member dapat berkonsultasi secara privat dengan bot via DM 1-on-1.
3. **Indikator Proses (UX):**
   * Menampilkan reaksi emoji atau status pengetikan (*typing indicator*) saat Grok sedang memproses jawaban.
4. **Error Handling & Rate Limiting:**
   * Penanganan gracefully saat kuota token habis atau xAI API mengalami timeout.
   * Format pesan panjang otomatis dipecah agar sesuai batas karakter Slack (4.000 karakter per pesan).

---

## 5. Konfigurasi Lingkungan (Environment Variables)

File `.env` akan menyimpan:
```bash
# Slack Credentials
SLACK_BOT_TOKEN=xoxb-...
SLACK_APP_TOKEN=xapp-...

# xAI Credentials
XAI_API_KEY=xai-...
XAI_MODEL=grok-2-mini
DEFAULT_SYSTEM_PROMPT="Anda adalah asisten AI resmi CDPK HQ yang didukung oleh Grok. Jawab dengan cerdas, ramah, dan profesional."
```

---

## 6. Rencana Peluncuran (Deployment Plan)

* **Fase 1 (Lokal / Development):** Menjalankan bot di mesin lokal menggunakan Socket Mode untuk memverifikasi fungsionalitas dan otentikasi.
* **Fase 2 (Git & Versioning):** Inisialisasi Git repository untuk pelacakan kode dan kemudahan deployment.
* **Fase 3 (Production Deployment):** 
  * Opsi A: Berjalan sebagai `systemd service` atau `pm2 / tmux` di server/PC kantor yang selalu aktif.
  * Opsi B: Dideploy dalam bentuk container Docker ke serverless cloud (Google Cloud Run / Render / VPS).
