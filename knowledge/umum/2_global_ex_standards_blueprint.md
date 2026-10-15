---
sumber_dokumen: "2_Global_Ex_Standards_Blueprint.pdf"
gdrive_file_id: "1UQKuba0cO-pElJWFYSA12FGhvlNsqlu4"
gdrive_modified_time: "2026-07-21T15:40:48.000Z"
folder_asal: "Root Knowledge / ATEX & Ex Knowledge"
tanggal_ekstraksi: "2026-10-15"
tingkat_akses: "SEMUA_MEMBER"
---

# Handbook ATEX, Ex, HazLoc & Intrinsically Safe Devices: Peta Regulasi dan Standar Global (Part II)

## 📌 Executive Summary

1. **Fondasi Universal IEC 60079:** Perbedaan utama antar-regulasi proteksi ledakan global (*Explosion Protection*) seperti ATEX (Eropa), IECEx (Internasional), dan HazLoc (Amerika Utara) mayoritas bersifat administratif dan legal-yuridiksi, bukan perbedaan pada prinsip dasar sains atau keselamatan teknisnya.
2. **Dua Pilar Regulasi ATEX:** ATEX memisahkan tanggung jawab secara tegas antara Directive 2014/34/EU (ATEX 114) yang mengikat produsen alat (*equipment/CE marking*), dan Directive 1999/92/EC (ATEX 137) yang membebani pemberi kerja (*workplace/EPD*). Sertifikat produk tidak menggantikan kewajiban dokumen proteksi ledakan di lokasi kerja.
3. **Miskonsepsi Kritis Pengelompokan Gas:** Urutan tingkat bahaya gas pada rezim NEC 500 berkebalikan dengan rezim IEC/ATEX. Pada NEC 500, Group A (Asetilena) adalah yang paling berbahaya/sensitif, sedangkan pada IEC/ATEX, Group IIC adalah kelompok gas yang paling berbahaya.
4. **Sistem Zonasi Amerika (AEx):** NEC Article 505 (Gas) dan 506 (Debu) telah mengadopsi sistem *Zone* berbasis IEC 60079 melalui penandaan `AEx`, memungkinkan integrasi dan pemasangan peralatan berperingkat Zone ke dalam area Division tradisional.
5. **Strategi Efisiensi Multi-Approval:** Pengujian fisik cukup dilakukan satu kali di laboratorium uji terakreditasi IECEx (ExTL) untuk menerbitkan ExTR (*Test Report*). Laporan portabel ini berfungsi sebagai "kunci utama" (*master key*) untuk mengurus paspor administratif regional (ATEX, EAC Ex, INMETRO, PESO, KCs) tanpa pengujian fisik ulang.

---

## 📖 Salinan Lengkap & Terstruktur

### 1. Informasi Dokumen
* **Judul Publikasi:** Handbook ATEX, Ex, HazLoc & Intrinsically Safe Devices – Peta Regulasi dan Standar Global (Part II)
* **Subjudul:** Panduan Teknis Explosion Protection untuk Engineer, HSE, & Procurement
* **Dasar Regulasi:** Seri IEC/EN 60079, ATEX, IECEx, NEC/CEC
* **Edisi:** Edisi 2.3 – 2026
* **Editor:** Adrian Bany Kansil
* **Status Distribusi:** FOR INTERNAL USE ONLY

---

### 2. Fondasi Bersama di Balik Kerangka Global (*The Regulatory Bridge*)

Kerangka keselamatan proteksi ledakan global bertumpu pada satu standar inti bersama: **IEC 60079 (Central Station)**. Perbedaan antar-rezim regional sebagian besar bersifat administratif, bukan perbedaan prinsip keselamatan teknis.

