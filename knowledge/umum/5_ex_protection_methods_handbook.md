---
sumber_dokumen: "5_Ex_Protection_Methods_Handbook.pdf"
gdrive_file_id: "1s7Ytc-w5R67xiqduF7nXMnWHI8SnGDe1"
gdrive_modified_time: "2026-07-21T15:41:22.000Z"
folder_asal: "Root Knowledge / ATEX & Ex Knowledge"
tanggal_ekstraksi: "2026-10-15"
tingkat_akses: "SEMUA_MEMBER"
---

# Handbook ATEX, Ex, HazLoc - Part V: Metode Proteksi

> **Panduan Teknis & Arsitektur Keselamatan untuk Engineer, HSE, Operasi, dan Pemeliharaan**  
> **Editor:** Adrian Bany Kansil  
> **Edisi:** 2.3 — 2026  
> *FOR INTERNAL USE ONLY*

---

## 📌 Executive Summary

1. **Tiga Prinsip Pokok Rekayasa Proteksi Ledakan (IEC 60079):** Seluruh metode proteksi peralatan di atmosfer eksplosif berakar pada tiga pilar utama pemutus segitiga ledakan: **Mengurung/Menahan Ledakan** (*Ex d*), **Memisahkan Sumber Penyalaan** (*Ex p, Ex o, Ex q, Ex m, Ex e, Ex n*), dan **Membatasi Energi** (*Ex i*).
2. **Kesesuaian Hierarki Zona & EPL:** Zona 0 mewajibkan perlindungan dengan redundansi ganda dan toleransi terhadap 2 kesalahan (*Ex ia*, *Ex ma*). Zona 1 mengizinkan proteksi seperti *Ex d*, *Ex pxb/pyb*, *Ex eb*, *Ex ib*, *Ex mb*, *Ex o*, dan *Ex q*. Zona 2 membuka ruang efisiensi desain dan opsi ekonomis seperti *Ex ec*, *Ex dc*, *Ex ic*, *Ex nR*, dan *Ex pzc*. Perangkat diizinkan turun zona (misal: *Ex ia* dipasang di Zona 1/2), namun **dilarang keras naik zona**.
3. **Integritas Fisik Metode Kurungan (Ex d):** Selungkup *flameproof* dirancang menahan tekanan ledakan internal hingga ~10 bar dan mendinginkan gas yang keluar via *flame path*. Goresan flens, penambahan cat tebal pada celah sambungan, atau baut yang kendor akan menghilangkan proteksi total secara instan.
4. **Keistimewaan Intrinsic Safety (Ex i) & Entity Parameters:** *Ex i* adalah metode utama yang aman untuk pekerjaan pemeliharaan langsung (*live maintenance*) tanpa *hot work permit*. Keamanan loop bergantung pada verifikasi 5 Aturan Emas *Entity Parameters* ($U_o \le U_i$, $I_o \le I_i$, $P_o \le P_i$, $L_o \ge L_i + L_c$, $C_o \ge C_i + C_c$), di mana kapasitas kabel ($C_c$) dan induktansi kabel ($L_c$) wajib diperhitungkan secara presisi.
5. **Kepatuhan Disiplin Sistem & Standar Terbaru:** Evolusi standar IEC 60079 memindahkan sebagian besar sub-tipe *Ex n* ke standar spesifik (*Ex nA* menjadi *Ex ec*, *Ex nC* menjadi *Ex dc*, *Ex nL* menjadi *Ex ic*). Setiap perubahan instrumen atau kabel di lapangan wajib tunduk pada prosedur *Management of Change* (MOC) dan dokumentasi loop sesuai standar IEC 60079-25.

---

## 📖 Salinan Lengkap & Terstruktur

### 1. Tiga Strategi Dasar Memutus Segitiga Ledakan

Seluruh metode proteksi berbasis standar IEC 60079 berakar pada salah satu dari tiga prinsip rekayasa keselamatan berikut:

