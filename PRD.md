# Product Requirement Document (PRD): Grok Slack Bot & Hybrid Knowledge Base untuk CDPK HQ

**Status**: Active / Production Deployed  
**Versi**: 2.1.0  
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
2. **Arsitektur Hybrid Knowledge Base Hemat Biaya**: Menghubungkan materi kerja dari Google Drive kantor ke dalam format Markdown (`.md`) bersih yang diproses secara otomatis oleh **Google Gemini 3.8 Flash** di cloud, menghemat biaya token hingga 80% dan bernilai konversi \$0.
3. **Infrastruktur Mandiri 24/7 Bebas Biaya (\$0 Cloud Ops)**: Berjalan 100% otomatis di cloud (Render + GitHub Actions) tanpa mewajibkan laptop admin menyala.
4. **Keamanan Data Berlapis (Zero-Trust 3-Tier RBAC)**: Memisahkan dokumen ke dalam subfolder kategori akses (`direksi/`, `finance/`, `umum/`) sehingga staf biasa tidak pernah memuat data konfidensial ke dalam memori AI.

---

## 2. Arsitektur Sistem (System Architecture)

Sistem menggunakan prinsip **Separation of Concerns (Pemisahan Tanggung Jawab)** dan beroperasi secara penuh di cloud tanpa ketergantungan perangkat lokal:

```text
┌────────────────────────────────────────────────────────────────────────┐
│ BAGIAN A: CLOUD INGESTION PIPELINE (GitHub Actions + Gemini 3.8 Flash)  │
└────────────────────────────────────────────────────────────────────────┘
 [ Google Drive Kantor ]
 Root ID: 1oF8gzaqV1UUdug08KlkKAPomjHsbRL4q
 (Subfolder & Shortcuts: OPERATIONS, Finance, Direksi, ATEX, Produk, dll)
         │
         ▼ (Pemicu: Cron 02.00 & 12.00 WIB atau @grok update knowledge di Slack)
 [ GitHub Actions Cloud Runner (Ubuntu) ]
         ├── 1. Incremental Change Detection (.sync_manifest.json via modifiedTime)
         ├── 2. Ekstraksi Dokumen (Docs -> Teks, Sheets -> CSV, PDF -> pypdf, Word -> docx)
         ├── 3. Restrukturisasi Dokumen via Google Gemini 3.8 Flash ($0 API)
         │      (Metadata YAML, Summary, Salinan Penuh Tanpa Sensor, FAQ Otomatis, Glosarium)
         ├── 4. Upload Balik ke Google Drive ("Markdown - Knowledge Base" Folder)
         └── 5. Git Commit & Push ke Repositori (knowledge/direksi/, finance/, umum/)

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
            ├─► Memuat knowledge/{direksi,finance,umum}/ sesuai Role penanya
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
| **AI Engine Utama** | `openai` SDK (xAI endpoint) | Terhubung ke `https://api.x.ai/v1` dengan model `grok-2-mini` (default cepat & hemat) atau `grok-2`. |
| **AI Structuring Engine** | Google Gemini 3.8 Flash | Mengonversi dokumen mentah Google Drive ke Markdown resmi secara gratis ($0 via Google AI Studio). |
| **Cloud Hosting** | Render Free Web Service | 750 jam komputasi gratis/bulan (cukup untuk 24/7 sebulan penuh). |
| **Cloud Ingestion Runner**| GitHub Actions | Menjalankan pipeline sinkronisasi otomatis harian dan on-demand tanpa mewajibkan komputer menyala. |
| **Uptime Keeper** | UptimeRobot (Free) | HTTP(s) monitor mem-ping URL render setiap 5 menit agar container tidak tertidur (*anti-sleep*). |
| **Version Control & CI/CD**| GitHub + Render Webhooks | Setiap pembaruan repositori langsung memicu deployment instan. |
| **Knowledge Store** | Markdown Files (`knowledge/`) | Terisolasi per kategori akses (`direksi/`, `finance/`, `umum/`) dan disinkronkan ke Google Drive. |

---

## 4. Mekanisme Hybrid Knowledge Base (Drive to Markdown)

### 4.1 Sumber Data
* **Folder Utama Google Drive**: `https://drive.google.com/drive/folders/1oF8gzaqV1UUdug08KlkKAPomjHsbRL4q`
* Berisi file kebijakan kantor, SOP alur kerja, panduan teknis, dan informasi produk/layanan CDPK HQ.
* **Resolusi Shortcut**: Mendukung shortcut folder (`application/vnd.google-apps.shortcut`) via Google Drive API `shortcutDetails.targetId`. Tidak perlu menduplikasi berkas dari shared drive lain.