* **ATEX:** Rezim wajib hukum regional Uni Eropa. Mengadopsi fondasi standar sebagai **EN 60079**.
* **IECEx:** Skema sertifikasi internasional sukarela (*voluntary*). Memakai fondasi **IEC 60079** secara langsung.
* **HazLoc (NEC/CEC):** Rezim Amerika Utara. Menggunakan sistem tradisional (*Division*) dan adopsi sistem *Zone* (NEC 505/506) yang selaras dengan IEC 60079.
* **Jalur Sertifikasi Regional Lain yang Menginduk:**
  * **EAC Ex** (Eurasia / TR CU 012)
  * **INMETRO** (Brasil)
  * **PESO** (India)

---

### 3. Dua Pilar ATEX: Produk vs. Tempat Kerja

| Aspek Pembanding | The Product: Directive 2014/34/EU (ATEX 114) | The Workplace: Directive 1999/92/EC (ATEX 137) |
| :--- | :--- | :--- |
| **Objek Fokus** | Peralatan & *protective systems* (Listrik & Non-Listrik/Mekanik) | Keselamatan & kesehatan pekerja di atmosfer ledak |
| **Pihak Terbebani** | Produsen (*Manufacturer*) | Pemberi Kerja (*Employer*) |
| **Fokus Utama** | Desain, pengujian, sertifikasi, dan *CE marking* | Klasifikasi area/zona, pemilihan alat, prosedur aman |
| **Bukti Kepatuhan** | *CE marking* + *EU Declaration of Conformity* | *Explosion Protection Document* (EPD) + Dokumen Peta Zona |

> **Titik Temu Kritis:** Pemberi kerja bertanggung jawab memilih kategori produk yang tepat sesuai zona hasil klasifikasi area. **Kepemilikan sertifikat produk TIDAK menggantikan kewajiban penyusunan EPD di tempat kerja.**

---

### 4. Anatomi Penandaan ATEX (*Marking Plate Anatomy*)

Contoh penandaan pelat nama alat:
$$\text{CE 0123} \quad \langle\varepsilon x\rangle \quad \text{II 2G} \quad \text{Ex db IIC T4 Gb}$$

Rincian pembedahan elemen penandaan:
1. **`CE 0123` (Kepatuhan Hukum Eropa):** Tanda CE menunjukkan kepatuhan direktif Uni Eropa. Angka `0123` merupakan nomor identifikasi *Notified Body* (wajib dicantumkan untuk peralatan risiko tinggi / Category 1 dan Category 2 listrik).
2. **$\langle\varepsilon x\rangle$ (Simbol Ex Heksagonal):** Simbol grafis khusus komunitas Eropa penanda peruntukan di atmosfer ledak (*explosive atmosphere*).
3. **`II 2G` (Lapisan Administratif ATEX):**
   * **`II`:** Group II (Peralatan industri permukaan / non-tambang).
   * **`2`:** Category 2 (Tingkat proteksi tinggi, dirancang aman untuk Zone 1).
   * **`G`:** Gas (Menunjukkan proteksi terhadap gas/uap/kabut; `D` untuk debu).
4. **`Ex db IIC T4 Gb` (Lapisan Teknis IEC 60079-0):**
   * **`Ex`:** Tanda kesesuaian standar proteksi ledakan.
   * **`db`:** Jenis proteksi penutup tahan api (*flameproof enclosure* - Equipment Protection Level b).
   * **`IIC`:** Gas group representatif (mencakup gas paling mudah menyala, misal hidrogen/asetilena).
   * **`T4`:** Temperature class (suhu permukaan maksimum alat tidak melampaui 135°C).
   * **`Gb`:** *Equipment Protection Level* (EPL Gb, tingkat proteksi tinggi untuk gas di Zone 1).

---

### 5. Skema IECEx: Satu Sertifikat, Diterima Di Mana Saja

Skema sukarela internasional berbasis IEC 60079 yang bertujuan memfasilitasi perdagangan global tanpa pengujian berganda melalui 3 pilar:

1. **Certified Equipment Scheme (Peralatan):**
   * Alur dokumen kunci: **ExTR** (*Test Report*) + **QAR** (*Quality Assessment Report*) $\rightarrow$ Menghasilkan **CoC** (*Certificate of Conformity*).