```
                          ┌───────────────────────────────────────────────┐
                          │   TIGA STRATEGI DASAR MEMUTUS SEGITIGA        │
                          │                 LEDAKAN                       │
                          └──────────────────────┬────────────────────────┘
                                                 │
         ┌───────────────────────────────────────┼───────────────────────────────────────┐
         │                                       │                                       │
         ▼                                       ▼                                       ▼
┌─────────────────────────────────┐   ┌─────────────────────────────────┐   ┌─────────────────────────────────┐
│       MENGURUNG / MENAHAN       │   │        MEMISAHKAN SUMBER        │   │        MEMBATASI ENERGI         │
│             LEDAKAN             │   │            PENYALAAN            │   │                                 │
├─────────────────────────────────┤   ├─────────────────────────────────┤   ├─────────────────────────────────┤
│ Ledakan boleh terjadi di dalam, │   │ Bagian panas/percikan           │   │ Energi listrik & termal dijaga  │
│ tapi tidak menyebar keluar.     │   │ dipisahkan dari atmosfer        │   │ di bawah ambang batas           │
│                                 │   │ eksplosif.                      │   │ penyalaan.                      │
├─────────────────────────────────┤   ├─────────────────────────────────┤   ├─────────────────────────────────┤
│ • Ex d (Flameproof)             │   │ • Ex p, Ex o, Ex q, Ex m,       │   │ • Ex i (Intrinsic Safety)       │
│                                 │   │   Ex e, Ex n                    │   │                                 │
└─────────────────────────────────┘   └─────────────────────────────────┘   └─────────────────────────────────┘
```

---

### 2. Peta Induk Metode Proteksi (Gas Group II)

Tabel berikut merangkum seluruh metode proteksi untuk kelompok gas industri (Group II):

| Kode | Prinsip Dasar | Standar (IEC) | EPL & Zona (Gas) |
| :--- | :--- | :--- | :--- |
| **Ex d** | Mengurung ledakan internal | IEC 60079-1 | Gb / Zona 1, 2 |
| **Ex p** | Tekanan lebih gas pelindung | IEC 60079-2 | Gb, Gc / Zona 1, 2 |
| **Ex o, q, m** | Isolasi minyak, serbuk, resin | IEC 60079-6, -5, -18 | Ga, Gb, Gc / Zona 0*, 1, 2 (*Zona 0 hanya untuk Ex ma) |
| **Ex e** | Margin ekstra cegah percikan | IEC 60079-7 | Gb, Gc / Zona 1, 2 |
| **Ex n** | Energi terbatas / *Non-sparking* | IEC 60079-15 | Gc / Zona 2 |
| **Ex i** | Membatasi energi di bawah ambang | IEC 60079-11 | Ga, Gb, Gc / Zona 0, 1, 2 |

> **ATURAN EMAS PEMILIHAN ZONA:**  
> - **Zona 0:** Sangat ketat (utamanya menggunakan *Ex ia* / *Ex ma*).  
> - **Zona 1:** Menawarkan banyak opsi metode proteksi (*Ex d, Ex p, Ex e, Ex ib, Ex mb, Ex o, Ex q*).  
> - **Zona 2:** Memiliki pilihan terluas, termasuk perangkat yang sangat ekonomis (*Ex n / Ex ic / Ex ec*).

---

### 3. Ex d (Flameproof): Mengurung Ledakan Internal

Metode *Ex d* mengizinkan gas eksplosif masuk ke dalam selungkup dan terbakar, namun selungkup dirancang cukup kuat menahan ledakan dan memadamkan apinya sebelum mencapai atmosfer luar.

#### Mekanisme Kerja
- **Kekuatan Struktural:** Mampu menahan tekanan ledakan internal ekstrem (mencapai $\sim 10\text{ bar}$).
- **Flame Path (Jalur Api):** Celah panjang dan sempit yang dirancang secara mekanis presisi untuk mendinginkan gas hasil pembakaran saat merambat keluar hingga suhunya turun di bawah titik nyala gas luar.

#### Spesifikasi dan Aplikasi
- **Zona Penggunaan:** Zona 1 & 2 (EPL Gb).
- **Aplikasi Tipikal:** Motor listrik berdaya besar, *switchgear*, panel distribusi, pemanas industri (*heaters*).

```
          ┌─────────────────────────────────────────────────────────────┐
          │                    Tutup Selungkup Baja                     │
          └───┬─────────────────────────────────────────────────────┬───┘
              │  Baut Pengencang                       Baut Pengencang  │
    Flame Path│===                                               ===│Flame Path
   (Celah     │                                                     │(Celah
   Sempit)    └───┬─────────────────────────────────────────────┬───┘Sempit)
                  │                                             │
                  │              LEDAKAN INTERNAL               │
                  │                  TERTAHAN                   │
                  │         (Menahan tekanan ~10 bar)           │
                  │                                             │
                  └─────────────────────────────────────────────┘
```

> ⚠️ **PERINGATAN PEMELIHARAAN LAPANGAN:**  
> Integritas celah api (*flame path*) bersifat mutlak! Menambahkan cat tebal pada permukaan flens sambungan, timbulnya goresan/baret mekanis, baut pengikat kurang kencang/kurang lengkap, atau adanya karat/korosi = **Proteksi Hilang Total!**

---

### 4. Ex p (Pressurization): Barikade Tekanan Lebih