### 4.2 Mandat Tugas Gemini 3.8 Flash
Setiap dokumen yang dikonversi wajib mengikuti struktur resmi:
1. **Metadata Header (YAML Frontmatter)**:
   * `sumber_dokumen`: Nama asli file.
   * `gdrive_file_id`: ID unik berkas Google Drive.
   * `gdrive_modified_time`: Timestamp modifikasi terakhir dari Drive.
   * `folder_asal`: Jalur folder Google Drive asal dokumen.
   * `tanggal_ekstraksi`: Tanggal pemrosesan.
   * `tingkat_akses`: Klasifikasi hak akses (`DIREKSI_SAJA`, `FINANCE_DAN_DIREKSI`, `SEMUA_MEMBER`).
2. **Executive Summary**: 3 - 5 poin inti paling penting di bagian atas dokumen.
3. **Salinan Lengkap & Rapi Tanpa Sensor**: Menyalin seluruh teks, angka, rincian gaji, margin, dan tabel tanpa dipotong atau disensor mentah.
4. **FAQ Otomatis Karyawan**: Mengantisipasi 3 - 7 pertanyaan praktis yang paling mungkin ditanyakan oleh tim di Slack.
5. **Glosarium & Rujukan Sumber**: Daftar singkatan/istilah teknis dan pencatatan sumber referensi.

### 4.3 Deteksi Perubahan Berkas (*Incremental Sync*)
* Sistem memelihara berkas pelacak `knowledge/.sync_manifest.json`.
* Sebelum mengunduh atau memanggil Gemini, pipeline membandingkan timestamp `modifiedTime` file di Google Drive dengan manifes.
* Berkas yang tidak berubah otomatis dilewati (`SKIP`), menghemat waktu eksekusi dan kuota token.

### 4.4 Sinkronisasi Dua Arah ke Google Drive
Selain disimpan di repositori Git, seluruh file Markdown hasil konversi otomatis diunggah langsung ke folder Google Drive kantor:
* **Folder Output**: `Markdown - Knowledge Base` (`1pO9k6fKZdBUoIIOiUuYP6ucoUxmkLLrI`)
  * `Khusus Direksi` (`1BL1KFiEGo4f-d2QjOD2TdvqS6i5EG1r5`)
  * `Finance` (`14qwqSdo2v2gZvkehgagvNs6q44hmLm2h`)
  * `Umum` (`1Vjq-nZk22HhcLA6Xu689T9IerdzU82zG`)

---

## 5. Fitur Pengguna di Slack (User Features)

### 5.1 Role-Based Access Control (RBAC) 3-Tier & Hard Data Isolation
Bot memverifikasi identitas pengguna di Slack berdasarkan User ID permanen dan profil email resmi:

| Level Hak Akses | Anggota Terdaftar | Cakupan Dokumen yang Dimuat ke Memori AI | Batasan Keamanan |
| :--- | :--- | :--- | :--- |
| 👑 **DIREKSI** | Gama, Janice, Richard, Adrian | **ALL ACCESS**: Memuat `knowledge/direksi/`, `knowledge/finance/`, dan `knowledge/umum/`. | Memiliki wewenang penuh atas seluruh dokumen dan komando sinkronisasi. |
| 💼 **TIM FINANCE** | Sen sen, Ririn, Villa | Memuat `knowledge/finance/` dan `knowledge/umum/`. | ❌ **HARD BLOCKED**: Berkas dari folder `knowledge/direksi/` sama sekali tidak pernah dimasukkan ke konteks prompt. |
| 👥 **STAF UMUM** | Anggota tim selain Direksi & Finance | HANYA memuat `knowledge/umum/`. | ❌ **HARD BLOCKED**: Berkas dari `finance/` dan `direksi/` tidak pernah dimasukkan ke konteks prompt. |

### 5.2 Pencatatan & Penyebutan Sumber Referensi (Citations)
* Setiap kali Grok menjawab pertanyaan seputar kebijakan, SOP, atau regulasi internal, bot **selalu menyebutkan nama file dokumen sumbernya** (contoh: *"Berdasarkan dokumen SOP FMTCS v2.1..."*).