2. **Certified Persons Scheme (Personel / CoPC):**
   * Sertifikasi kompetensi individu dalam bidang proteksi ledakan (contoh: Unit Ex 001 - Prinsip dasar proteksi ledakan).
3. **Certified Service Facilities Scheme (Fasilitas Perbaikan):**
   * Sertifikasi untuk bengkel reparasi, inspeksi, dan *overhaul* peralatan Ex (sesuai standar IEC 60079-19).
4. **Keamanan & Transparansi Digital:**
   * Setiap sertifikat CoC memiliki nomor registrasi unik yang dapat diverifikasi secara publik dan *real-time* melalui *Online Certificate System* resmi IECEx.

---

### 6. Matriks Diagnostik: ATEX vs. IECEx

| Aspek | ATEX | IECEx |
| :--- | :--- | :--- |
| **Sifat & Wilayah Regulasi** | Wajib (*Mandatory by Law*) di Uni Eropa | Sukarela (*Voluntary*), diakui secara global di pasar internasional |
| **Standar Teknis** | EN 60079 (Standar harmonis Eropa) | IEC 60079 (Standar IEC langsung) |
| **Lembaga Penilai** | *Notified Body* (NB) | *ExCB* (*Certification Body*) + *ExTL* (*Testing Laboratory*) |
| **Bukti Kesesuaian** | *CE Marking* + *EU Declaration of Conformity* | *IECEx CoC* (Dapat diverifikasi langsung secara daring) |
| **Peralatan Mekanik** | Termasuk sejak awal penerbitan direktif | Standar non-listrik/mekanik mulai diintegrasikan |

> **Prinsip Kolaborasi:** **Saling Melengkapi, Bukan Bersaing.** Produsen cukup melakukan uji fisik satu kali untuk mendapatkan IECEx ExTR, kemudian laporan portabel tersebut digunakan untuk mengurus sertifikasi administratif ATEX dan sertifikasi regional lainnya.

---

### 7. Kerangka HazLoc (NEC/CEC): Sistem Class & Division

Sistem tradisional Amerika Utara (NEC 500 / CEC) memetakan area berbahaya berdasarkan matriks materi dan probabilitas:

```
[The North American HazLoc Matrix]
├── Class I   : Gas / Uap (Kilang, Petrokimia)
├── Class II  : Debu / Dust (Silo biji-bijian, Logam)
└── Class III : Serat terbang / Flyings (Tekstil, Pemrosesan Kayu)

Probabilitas Kehadiran:
├── Division 1 : Hadir terus-menerus atau periodik dalam operasi normal / kegagalan alat rutin.
└── Division 2 : Jarang hadir / hanya hadir jika terjadi kecelakaan atau sistem ventilasi abnormal (terkurung).
```

* **Peringatan Penting:** Sistem *Division* hanya memiliki 2 tingkat probabilitas, sedangkan sistem *Zone* (IEC) memiliki 3 tingkat. **Division 1 mencakup gabungan Zone 0 dan Zone 1.** Pemetaan klasifikasi tidak bersifat satu-lawan-satu secara mutlak.
* **Pengawasan & Kepatuhan:** Kepatuhan dibuktikan lewat *Listing/Labelling* oleh *Nationally Recognized Testing Laboratory* (NRTL, seperti UL, FM, CSA) dan diawasi oleh *Authority Having Jurisdiction* (AHJ / inspektur lokal).

---

### 8. Miskonsepsi Fatal: Sistem Pengelompokan Gas yang Terbalik (*The Flipped Groups Matrix*)

Terdapat perbedaan mendasar dan berbahaya antara penamaan kelompok gas pada sistem Amerika (NEC 500) dan sistem Global (IEC/ATEX):

| Material Representatif | NEC 500 (Amerika Utara) | IEC / ATEX (Internasional) |
| :--- | :--- | :--- |
| **Asetilena** | **Group A** *(Paling Berbahaya / Sulit)* | **IIC** *(Paling Berbahaya / Sulit)* |
| **Hidrogen** | **Group B** | **IIC** / **IIB+H2** |
| **Etilena** | **Group C** | **IIB** |
| **Propana / Metana** | **Group D** *(Paling Ringan)* | **IIA** *(Paling Ringan)* |