Prinsip *Ex p* bekerja dengan cara menahan atmosfer luar agar tidak dapat masuk ke dalam selungkup dengan menjaga tekanan internal selungkup tetap lebih tinggi dibandingkan tekanan atmosfer di sekitarnya (+50 Pa di atas lingkungan luar). Udara bersih atau gas *inert* (misal: Nitrogen) ditiupkan secara terus-menerus ke dalam unit.

```
       Udara/Inert Bersih ───► ┌───────────────────────────────────┐
                               │       Selungkup Bertekanan        │
                               │   (+50 Pa di atas lingkungan)     ├───► Kebocoran Terkontrol ke Luar
                               │                                   │     (Atmosfer eksplosif tercegah masuk)
                               │  ┌─────────────────────────────┐  │
                               │  │      Peralatan Listrik      │  │
                               │  │   (Tak Tersertifikasi Ex)   │  │
                               │  └─────────────────────────────┘  │
                               └───────────────────────────────────┘
```

#### Tiga Langkah Operasional
1. **Purging:** Membilas gas sisa di dalam selungkup dengan beberapa kali kelipatan volume selungkup sebelum sistem dienergisasikan.
2. **Pressurization:** Menjaga tekanan lebih (*overpressure*) secara konstan terhadap atmosfer luar.
3. **Monitoring:** Sistem proteksi dan sensor alarm otomatis yang akan memutus suplai daya secara aman seketika jika tekanan mengalami *drop* (penurunan).

#### Tingkat Proteksi Tekanan (EPL)
| Tipe Proteksi | Tekanan Lebih Minimum | Kesesuaian Penggunaan |
| :--- | :--- | :--- |
| **pxb / pyb** | Minimum $50\text{ Pa}$ | Untuk Zona 1 |
| **pzc** | Minimum $25\text{ Pa}$ | Untuk Zona 2 |

- **Aplikasi:** Ruang analyzer (*analyzer shelter/house*), panel kontrol berukuran besar.
- **Kelemahan Operasional:** Membutuhkan suplai gas pelindung yang konstan dan infrastruktur perpipaan udara/gas tekan yang handal.

---

### 5. Isolasi Fisik: Minyak, Serbuk, dan Enkapsulasi

Metode-metode ini mengisolasi komponen listrik yang berpotensi memercik atau panas dari kontak langsung dengan atmosfer eksplosif di sekitarnya menggunakan medium pengisi.

```
┌─────────────────────────┐    ┌─────────────────────────┐    ┌─────────────────────────┐
│   Ex o (Oil Immersion)  │    │   Ex q (Powder Filling) │    │   Ex m (Encapsulation)  │
├─────────────────────────┤    ├─────────────────────────┤    ├─────────────────────────┤
│ Bagian busur/percikan   │    │ Komponen dikubur dalam  │    │ Komponen dibungkus      │
│ direndam dalam minyak   │    │ pasir kuarsa halus      │    │ total oleh resin/       │
│ pelindung khusus.       │    │ untuk redam percikan.   │    │ compound padat.         │
├─────────────────────────┤    ├─────────────────────────┤    ├─────────────────────────┤
│ Titik Kritis:           │    │ Titik Kritis:           │    │ Titik Kritis:           │
│ Pantau level dan        │    │ Integritas volume,      │    │ Batas suhu permukaan    │
│ kualitas dielektrik     │    │ harus padat dan bebas   │    │ & keutuhan compound     │
│ minyak secara berkala.  │    │ dari rongga udara.      │    │ dari keretakan.         │
├─────────────────────────┤    ├─────────────────────────┤    ├─────────────────────────┤
│ Zona 1 & 2              │    │ Zona 1 & 2              │    │ Zona 0 (ma), 1 (mb),    │
│                         │    │                         │    │ 2 (mc)                  │
└─────────────────────────┘    └─────────────────────────┘    └─────────────────────────┘
```

---

### 6. Ex e (Increased Safety): Margin Ekstra Tanpa Kurungan

Prinsip *Ex e* diterapkan secara eksklusif pada peralatan yang dalam kondisi operasional normal **tidak menghasilkan busur api atau percikan** (*non-sparking*). Keamanan dicapai dengan memperbesar faktor keselamatan mekanis dan elektris:

#### Peningkatan Desain Utama (Key Design Upgrades)
- **Jarak Clearance & Creepage:** Jarak bebas rambatan lewat udara (*clearance*) dan jarak rambat sepanjang permukaan isolator (*creepage*) diperbesar secara signifikan.
- **Terminal Anti-Kendur:** Desain klem terminal mekanis khusus yang mengunci secara positif untuk menolak risiko timbulnya percikan akibat koneksi yang melonggar seiring waktu.
- **Batas Pemanasan Ketat:** Pembatasan kenaikan suhu yang sangat ketat (perhitungan nilai waktu kritis $t_E$ pada proteksi motor listrik saat kondisi rotor terkunci).

