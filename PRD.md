# Product Requirement Document (PRD): Grok Slack Bot & Hybrid Knowledge Base untuk CDPK HQ

**Status**: Active / Production Deployed  
**Versi**: 2.0.0  
**Target Rilis**: Q4 2026  
**Owner**: Adrian Kansil (CDPK HQ)  
**Repositori**: [tech-sol-id/cdpk-grok-slack-bot](https://github.com/tech-sol-id/cdpk-grok-slack-bot)  
**Live Service**: `https://cdpk-grok-slack-bot.onrender.com`  

---

## 1. Latar Belakang & Tujuan (Background & Objectives)

### 1.1 Latar Belakang
Tim kerja CDPK HQ membutuhkan asisten kecerdasan buatan (AI) yang cerdas, cepat, dan terintegrasi langsung ke dalam alur komunikasi harian di Slack. Sebelumnya, penggunaan AI bersifat individual di browser masing-masing, sehingga:
1. Kolaborasi pemecahan masalah dan diskusi tim tidak terdokumentasi di Slack.
2. AI umum tidak memahami konteks SOP, panduan kerja, dan basis pengetahuan (*knowledge base*) internal CDPK HQ.
3. Memasukkan dokumen mentah (PDF, Word, Google Docs puluhan halaman) langsung ke API model frontier memakan biaya token yang sangat boros dan rawan halusinasi.

### 1.2 Tujuan Utama
1. **Asisten AI Kolektif**: Mengintegrasikan xAI Grok (`grok-2-mini` / `grok-2`) ke dalam workspace Slack CDPK HQ melalui channel resmi `#ask-grok` dan Direct Message.
2. **Arsitektur Hybrid Knowledge Base Hemat Biaya**: Menghubungkan materi kerja dari Google Drive kantor ke dalam format Markdown (`.md`) bersih yang dikurasi secara lokal sebelum diunggah ke cloud, menghemat biaya token hingga 80% dan bernilai konversi \$0.
3. **Infrastruktur Mandiri 24/7 Bebas Biaya (\$0 Cloud Ops)**: Berjalan secara otomatis di cloud tanpa mewajibkan laptop admin menyala.

---

## 2. Arsitektur Sistem (System Architecture)

Sistem menggunakan prinsip **Separation of Concerns (Pemisahan Tanggung Jawab)** antara pipeline konversi dokumen dan runtime bot di Slack:

```
┌────────────────────────────────────────────────────────────────────────┐
│ BAGIAN A: LOCAL KNOWLEDGE INGESTION PIPELINE (Offline / Admin Laptop)  │
└────────────────────────────────────────────────────────────────────────┘
 [ Google Drive Kantor ]
 Folder ID: 1oF8gzaqV1UUdug08KlkKAPomjHsbRL4q
 (Format mentah: Docs, PDF, Word, Spreadsheet)
         │
         ▼ (Konversi Lokal: Script / Antigravity Agent - Biaya: $0)
 [ Pembersihan & Ekstraksi Teks ]
 - Menghilangkan metadata sampah & format biner
 - Sensor data sensitif (Human-in-the-Loop)
 - Format ulang menjadi Markdown bersih & terstruktur
         │
         ▼
 [ Direktori knowledge/*.md ] di Repo Git Lokal
         │
         ▼ (git push)
 [ GitHub: tech-sol-id/cdpk-grok-slack-bot ]

──────────────────────────────────────────────────────────────────────────

┌────────────────────────────────────────────────────────────────────────┐
│ BAGIAN B: CLOUD SLACK BOT ENGINE (24/7 Online di Render Cloud)         │
└────────────────────────────────────────────────────────────────────────┘
 [ GitHub Commit Trigger ]
         │ (Render Auto-deploy ~30 detik)
         ▼
 [ Docker Container di Render (Region: Singapore) ]
    ├── Port 7860: Mini HTTP Server (Health Check) <─── [ UptimeRobot ]
    └── Background Thread: Slack Bolt (Socket Mode)      (Ping tiap 5 menit)
            │
            ├─► Memuat knowledge/*.md ke memori
            ├─► Terhubung Outbound WebSocket ke Slack CDPK HQ
            │
            ▼ (Member mention di #ask-grok atau kirim DM)
 [ Slack CDPK HQ ] ◄── (Jawaban cerdas berbasis SOP CDPK) ──► [ xAI Grok API ]
```

---

## 3. Komponen Arsitektur & Stack Teknologi

| Komponen | Teknologi | Keterangan & Rationale |
| :--- | :--- | :--- |
| **Runtime & Language** | Python 3.11 / Docker | Ringan, kompatibel dengan container cloud modern. |
| **Slack Framework** | `slack-bolt`, `slack-sdk` | Menggunakan **Socket Mode** via WebSocket outbound; tidak butuh IP publik, webhook, atau domain berbayar. |
| **AI Engine** | `openai` SDK (xAI endpoint) | Terhubung ke `https://api.x.ai/v1` dengan model `grok-2-mini` (default cepat & hemat) atau `grok-2`. |
| **Cloud Hosting** | Render Free Web Service | 750 jam komputasi gratis/bulan (cukup untuk 24/7 sebulan penuh). |
| **Uptime Keeper** | UptimeRobot (Free) | HTTP(s) monitor mem-ping URL render setiap 5 menit agar container tidak tertidur (*anti-sleep*). |
| **Version Control & CI/CD** | GitHub + Render Webhooks | Setiap `git push` ke branch `main` langsung memicu auto-deploy instan. |
| **Knowledge Store** | Local Markdown Files (`knowledge/`) | Dokumen teks murni, minim token, mudah ditinjau sebelum dideploy. |

---

## 4. Mekanisme Hybrid Knowledge Base (Drive to Markdown)

### 4.1 Sumber Data
* **Folder Google Drive**: `https://drive.google.com/drive/folders/1oF8gzaqV1UUdug08KlkKAPomjHsbRL4q`
* Berisi file kebijakan kantor, SOP alur kerja, panduan teknis, dan informasi produk/layanan CDPK HQ.

### 4.2 Alur Transformasi ke Markdown & Mandat Gemini
1. **Pengambilan Dokumen & Resolusi Google Drive Shortcuts**:
   * Sistem mendukung file langsung maupun **Shortcut Folder** (`application/vnd.google-apps.shortcut`) via Google Drive API `shortcutDetails.targetId`.
   * Tidak perlu menduplikasi atau meng-copy file dari shared folder lain; cukup buat shortcut di folder utama, dan pipeline akan menelusuri ke folder target aslinya.
2. **Mandat Tugas Gemini 3.8 Flash**:
   * **Salinan Lengkap**: Menyalin seluruh isi teks, tabel, dan klausul dokumen tanpa memangkas fakta penting atau melakukan auto-sensor pada data angka/spesifik.
   * **Executive Summary**: Menghasilkan 3 - 5 poin inti paling penting di bagian atas dokumen.
   * **Struktur Dokumen Rapi**: Memformat dokumen ke hierarki Markdown standar (`#`, `##`, `-`, dan tabel).
   * **FAQ Otomatis Karyawan**: Mengantisipasi 3 - 7 pertanyaan praktis yang paling sering ditanyakan oleh anggota tim di Slack.
   * **Metadata Sumber (Citation)**: Menyematkan frontmatter YAML (`sumber_dokumen`, `folder_asal`, `tanggal_ekstraksi`).
3. **Distribusi & Deploy**:
   * File `.md` di-commit ke repositori GitHub.
   * Render secara otomatis memperbarui bot dalam ~30 detik tanpa downtime.

### 4.3 Mengapa Strategi Ini Menghemat Biaya?
* **Zero Processing Cost**: Pemrosesan dokumen tebal tidak menggunakan token xAI API berbayar, melainkan ditangani oleh Google Gemini Flash Free Tier ($0).
* **Token Efficiency**: File Markdown 60–80% lebih ringkas dibandingkan teks mentah dari PDF/Word.
* **Peningkatan Akurasi**: Grok secara alami sangat cerdas dalam memahami konteks berstruktur Markdown, mencegah halusinasi.

---

## 5. Fitur Pengguna di Slack (User Features)

### 5.1 Role-Based Access Control (RBAC) Cerdas
Bot membedakan profil dan hak akses penanya berdasarkan akun Slack (`user_id`, email, dan title profil):
* **Hak Akses Tinggi (Direksi & Finance Manager)**:
  * Diizinkan mengakses seluruh informasi konfidensial, nominal keuangan, kompensasi, dan data manajerial jika ditanyakan.
* **Hak Akses Standar (Karyawan & Tim Umum)**:
  * Dilindungi aturan privasi ketat: Grok secara otomatis menolak dan membatasi pembagian nominal gaji individu atau rahasia finansial pribadi karyawan lain, serta mengarahkan penanya ke Direksi/Finance secara resmi.

### 5.2 Pencatatan & Penyebutan Sumber Referensi (Citations)
* Setiap kali Grok menjawab pertanyaan seputar kebijakan, SOP, atau regulasi internal, bot **selalu menyebutkan nama file dokumen sumbernya** (berdasarkan metadata header dokumen) agar tim mengetahui dasar rujukan resminya.

### 5.3 Channel Terpusat (`#ask-grok`) & Direct Message
* Anggota tim berinteraksi dengan me-mention bot: `@Grok <pertanyaan>` di channel `#ask-grok` (membalas di thread) atau berkonsultasi privat melalui Direct Message (DM 1-on-1).
* **Indikator UX**: Emoji reaksi `thinking_face` otomatis disematkan saat Grok sedang memproses jawaban.

---

## 6. Keamanan, Privasi, & Manajemen Rahasia (Security & Governance)

1. **Isolasi Akun Pribadi**:
   * Bot Slack yang dideploy di cloud **tidak memiliki akses** ke Google Drive pribadi, email Gmail, kalender, maupun file lokal admin.
   * Bot hanya membaca file yang secara eksplisit sudah dikonversi ke folder `knowledge/` di repositori.
2. **Manajemen Kredensial**:
   * Seluruh kredensial (`SLACK_BOT_TOKEN`, `SLACK_APP_TOKEN`, `XAI_API_KEY`) disimpan di *Environment Variables* Render dan dilindungi oleh `.gitignore`.
3. **Budget Guardrail**:
   * Admin menetapkan batas pengeluaran bulanan (*Monthly Spending Limit*) di dashboard xAI console untuk mencegah pembengkakan biaya.

---

## 7. Struktur Repositori

```text
Grok x Slack/
├── .env                  # Token lokal (tidak masuk git)
├── .env.example          # Panduan template environment variable
├── .gitignore            # Mengabaikan .env, venv/, __pycache__/
├── Dockerfile            # Konfigurasi container cloud (non-root UID 1000)
├── Procfile              # Worker descriptor
├── render.yaml           # Blueprint deklaratif Render
├── requirements.txt      # Dependensi Python (slack-bolt, openai, dll)
├── app.py                # Aplikasi utama (Slack Socket Mode + Health Server)
├── PRD.md                # Dokumen PRD resmi (dokumen ini)
├── README.md             # Dokumentasi umum proyek
└── knowledge/            # Basis pengetahuan tim CDPK HQ (format .md)
    ├── README.md         # Panduan kontribusi knowledge
    └── cdpk_overview.md  # Ringkasan profil & aturan kerja CDPK HQ
```

---

## 8. Panduan Operasional & Pemeliharaan (Runbook)

### 8.1 Menambah / Memperbarui Dokumen Pengetahuan
1. Taruh dokumen baru di folder Google Drive kantor.
2. Minta Antigravity Agent untuk mengonversi dokumen tersebut ke format `.md` di folder `knowledge/`.
3. Jalankan `git add knowledge/ && git commit -m "Update knowledge: <nama-dokumen>" && git push origin main`.
4. Render akan otomatis melakukan build dan deploy versi terbaru.

### 8.2 Mengganti Model AI
* Buka Dashboard Render -> Environment Variables -> ubah `XAI_MODEL`:
  * `grok-2-mini` : Untuk kecepatan tinggi dan biaya sangat murah (rekomendasi harian).
  * `grok-2` : Untuk penalaran mendalam dan analisis logika kompleks.