> ⚠️ **PERINGATAN KESELAMATAN:** Engineer yang terbiasa dengan standar IEC dapat keliru menganggap 'Group A' sebagai kelompok gas paling aman/ringan. Pada sistem HazLoc NEC 500, **Group A (Asetilena) adalah kelompok gas yang paling berbahaya dan paling mudah tersulut.**

---

### 9. Resolusi Suhu HazLoc: Klasifikasi T-Code Spesifik

Rezim HazLoc NEC/CEC membagi kelas temperatur menjadi lebih spesifik menggunakan sub-kode alfabet untuk memberikan toleransi desain yang lebih presisi:

* **T1:** $\le 450^\circ\text{C}$
* **T2:** $\le 300^\circ\text{C}$
  * **T2A:** $\le 280^\circ\text{C}$
  * **T2B:** $\le 260^\circ\text{C}$
  * **T2C:** $\le 230^\circ\text{C}$
  * **T2D:** $\le 215^\circ\text{C}$
* **T3:** $\le 200^\circ\text{C}$
  * **T3A:** $\le 180^\circ\text{C}$
  * **T3B:** $\le 165^\circ\text{C}$
  * **T3C:** $\le 160^\circ\text{C}$
* **T4:** $\le 135^\circ\text{C}$
  * **T4A:** $\le 120^\circ\text{C}$
* **T5:** $\le 100^\circ\text{C}$
* **T6:** $\le 85^\circ\text{C}$

> **Ketentuan Substitusi:** Peralatan dengan sub-kode temperatur (misalnya T2C = 230°C) **tidak boleh disamakan atau ditukar secara otomatis** dengan kode utama di atasnya (T2 = 300°C), karena batas suhu operasinya lebih ketat.

---

### 10. Menjembatani Benua: Sistem Zone Amerika Utara (AEx)

Sejak tahun 1996, NEC Article 505 (Gas) dan Article 506 (Debu) memperkenalkan alternatif *Zone System* untuk menyelaraskan instalasi industri di AS dengan pasar global berbasis IEC.

Contoh penandaan proteksi Zone di Amerika:
$$\mathbf{Class\ I,\ Zone\ 1,\ AEx\ db\ IIC\ T4\ Gb}$$

* **`Class I, Zone 1`:** Penamaan lokasi bahaya gaya Amerika (menggantikan klasifikasi Division 1).
* **`AEx`:** Tanda resmi bahwa alat disertifikasi berdasarkan standar proteksi Zone Amerika Serikat (bukan sekadar sertifikat Ex impor tanpa akreditasi lokal).
* **`db IIC T4 Gb`:** Standar adopsi langsung IEC (Metode proteksi flameproof enclosure `db`, Gas Group `IIC`, Kelas Suhu `T4`, dan `EPL Gb`).
* **Interoperabilitas:** NEC mengizinkan peralatan yang memiliki sertifikasi rating Zone untuk dipasang pada area **Division 2** tradisional.

---

### 11. Padanan Lintas-Rezim: Tingkat Area Berbahaya (*The Master Equivalency Grid*)

#### A. Padanan Atmosfer Gas (*Gas Equivalent*)
| Tingkat Kehadiran Gas | IEC 60079 | ATEX (Directive) | IECEx (EPL) | NEC 500 (HazLoc) |
| :--- | :--- | :--- | :--- | :--- |
| **Terus-menerus / Kontinu** | Zone 0 | Category 1G | EPL Ga | \multirow{2}{*}{Division 1} |
| **Operasi Normal Rutin** | Zone 1 | Category 2G | EPL Gb | |
| **Jarang / Singkat (Abnormal)** | Zone 2 | Category 3G | EPL Gc | Division 2 |