#### Catatan Evolusi Standar (IEC 60079-7 Edisi 5)
- **Ex eb (Zona 1):** Kategori keamanan tinggi; tidak mengizinkan penggunaan komponen semikonduktor dan kapasitor elektrolit di dalamnya.
- **Ex ec (Zona 2):** Kategori peningkatan keamanan umum; mengizinkan penggunaan sirkuit semikonduktor. Kode ini resmi menggantikan penamaan kode standar lama **Ex nA**.

---

### 7. Ex n: Proteksi Khusus & Ekonomis untuk Zona 2

Metode *Ex n* (IEC 60079-15) dirancang khusus untuk area Zona 2 (di mana atmosfer gas eksplosif sangat jarang terjadi dan hanya berlangsung dalam durasi singkat). Metode ini memiliki kriteria pengujian yang lebih ringan dan biaya implementasi yang jauh lebih ekonomis. **TIDAK diizinkan untuk digunakan di Zona 0 maupun Zona 1.**

#### Evolusi Standar Ex n (IEC 60079-15)

| Standar Lama (IEC 60079-15 Ed. 4 atau sebelumnya) | Standar Terkini (Harmonisasi / Mutasi Standar) | Standar Rujukan Baru |
| :--- | :--- | :--- |
| **Ex nA** (*Non-sparking*) | Diubah menjadi **Ex ec** | IEC 60079-7 (*Increased Safety*) |
| **Ex nC** (*Enclosed Break*) | Diubah menjadi **Ex dc** | IEC 60079-1 (*Flameproof*) |
| **Ex nL** (*Energy-limited*) | Diubah menjadi **Ex ic** | IEC 60079-11 (*Intrinsic Safety*) |

#### Klasifikasi yang Masih Berlaku di IEC 60079-15 (Edisi 5)
- **nC:** Peralatan dengan komponen tersegel rapat secara permanen (*sealed / hermetically sealed device*).
- **nR:** Selungkup dengan pembatasan pernapasan udara luar (*restricted breathing enclosure*).

> 💡 **Pesan Procurement:** Selalu verifikasi kode proteksi pada lembar sertifikat (*certificate of conformity*) berdasarkan rujukan standar edisi terbaru sebelum melakukan pembelian!

---

### 8. Intrinsic Safety (Ex i): Membatasi Energi di Sumbernya

Metode *Intrinsic Safety* (Keamanan Intrinsik) bekerja secara fundamental dengan membatasi energi listrik dan termal ke tingkat yang jauh di bawah energi minimum penyalaan (*Minimum Ignition Energy* / MIE) dari campuran gas di sekitarnya.

- **Status Proteksi:** Disebut sebagai **"Raja Zona 0"** (EPL Ga).
- **Pemeliharaan:** Satu-satunya metode yang aman dikerjakan dalam kondisi bertegangan/hidup (*Live Maintenance*) tanpa memerlukan izin kerja panas (*hot work permit*).
- **Peruntukan:** Khusus untuk instrumentasi dan sistem sinyal arus lemah.

```
       SAFE AREA                                          HAZARDOUS AREA
    (Non-Hazardous)                                        (Zona 0, 1, 2)
  ┌─────────────────┐             IS BARRIER            ┌──────────────────┐
  │                 │    ┌──────────────────────────┐   │                  │
  │  Sistem Kontrol │───►│  Energi Liar (V, I, P)   ├──►│  Energi Terbatas │
  │   (PLC / DCS)   │    │          Ditekan         │   │   (Aman di Haz)  │
  └─────────────────┘    └─────────────┬────────────┘   └──────────────────┘
                                       │
                                   IS Earth
```

#### Parameter yang Dibatasi oleh IS Barrier
- **Tegangan ($V$):** Dijepit (*clamped*) oleh Dioda Zener agar tidak melampaui nilai ambang batas breakdown.
- **Arus ($I$):** Dibatasi secara fisik menggunakan Resistor pembatas arus.
- **Daya ($P$):** Dibatasi untuk mengendalikan efek kenaikan suhu termal pada permukaan komponen.
- **Induktansi ($L$):** Pembatasan energi medan magnet yang tersimpan pada kumparan/kabel:  
  $$E_L = \frac{1}{2} L \cdot I^2$$
- **Kapasitansi ($C$):** Pembatasan energi medan listrik yang tersimpan pada kapasitor/kabel:  
  $$E_C = \frac{1}{2} C \cdot V^2$$

---

### 9. Level Ex i: Toleransi Gangguan dan Hierarki Zona