### 5.3 Channel Terpusat (`#ask-grok`) & Direct Message
* Anggota tim berinteraksi dengan me-mention bot: `@Grok <pertanyaan>` di channel `#ask-grok` (membalas di thread) atau berkonsultasi privat melalui Direct Message (DM 1-on-1).
* **Indikator UX**: Emoji reaksi `thinking_face` otomatis disematkan saat Grok sedang memproses jawaban.

### 5.4 Pemicu Sinkronisasi dari Slack & Jadwal Cloud
1. **Pemicu On-Demand dari Slack**:
   * Perintah: `@grok update knowledge` atau `@grok sync knowledge`.
   * Hanya anggota dengan otoritas **Direksi** yang dapat memicu perintah ini.
   * Bot langsung memicu GitHub Actions di cloud dan mengabari di Slack bahwa proses telah berjalan.
2. **Jadwal Otomatis Harian (Dual Cron)**:
   * **Pukul 02.00 WIB** (`0 19 * * *` UTC)
   * **Pukul 12.00 WIB** (`0 5 * * *` UTC)

---

## 6. Keamanan, Privasi, & Manajemen Rahasia (Security & Governance)

1. **Isolasi Akun Pribadi**:
   * Bot Slack yang dideploy di cloud tidak memiliki akses ke Google Drive pribadi atau Gmail admin.
   * Kredensial Google Drive di cloud menggunakan dedicated session token yang disimpan secara aman di GitHub Secrets (`GDRIVE_CREDENTIALS_JSON`).
2. **Manajemen Kredensial**:
   * Seluruh kredensial (`SLACK_BOT_TOKEN`, `SLACK_APP_TOKEN`, `XAI_API_KEY`, `GITHUB_TOKEN`) disimpan di Environment Variables Render dan dilindungi oleh `.gitignore`.
3. **Budget Guardrail**:
   * Admin menetapkan batas pengeluaran bulanan (*Monthly Spending Limit*) di dashboard xAI console untuk mencegah pembengkakan biaya.

---

## 7. Struktur Repositori

```text
Grok x Slack/
├── .github/
│   └── workflows/
│       └── sync_drive.yml      # GitHub Actions: jadwal 02.00 & 12.00 WIB + workflow_dispatch
├── scripts/
│   └── sync_knowledge.py       # Pipeline: Google Drive -> Gemini 3.8 Flash -> Markdown -> Drive
├── knowledge/                  # Basis pengetahuan tim CDPK HQ (format .md)
│   ├── .sync_manifest.json     # Manifes pelacak perubahan dokumen (incremental sync)
│   ├── README.md               # Dokumentasi arsitektur folder knowledge
│   ├── direksi/                # Dokumen khusus Direksi (gaji, legalitas direksi)
│   ├── finance/                # Dokumen tim Finance & Direksi (LK, SPT, invoicing)
│   └── umum/                   # Dokumen operasional publik (SOP, FMTCS, produk, sales)
├── .env                        # Token lokal (tidak masuk git)
├── .env.example                # Template environment variables
├── .gitignore                  # Mengabaikan .env, venv/, __pycache__/
├── Dockerfile                  # Container cloud Render (non-root UID 1000)
├── Procfile                    # Worker descriptor
├── render.yaml                 # Blueprint deklaratif Render
├── requirements.txt            # Dependensi Python
├── app.py                      # Core bot (Slack Socket Mode + RBAC Loader + Health Server)
├── PRD.md                      # Dokumen PRD resmi ini
└── README.md                   # Dokumentasi umum proyek
```

---

## 8. Panduan Operasional & Pemeliharaan (Runbook)

### 8.1 Menambah Dokumen Baru
1. Letakkan dokumen (atau shortcut folder) di Google Drive kantor:
   `https://drive.google.com/drive/folders/1oF8gzaqV1UUdug08KlkKAPomjHsbRL4q`.
2. Tunggu jadwal otomatis (jam 02.00 atau 12.00 WIB), ATAU ketik `@grok update knowledge` di Slack.
3. Dokumen akan otomatis diekstrak, distrukturkan oleh Gemini 3.8 Flash, diunggah ke folder `Markdown - Knowledge Base` di Google Drive, dan diperbarui di memori Grok.

### 8.2 Menjalankan Perubahan Tanpa Menyalakan Komputer
* Seluruh pipeline pembaruan berjalan 100% di cloud.
* Admin dan tim dapat meninggalkan komputer atau mematikan laptop kapan saja; GitHub Actions dan Render akan menyelesaikan sinkronisasi di latar belakang.