#### B. Padanan Atmosfer Debu (*Dust Equivalent*)
| Tingkat Kehadiran Debu | IEC 60079 | ATEX (Directive) | IECEx (EPL) | NEC 500 (HazLoc) |
| :--- | :--- | :--- | :--- | :--- |
| **Terus-menerus / Kontinu** | Zone 20 | Category 1D | EPL Da | \multirow{2}{*}{Division 1} |
| **Operasi Normal Rutin** | Zone 21 | Category 2D | EPL Db | |
| **Jarang / Singkat (Abnormal)** | Zone 22 | Category 3D | EPL Dc | Division 2 |

> ⚠️ **Catatan Yuridis:** Tabel padanan ini bersifat indikatif teknis untuk perbandingan rekayasa dan **bukan merupakan kesetaraan hukum otomatis**. Sertifikasi alat harus selalu dicocokkan dengan regulasi lokal di yurisdiksi tempat instalasi fasilitas berdiri.

---

### 12. Peta Standar Global & Strategi Multi-Approval (*The Funnel of Certification*)

```
[Uji Fisik Tunggal]             [Master Key]                        [Konversi Paspor Administratif]
  (ExtL Lab Test)            (IECEx ExTR Report)                     (Tanpa Uji Fisik Ulang)
┌─────────────────┐        ┌─────────────────────┐        ┌──► ATEX (Eropa - Notified Body)
│ 1. Uji Fisik    │        │ 2. Penerbitan       │        ├──► EAC Ex (Eurasia - TR CU 012)
│ Terhadap Standar├───────►│    IECEx ExTR       ├───────┼──► PESO (India)
│ IEC 60079       │        │    (Portable Key)   │        ├──► INMETRO (Brasil)
└─────────────────┘        └─────────────────────┘        └──► KCs (Korea Selatan), dll.
```

* **Prinsip Inti:** Kerangka proteksi ledakan global bukanlah ribuan standar yang berdiri sendiri-sendiri, melainkan **satu standar sains universal (IEC 60079)** yang dibungkus dalam berbagai bentuk "paspor administratif" regional.
* **Efisiensi Anggaran & Waktu:** Pemahaman atas konversi IECEx ExTR memangkas biaya berulang dan mempercepat pengadaan perangkat tanpa harus mengirim sampel fisik uji ke setiap negara tujuan.

---

## ❓ Antisipasi Pertanyaan Karyawan (FAQ Otomatis)

**P: Kalau perangkat sudah punya sertifikat ATEX (misal: II 2G Ex db IIC T4 Gb), apakah boleh langsung kita pasang di proyek klien yang mewajibkan standar Amerika (NEC HazLoc)?**  
*J:* Tidak bisa langsung. Meskipun secara teknis desain proteksinya setara, otoritas di Amerika Utara (AHJ/OSHA) mewajibkan sertifikasi melalui lembaga NRTL (seperti UL, FM, CSA) dengan penandaan Class/Division atau tanda `AEx`. Namun, laporan pengujian perangkat dapat dijadikan dasar konversi dokumen tanpa uji lab dari nol.

**P: Pada dokumen pengadaan terdapat spesifikasi alat "NEC Group A", tetapi tim purchasing memesan "IEC Group IIA" karena dikira sama-sama kode huruf pertama. Apa risikonya?**  
*J:* Ini adalah kesalahan fatal. Pada IEC, Group IIA adalah proteksi untuk gas paling ringan (seperti propana), sedangkan pada NEC 500, Group A adalah gas paling berbahaya dan paling mudah tersulut (asetilena). Memasang alat berating IIA di lingkungan gas Group A dapat memicu ledakan akibat celah penahan api (*flamepath*) yang terlalu longgar.

**P: Apa perbedaan utama sertifikat ExTR dan CoC di skema IECEx?**  
*J:* ExTR (*Explosion Protection Test Report*) adalah laporan hasil uji laboratorium independen terhadap sampel fisik produk. Sedangkan CoC (*Certificate of Conformity*) adalah sertifikat resmi yang menyatakan produk telah memenuhi ExTR dan pabrik pembuatnya telah lulus audit mutu berkala (*Quality Assessment Report* / QAR).