Standar IEC 60079-11 membagi metode Keamanan Intrinsik ke dalam 3 tingkatan keandalan berdasarkan ketahanan terhadap kegagalan komponen (*fault tolerance*):

| Level Proteksi | Kriteria Keamanan Sirkuit | Zona yang Diizinkan (EPL) |
| :--- | :--- | :--- |
| **Ex ia** | Tetap aman pada kondisi **operasi normal + 2 gangguan simultan (2 fault)** | Zona 0, Zona 1, Zona 2 (EPL Ga) |
| **Ex ib** | Tetap aman pada kondisi **operasi normal + 1 gangguan (1 fault)** | Zona 1, Zona 2 (EPL Gb) |
| **Ex ic** | Tetap aman pada kondisi **operasi normal saja (0 fault)** | Zona 2 (EPL Gc) |

> **KESIMPULAN:**  
> Semakin tinggi kriteria toleransi gangguan ($ia > ib > ic$), semakin tinggi redundansi komponen internal proteksi (misalnya penggunaan 3 dioda Zener paralel untuk *ia* vs 2 untuk *ib*), sehingga keandalan sistem meningkat dan instrumen diizinkan beroperasi di zona yang paling berbahaya.

---

### 10. Di Balik Layar Ex i: Margin Ekstrem & Aturan Derating

Untuk menjamin keselamatan absolut, perancangan sirkuit *Ex i* menerapkan faktor keselamatan yang sangat ketat:

1. **Faktor Keamanan Percikan 1,5x:**
   - Untuk sirkuit *Ex ia* dan *Ex ib*, batas kurva penyalaan diuji dengan margin pengali $1,5\times$ dari kondisi gangguan terburuk.
   - *Catatan:* Tingkat *Ex ic* dan evaluasi batas suhu permukaan menggunakan faktor keamanan $1,0$.
2. **Aturan Derating Komponen Internal Dua Pertiga (2/3 Rule):**
   - Komponen proteksi utama (seperti *Ceramic Resistor* dan *Zener Diode*) dilarang keras beroperasi melebihi beban **$67\%$ ($2/3$)** dari rating nominal pabrikannya (baik untuk parameter Tegangan, Arus, maupun Daya), bahkan saat terjadi kondisi gangguan terburuk.

> 🛑 **PERINGATAN PENTING UNTUK TEKNISI:**  
> **JANGAN PERNAH MENERAPKAN ULANG FAKTOR KEAMANAN INI SECARA MANDIRI!**  
> Parameter entitas tersertifikasi (*Entity Parameters*) yang tercetak pada sertifikat produk **SUDAH** memperhitungkan semua margin keselamatan ini. Teknisi di lapangan wajib memverifikasi kecocokan sistem menggunakan angka sertifikat apa adanya.

---

### 11. Entity Parameters: Bahasa Pencocokan Loop IS

Agar sebuah sirkuit *IS* terjamin keselamatannya, parameter entitas pada peralatan pencatu daya di *Safe Area* (*Associated Apparatus* / Barrier) harus cocok dengan peralatan instrumen di *Hazardous Area* (*Intrinsically Safe Apparatus* / Sensor / Transmitter) beserta kabel penghubungnya.

```
       SAFE AREA                 │               HAZARDOUS AREA (Zona 0/1/2)
    (Non-hazardous)              │
                                 │
┌──────────────────────┐         │          IS Cable (Lc, Cc)         ┌─────────────────────┐
│    Sistem Kontrol    │         │       ════════════════════         │ Perangkat Lapangan  │
│      (PLC / DCS)     │         │                                    │         IS          │
└──────────┬───────────┘         │                                    │ (Transmitter/Sensor)│
           │                     │                                    └──────────┬──────────┘
┌──────────▼───────────┐         │                                               │
│    Zener / Galvanic  ├─────────┴───────────────────────────────────────────────┘
│       Barrier        │  Parameter Output Barrier: Uo, Io, Po, Lo, Co
└──────────┬───────────┘  Parameter Kabel: Lc, Cc
           │              Parameter Input Instrumen: Ui, Ii, Pi, Li, Ci
       IS Earth
```

#### 5 Aturan Emas Pencocokan (Wajib Terpenuhi Semua):

$$1.\quad U_o \le U_i \quad \text{(Tegangan maksimum sumber tidak melampaui tegangan aman alat)}$$

$$2.\quad I_o \le I_i \quad \text{(Arus maksimum sumber tidak melampaui arus aman alat)}$$

$$3.\quad P_o \le P_i \quad \text{(Daya keluaran maksimum tidak melampaui daya pemanasan aman)}$$

$$4.\quad L_o \ge L_i + L_c \quad \text{(Kapasitas induktansi barrier mampu menampung induktansi alat + KABEL)}$$

$$5.\quad C_o \ge C_i + C_c \quad \text{(Kapasitas kapasitansi barrier mampu menampung kapasitansi alat + KABEL)}$$

> ⚠️ **PERINGATAN FATAL PERANCANGAN:**  
> Kabel transmisi bertindak sebagai kapasitor dan induktor terdistribusi yang menyimpan energi! Mengabaikan perhitungan kapasitansi kabel ($C_c$) dan induktansi kabel ($L_c$) merupakan **kesalahan fatal dalam perancangan loop IS**.

---

### 12. Arsitektur Sistem: Zener Barrier vs Galvanic Isolator

| Parameter | Zener Barrier | Galvanic Isolated Barrier |
| :--- | :--- | :--- |
| **Prinsip Operasi** | Membuang kelebihan energi/lonjakan voltase ke bumi (*shunt-diode*). | Mentransfer sinyal menggunakan kopling optik (*optocoupler*) atau magnetik (*transformator*). |
| **Isolasi Galvanis** | **TIDAK ADA** hubungan isolasi fisik. | **ADA** (Memisahkan sirkuit *safe area* dan *hazardous area* secara total). |
| **Kebutuhan Grounding** | **WAJIB** terhubung ke sistem Pembumian IS khusus dengan resistansi sangat rendah ($< 1\,\Omega$). | **TIDAK** membutuhkan pembumian acuan khusus. |
| **Kerentanan Sinyal** | Sangat rentan terhadap gangguan *ground loop* dan perbedaan potensial tanah. | Kebal terhadap gangguan *ground loop*. |
| **Catu Daya & Dimensi** | Pasif (tidak butuh catu daya tersendiri), bentuk fisik sangat kompak dan tipis. | Aktif (umumnya membutuhkan suplai catu daya tersendiri), modul sedikit lebih lebar. |
| **Biaya & Penggunaan** | Harga unit lebih murah; umum ditemui pada instalasi fasilitas warisan lama (*legacy systems*). | Harga unit lebih mahal; mendominasi standar instalasi fasilitas industri modern saat ini. |

---

### 13. Tata Kelola Sistem IS: Dokumentasi & Jebakan Lapangan

#### Kewajiban Dokumentasi Sesuai IEC 60079-25
Dokumen deskriptif sistem (*Descriptive System Document* / DSD) wajib tersedia untuk setiap loop IS:
- [x] Salinan sertifikat keabsahan & level proteksi perangkat spesifik (*ia / ib / ic*).
- [x] Rekam jejak lembar perhitungan perbandingan *Entity Parameters* secara lengkap.
- [x] Data spesifikasi fisik kabel: tipe kabel, panjang bentang total, nilai $L_c/\text{m}$, dan $C_c/\text{m}$.
- [x] Skema diagram loop terverifikasi (**Kabel dan Terminal pembagi sirkuit IS wajib ditandai warna BIRU MUDA / Light Blue**).

#### Jebakan Lapangan / Kesalahan Klasik yang Sering Terjadi:
1. **Mengabaikan Kapasitansi Kabel ($C_c$):** Pada tarikan kabel instrumen yang panjang (ratusan meter), nilai kapasitansi kabel ($C_c$) terakumulasi melampaui nilai toleransi sisa ($C_o - C_i$).
2. **Penurunan Kualitas Grounding Zener:** Tahanan elektroda *IS Earth* memburuk atau korosi sehingga resistansinya naik di atas $1\,\Omega$, yang menggagalkan mekanisme pembuangan tegangan lebih.
3. **Penyusupan Perangkat Ilegal:** Teknisi menyisipkan alat ukur, display, kalibrator, atau indikator digital non-IS ke dalam loop tersertifikasi.
4. **Penggantian Unit Tanpa Prosedur MOC:** Mengganti transmitter tipe lama dengan transmitter model baru di lapangan tanpa menghitung ulang kesesuaian *Entity Parameters* (Merupakan **Pelanggaran Berat terhadap *Management of Change***).

---

### 14. Aturan Emas Proteksi Ex