**P: Apakah perusahaan kita cukup memegang sertifikat ATEX Directive 2014/34/EU untuk memenuhi seluruh audit keselamatan di area pabrik?**  
*J:* Tidak cukup. Direktif 2014/34/EU (ATEX 114) hanya membuktikan bahwa alat yang dibeli dari produsen berstatus aman. Sebagai pengelola fasilitas, kita wajib mematuhi Direktif 1999/92/EC (ATEX 137) yang mewajibkan penyusunan *Explosion Protection Document* (EPD), pemetaan zona area berbahaya, serta penetapan SOP kerja aman bagi personel.

**P: Mengapa pada label alat tercantum kode suhu T2C, dan bisakah kita menggantinya dengan alat berkode T2 biasa jika stok gudang habis?**  
*J:* Tidak boleh. Kode T2 mengizinkan suhu permukaan maksimum hingga 300°C, sementara sub-kode T2C membatasi suhu permukaan maksimal di 230°C. Mengganti alat T2C dengan T2 dapat membuat temperatur alat melampaui titik nyala (*auto-ignition temperature*) gas di area tersebut.

---

## 📚 Glosarium & Istilah Penting

* **AHJ (*Authority Having Jurisdiction*):** Badan, badan hukum, atau individu yang bertanggung jawab menegakkan persyaratan kode atau standar (misalnya inspektur kebakaran regional, pengawas keselamatan setempat).
* **ATEX (*Atmosphères Explosibles*):** Kerangka regulasi hukum Uni Eropa yang mengatur keselamatan peralatan (Directive 2014/34/EU) dan tempat kerja (Directive 1999/92/EC) di area rawan ledakan.
* **CoC (*Certificate of Conformity*):** Dokumen sertifikat kesesuaian resmi yang diterbitkan oleh badan sertifikasi (ExCB) pada skema IECEx.
* **CoPC (*Certificate of Personnel Competence*):** Sertifikasi kompetensi resmi untuk personel yang bekerja di area proteksi ledakan dalam skema IECEx.
* **EPD (*Explosion Protection Document*):** Dokumen penilaian risiko ledakan komprehensif yang wajib dimiliki oleh pemberi kerja sesuai mandat ATEX 137.
* **EPL (*Equipment Protection Level*):** Tingkat proteksi peralatan yang ditentukan berdasarkan risiko alat tersebut menjadi sumber penyalaan (contoh: Ga, Gb, Gc untuk gas; Da, Db, Dc untuk debu).
* **ExCB (*IECEx Certification Body*):** Badan sertifikasi yang diakui secara internasional untuk menerbitkan sertifikat IECEx CoC dan QAR.
* **ExTL (*IECEx Testing Laboratory*):** Laboratorium terakreditasi yang berhak melakukan pengujian teknis fisik dan mengeluarkan laporan ExTR.
* **ExTR (*Explosion Protection Test Report*):** Laporan teknis hasil uji produk terhadap standar seri IEC 60079 yang diakui secara global.
* **HazLoc (*Hazardous Locations*):** Istilah standar di Amerika Utara (NEC/CEC) untuk mendefinisikan lokasi kerja yang berpotensi memiliki bahaya kebakaran atau ledakan.
* **NEC (*National Electrical Code*):** Standar instalasi kelistrikan Amerika Serikat (diterbitkan oleh NFPA sebagai NFPA 70).
* **Notified Body (NB):** Lembaga independen di Uni Eropa yang ditunjuk resmi oleh negara anggota untuk menilai kesesuaian produk terhadap direktif ATEX.
* **NRTL (*Nationally Recognized Testing Laboratory*):** Laboratorium pengujian independen di Amerika Serikat yang diakui oleh OSHA (contoh: UL, FM, CSA).
* **QAR (*Quality Assessment Report*):** Laporan audit sistem manajemen mutu fasilitas pabrik manufaktur peralatan Ex.