```
┌───────────────────────────────────────────────┐ ┌───────────────────────────────────────────────┐
│              FONDASI REKAYASA                 │ │                HIERARKI ZONA                  │
├───────────────────────────────────────────────┤ ├───────────────────────────────────────────────┤
│ • Setiap metode berakar pada 1 dari 3         │ │ • Zona 0 menuntut kesempurnaan rekayasa dan   │
│   strategi murni: Kurung ledakannya (Ex d),   │ │   sistem redundansi ganda (Ex ia / Ex ma).    │
│   Pisahkan sumber panasnya (Ex p, o, q, m,    │ │ • Zona 2 mengizinkan efisiensi desain         │
│   e, n), atau Batasi energinya (Ex i).        │ │   (Ex n / Ex ic / Ex ec).                     │
│                                               │ │ • Prinsip Mutlak: Boleh turun zona, DILARANG  │
│                                               │ │   KERAS naik zona.                            │
└───────────────────────────────────────────────┘ └───────────────────────────────────────────────┘
┌───────────────────────────────────────────────┐ ┌───────────────────────────────────────────────┐
│               KEISTIMEWAAN EX I               │ │               DISIPLIN SISTEM                 │
├───────────────────────────────────────────────┤ ├───────────────────────────────────────────────┤
│ • Satu-satunya metode yang mencegah potensi   │ │ • Keselamatan Ex bukan sekadar membeli alat   │
│   energi penyalaan hadir sejak awal.          │ │   berlabel sertifikat mahal.                  │
│ • Sistem sinyal arus lemah yang mendukung     │ │ • Proteksi hidup pada integritas pemasangan   │
│   live maintenance secara penuh tanpa         │ │   (flame path Ex d, batas panjang kabel IS,   │
│   membutuhkan hot work permit.                │ │   grounding Zener) dan kepatuhan MOC.         │
└───────────────────────────────────────────────┘ └───────────────────────────────────────────────┘
```

---

## ❓ Antisipasi Pertanyaan Karyawan (FAQ Otomatis)

### Q1: Mengapa permukaan sambungan/flens junction box Ex d sama sekali tidak boleh dicat atau tergores?
**A:** Perlindungan *Ex d* mengandalkan celah sempit berukuran mikron yang disebut *flame path*. Jalur ini berfungsi untuk mendinginkan dan memadamkan api ledakan internal saat gas bertekanan memaksa keluar selungkup. Jika permukaan tersebut dicat tebal, partikel cat dapat merusak toleransi celah atau terbakar saat terjadi insiden. Sebaliknya, jika flens baret/tergores atau bautnya longgar, celah akan merenggang sehingga gas panas yang keluar belum sempat didinginkan dan langsung menyulut atmosfer eksplosif di luar.

### Q2: Kapan kita wajib memilih Galvanic Isolator dibandingkan Zener Barrier pada sistem Ex i?
**A:** Galvanic Isolator sangat disarankan pada hampir seluruh instalasi modern, terutama jika:
1. Lokasi pemasangan tidak memiliki sistem *dedicated IS earthing* dengan resistansi $< 1\,\Omega$ yang stabil.
2. Jarak kabel cukup jauh dan rentan mengalami masalah *ground loop* atau perbedaan potensial tanah.
3. Anda menginginkan kemudahan pemeliharaan berkala tanpa perlu pengujian resistansi tanah rutin. Zener barrier umumnya hanya dipertahankan pada instalasi warisan lama (*legacy*) atau saat ruang kabinet sangat terbatas dan anggaran per channel sangat ketat.

### Q3: Apakah instrumen bersertifikat Ex ia boleh dipasang di Zona 1 atau Zona 2?
**A:** **Boleh.** Prinsip hierarki keselamatan Ex mengizinkan peralatan turun zona (dipasang di zona dengan tingkat risiko bahaya yang lebih rendah daripada sertifikasinya). Namun, arah sebaliknya **dilarang mutlak**: peralatan *Ex ib* (untuk Zona 1) atau *Ex ic* (untuk Zona 2) tidak boleh dipasang di Zona 0.

### Q4: Mengapa parameter kabel ($L_c$ dan $C_c$) wajib dimasukkan dalam perhitungan Entity Parameter Ex i?
**A:** Kabel instrumen bukanlah penghantar murni ideal; kabel menyimpan energi listrik dalam bentuk medan induktansi ($L$) dan medan kapasitansi ($C$). Jika kabel ditarik sangat panjang, akumulasi energi tersimpan dalam kabel bersama instrumen lapangan dapat melampaui batas energi maksimum ($L_o$ dan $C_o$) yang sanggup dijaga oleh barrier, sehingga lonjakan pelepasan energi akibat hubung singkat kabel dapat memicu percikan yang membakar gas.

### Q5: Saya menemukan perangkat lama berlabel "Ex nA" di gudang. Apakah masih boleh dipakai untuk proyek penggantian di Zona 2?
**A:** Sesuai pembaruan standar IEC 60079-15 ke IEC 60079-7 (Ed. 5), konsep proteksi *Ex nA* kini telah dilebur dan diubah namanya menjadi **Ex ec**. Perangkat lama tetap aman digunakan selama sertifikasinya sesuai dengan desain awal dan spesifikasi area Zona 2 yang dituju. Namun, untuk pengadaan baru, pastikan dokumen pemesanan dan sertifikat pabrikan mencantumkan kode termutakhir yaitu **Ex ec**.

### Q6: Apa konsekuensinya jika teknisi lapangan mengganti transmitter IS yang rusak dengan model baru tanpa lapor ke Engineering/MOC?
**A:** Ini merupakan pelanggaran serius terhadap prosedur keselamatan (*Management of Change*). Meskipun transmitter baru sama-sama berlabel *Ex i*, parameter internalnya ($U_i, I_i, P_i, L_i, C_i$) kemungkinan besar berbeda dari transmitter lama. Jika $C_i$ transmitter baru lebih tinggi, batas total $C_i + C_c$ bisa melampaui $C_o$ barrier, sehingga sirkuit tersebut tidak lagi memiliki sertifikasi keselamatan yang sah dan rentan memicu ledakan.

---

## 📚 Glosarium & Istilah Penting

- **ATEX:** *Appareils destinés à être utilisés en ATmosphères EXplosibles* (Arahan standar keselamatan Uni Eropa untuk peralatan di area eksplosif).
- **Clearance:** Jarak terpendek yang diukur melalui media udara bebas antara dua bagian konduktif yang dialiri listrik.
- **Creepage:** Jarak terpendek sepanjang permukaan bahan isolasi padat antara dua bagian konduktif listrik.
- **Derating:** Penurunan batasan beban operasional komponen listrik (tegangan, arus, daya) di bawah kapasitas nominal maksimalnya demi meningkatkan keandalan dan faktor keamanan.
- **Entity Parameters:** Himpunan nilai batas elektris aman ($U, I, P, L, C$) yang tercantum pada sertifikat komponen *Intrinsic Safety* sebagai acuan verifikasi kecocokan sistem loop.
  - $U_o, I_o, P_o, L_o, C_o$: Parameter batas keluaran (*Output*) dari Barrier/Pencatu Daya aman.
  - $U_i, I_i, P_i, L_i, C_i$: Parameter batas masukan (*Input*) maksimum yang dapat diterima instrumen lapangan.
  - $L_c, C_c$: Induktansi dan Kapasitansi total yang disumbangkan oleh media kabel penghubung.
- **EPL (Equipment Protection Level):** Tingkat proteksi peralatan menurut standar IEC (Ga/Da untuk tingkat sangat tinggi, Gb/Db untuk tingkat tinggi, Gc/Dc untuk tingkat normal).
- **Ex d (Flameproof):** Metode proteksi di mana selungkup didesain mampu menahan ledakan gas internal tanpa membiarkan kobaran api menyebar keluar.
- **Ex e (Increased Safety):** Metode proteksi yang memberikan margin keamanan ekstra pada komponen listrik yang tidak memercik untuk mencegah suhu tinggi dan percikan.
- **Ex i (Intrinsic Safety):** Metode proteksi yang membatasi suplai energi listrik dan termal ke area berbahaya di bawah level energi penyalaan terkecil dari campuran gas.
- **Ex p (Pressurization):** Metode proteksi dengan memberikan tekanan lebih (*overpressure*) gas inert/udara bersih di dalam selungkup untuk mencegah masuknya atmosfer eksplosif dari luar.
- **Flame Path:** Celah sempit terkalibrasi pada sambungan mekanis selungkup *Ex d* yang berfungsi meredam dan mendinginkan nyala api sebelum keluar ke atmosfer bebas.
- **HazLoc:** *Hazardous Locations* (Area atau fasilitas dengan potensi keberadaan bahaya gas, uap cair, atau debu mudah meledak).
- **IEC:** *International Electrotechnical Commission* (Organisasi standardisasi global untuk bidang elektrikal dan elektronika, pembuat seri standar IEC 60079).
- **Live Maintenance:** Kegiatan perbaikan, kalibrasi, atau pembongkaran instrumen yang dilakukan secara langsung saat sirkuit masih aktif dialiri daya listrik.
- **MOC (Management of Change):** Prosedur formal manajemen keselamatan untuk mengevaluasi, menyetujui, dan mendokumentasikan setiap perubahan teknis sebelum diterapkan di lapangan.
- **Purging:** Proses pembilasan isi rongga selungkup menggunakan udara bersih atau gas pelindung sebelum daya listrik dinyalakan pada metode *Ex p*.
- **tE (Time tE):** Waktu yang dibutuhkan belitan motor listrik AC saat kondisi rotor macet (*locked rotor*) untuk memanas dari temperatur kerja nominal hingga temperatur batas maksimum yang diizinkan pada proteksi *Ex e*.