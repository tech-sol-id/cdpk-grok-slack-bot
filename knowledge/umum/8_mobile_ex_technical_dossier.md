---
sumber_dokumen: "8_Mobile_Ex_Technical_Dossier.pdf"
gdrive_file_id: "10oGu0pGvpUhWPBGK42l0r97Ajl5J1Unp"
gdrive_modified_time: "2026-07-21T15:41:38.000Z"
folder_asal: "Root Knowledge / ATEX & Ex Knowledge"
tanggal_ekstraksi: "2026-10-13"
tingkat_akses: "SEMUA_MEMBER"
---

# PART 8: Perangkat Mobile Ex di Lapangan – Panduan Teknis & Pelatihan Intrinsically Safe Devices untuk Lingkungan Berbahaya

*Handbook ATEX, Ex, HazLoc & Intrinsically Safe Devices*  
*Ditujukan untuk: Engineer Instrumentasi, HSE, Operasi, dan Procurement*

---

## 📌 Executive Summary

1. **Prinsip Intrinsic Safety (Ex i) untuk Mobilitas:** Pembatasan energi di bawah *Minimum Ignition Energy* (MIE) adalah satu-satunya metode proteksi ledakan yang praktis dan ergonomis untuk perangkat mobile (smartphone/tablet industri), menggantikan enclosure berat tipe flameproof (Ex d).
2. **Aturan Baku Lintas Zona:** Perangkat Zona 1 (`Ex ib`) diperbolehkan turun digunakan di area Zona 2. Namun sebaliknya, perangkat Zona 2 (`Ex ic`) **dilarang keras** dibawa masuk ke area Zona 1 karena perbedaan margin keselamatan dan toleransi terhadap kegagalan komponen (*fault tolerance*).
3. **Kesesuaian Spesifikasi Menyeluruh:** Pemilihan perangkat genggam wajib mencakup kecocokan menyeluruh antara klasifikasi Zona, Gas Group (misal IIC), Temperature Class (misal T4), serta rentang suhu ambien ($T_a$), bukan hanya klasifikasi zonanya saja.
4. **Integritas Ekosistem & Sertifikasi Operasional:** Komponen pelengkap seperti baterai resmi, stasiun pengisian daya (*charging*), aksesoris anti-statis, dan sensor nirkabel (*Bluetooth/RF*) merupakan satu kesatuan sertifikasi Ex. Penggunaan part pihak ketiga atau kelalaian prosedur membatalkan status keselamatan unit secara hukum dan teknis.

---

## 📖 Salinan Lengkap & Terstruktur

### 1. Objektif Pembelajaran Part 8

* **Prinsip Intrinsic Safety (Ex i):** Memahami alasan teknis mengapa pembatasan energi adalah satu-satunya metode praktis untuk perangkat genggam.
* **Klasifikasi Zona:** Membedakan perangkat Zona 1 (`Ex ib`) vs Zona 2 (`Ex ic`) serta implikasi keamanannya.
* **Ekosistem Connected Worker:** Memahami fungsi telemetri, proteksi *lone worker*, dan integrasi sensor eksternal.
* **Aturan & Seleksi:** Menguasai aspek baterai, aksesori, dan menggunakan *checklist* pemilihan sesuai area kerja.

---

### 2. Pendekatan Khusus Perangkat Mobile

Keterbatasan ukuran dan ergonomi menentukan metode proteksi yang layak dipakai pada perangkat genggam:

* **Mobilitas Penuh:** Dipegang, dipindahkan, dan digunakan langsung oleh operator selama berjam-jam tanpa henti.
* **Ergonomi & Bobot:** Harus ringan, tipis, dan tidak membebani pekerja (berbeda dengan *fixed equipment* seperti motor listrik).
* **Kebutuhan Daya Mandiri:** Membawa sumber energi mandiri (baterai) yang berpotensi memicu percikan jika terjadi korsleting.
* **Pemeliharaan Aktif:** Memerlukan penggantian baterai atau kartu (SIM/SD) secara langsung di lapangan (berbeda dengan instrumen statis).

---

### 3. Komparasi Pendekatan Proteksi Ledakan

#### A. Pendekatan Kurungan: Ex d (*Flameproof*)
* Menggunakan *enclosure* logam tebal dan berat.
* Bekerja dengan cara menahan ledakan dari dalam agar tidak menyebar ke atmosfer sekitar.
* Massa besar, tidak ergonomis untuk digenggam.
* Membuka tutup *enclosure* memerlukan izin kerja panas (*hot work permit*).
* Tidak cocok untuk perangkat mobile / genggam.

#### B. Pendekatan Pembatasan Energi: Ex i (*Intrinsic Safety*)
* Menggunakan rangkaian berenergi rendah dan ringan.
* Energi dijaga selalu berada di bawah MIE (*Minimum Ignition Energy*), sehingga tidak mampu memicu percikan.
* Ringan, kompak, dan ergonomis.
* Aman di-service meskipun dalam kondisi *energized* (bertegangan).
* Sangat ideal untuk perangkat mobile.

#### Ringkasan Perbandingan Teknis: Ex d vs Ex i

| Parameter | Ex d (*Flameproof*) | Ex i (*Intrinsic Safety*) |
| :--- | :--- | :--- |
| **Prinsip Proteksi** | Menahan & Mendinginkan | Membatasi Energi di bawah MIE |
| **Bobot & Ukuran** | Berat, Tebal, Logam Keras | Ringan, Kompak, Material Maju |
| **Buka Casing saat Energized** | ❌ Dilarang Keras | ✔️ Boleh Di-*service* |
| **Ganti Baterai di Lapangan** | ❌ Tidak Praktis | ✔️ Dimungkinkan (Baterai Khusus) |
| **Kesesuaian Mobile** | ❌ Sangat Rendah | ✔️ Sangat Tinggi (Metode Pilihan) |

> **Kesimpulan:** Keamanan Ex i berasal dari keterbatasan sirkuit, bukan dari massa *enclosure*. Ini memungkinkan pembuatan smartphone & tablet industri yang tipis.

---

### 4. Klasifikasi Perangkat: Zona 1 vs Zona 2

Perbedaan inti terletak pada toleransi kesalahan (*fault tolerance*) dan faktor keamanan sirkuit:

#### Perangkat Zona 1 (`Ex ib IIC T4 Gb`)
* **Toleransi Kesalahan:** Aman dengan 1 komponen gagal (*1 fault*).
* **Faktor Keamanan Arus:** $1{,}5\times$ (Proteksi ekstra ketat).
* **Area Aplikasi:** Unit proses kilang, *offshore*, area di sekitar *valve* & pompa.

#### Perangkat Zona 2 (`Ex ic IIC T4 Gc`)
* **Toleransi Kesalahan:** Hanya aman pada operasi normal (*tanpa fault* / *0 fault*).
* **Faktor Keamanan Arus:** $1{,}0\times$ (Tanpa margin tambahan).
* **Area Aplikasi:** Gudang, area berventilasi baik, ruang kompresor.

---

### 5. Prinsip Penggunaan Lintas Zona (*Cross-Zone*)

> **Aturan Dasar: Boleh Turun Zona, Tidak Boleh Naik.**

* **Skenario Aman (Fleksibilitas):**  
  Perangkat **Ex ib (Zona 1 / Gb)** $\rightarrow$ **SAH & AMAN** dipakai di area **Zona 2**.  
  *Keuntungan:* Menghemat biaya manajemen armada (*fleet management*) dengan standardisasi satu tipe perangkat untuk seluruh area fasilitas.
* **Skenario Berbahaya (Pelanggaran):**  
  Perangkat **Ex ic (Zona 2 / Gc)** $\rightarrow$ **DILARANG KERAS** dibawa masuk ke area **Zona 1**.  
  *Risiko:* Kurangnya toleransi kesalahan (*fault*) dapat memicu penyalaan atmosfer eksplosif sewaktu-waktu terjadi lonjakan atau malfungsi.

---

### 6. Cara Membaca *Marking* Sertifikasi

Contoh *marking*: **`II 2G Ex ib IIC T4 Gb`**

* **`II`** : Peralatan Permukaan / *Surface industries* (bukan tambang bawah tanah / Grup I).
* **`2G`** : Kategori ATEX 2 untuk Gas (Zona 1 & 2).
* **`Ex ib`** : Metode proteksi *Intrinsic Safety*, tahan terhadap 1 kesalahan komponen (*1 fault*).
* **`IIC`** : *Gas Group* paling menuntut / berisiko tinggi (mencakup Hidrogen dan Asetilen).
* **`T4`** : *Temperature Class* $\le 135^\circ\text{C}$ (aman jika temperatur penyalaan gas $> 135^\circ\text{C}$).
* **`Gb`** : *Equipment Protection Level* (EPL) Gas level b (konsisten dengan kebutuhan Zona 1).

> ⚠️ **PERINGATAN SUHU:** Perangkat bertanda T4 tidak memadai jika area operasi memiliki gas seperti Karbon Disulfida ($\text{CS}_2$) yang memerlukan kelas suhu **T6** (suhu penyalaan $\sim 90^\circ\text{C}$).

---

### 7. Ekosistem Perangkat Mobile Ex (*Connected Worker*)

Perangkat genggam Ex berfungsi sebagai pusat koordinasi pekerja modern di lapangan dengan modul terintegrasi:

* **Telemetri & IoT:** Mengirim data proses secara *real-time* ke ruang kendali (*control room*).  
  *Syarat Ex:* Modul RF & Antena harus lulus uji batas IS (*Intrinsically Safe*).
* **Kamera & RFID:** Mendukung inspeksi visual jarak jauh dan pemindaian barcode/RFID aset.  
  *Syarat Ex:* Kilat/Flash kamera dinilai secara ketat terhadap batas termal.
* **Sensor Bluetooth:** Terhubung (*pairing*) dengan detektor gas portabel pribadi.  
  *Syarat Ex:* Hanya dapat dipasangkan dengan perangkat yang saling teruji / kompatibel sertifikasinya.
* **Fitur Lone Worker:** Deteksi *Man-down*, *No-motion*, serta tombol darurat (SOS).  
  *Syarat Ex:* Sensor gerak internal tidak boleh menambah atau melampaui batas energi sirkuit.

---

### 8. Parameter Kritis Keselamatan Operasional

Pelanggaran terhadap elemen-elemen berikut secara otomatis **membatalkan sertifikasi Ex**:

1. **Baterai Bersertifikat:** Hanya gunakan *battery pack* asli yang tertera dalam dokumen sertifikasi. Baterai pihak ketiga atau tiruan membatalkan seluruh perlindungan keselamatan.
2. **Area Pengisian Daya (Charging):** Pengisian daya **WAJIB** dilakukan di Area Aman (*non-hazardous*), kecuali menggunakan stasiun pengisian khusus yang memiliki sertifikasi eksplisit untuk *hazardous area*.
3. **Penggantian Baterai di Lapangan (Hot-Swap):** Dilarang membuka atau melepas baterai di Zona berbahaya, kecuali perangkat tersebut memiliki sertifikasi eksplisit yang mengizinkan *hot-swap* baterai.
4. **Aksesori & Bahaya Elektrostatik:** Permukaan non-logam rentan menimbulkan muatan statis. Selalu gunakan sarung (*casing* / *holster*) resmi bersertifikasi, dan bersihkan layar sentuh hanya menggunakan kain lembap.

---

### 9. Checklist Pemilihan Perangkat Lapangan

#### Tahap 1: Evaluasi Area
* **Step 1: Tentukan Zona Area.** Petakan klasifikasi area pelanggan (Zona 0/1/2 untuk Gas, atau Zona 20/21/22 untuk Debu).
* **Step 2: Tetapkan EPL Minimum.** Pastikan EPL perangkat (Ga/Gb/Gc) memenuhi atau melampaui kebutuhan zona tersebut.
* **Step 3: Identifikasi Gas/Dust Group.** *Gas group* perangkat harus mencakup zat di lapangan (IIC otomatis mencakup IIA & IIB).
* **Step 4: Validasi Temperature Class.** T-Class perangkat harus berada di bawah ambang batas suhu penyalaan zat terendah di lokasi ($\text{T-Class} \ge \text{Kebutuhan Area}$).
* **Step 5: Periksa Suhu Ambien ($T_a$).** Rentang $T_a$ pada penandaan alat wajib mencakup kondisi suhu ekstrem lokasi kerja.
* **Step 6: Evaluasi Paparan Debu.** Jika terdapat risiko debu (Zona 20/21/22), verifikasi tanda tambahan (`...D / Da/Db/Dc`) serta rating IP *enclosure*.

#### Tahap 2: Verifikasi Dokumen & Kesiapan
* **Step 7: Uji Ketahanan Lingkungan.** Pastikan *rating* IP, resistansi korosi, dan ketahanan getaran/guncangan sesuai kondisi lapangan.
* **Step 8: Konfirmasi Baterai & Charger.** Validasi bahwa baterai asli terdaftar dan prosedur pengisian daya dipahami dengan benar.
* **Step 9: Verifikasi Modul Nirkabel.** Pastikan fungsi Bluetooth, RF, dan sensor eksternal tercantum dalam lingkup sertifikat.
* **Step 10: Analisis Sertifikat "X".** Baca buku panduan secara menyeluruh! Pahami dan terapkan seluruh klausul khusus (*Special Conditions of Use* / tanda X).
* **Step 11: Validasi Legalitas Sertifikat.** Pastikan sertifikat ATEX/IECEx sah dan sesuai dengan regulasi negara/klien terkait.
* **Step 12: Siapkan Pelatihan Operator.** Susun instruksi kerja (IK/SOP); operator wajib memahami batasan zona, tata cara *charging*, serta mitigasi bahaya elektrostatis.

---

### 10. Poin Penting (*Key Takeaways*)

* **Metode Proteksi:** Pembatasan energi (`Ex i`) adalah satu-satunya solusi aman dan ergonomis untuk perangkat mobile di area berbahaya.
* **Hierarki Zona:** Perangkat `Ex ib` (Zona 1) aman dipakai di Zona 2, namun perangkat `Ex ic` (Zona 2) tidak boleh masuk ke Zona 1.
* **Kecocokan Total:** Memilih perangkat tidak hanya mencocokkan Zona, melainkan wajib mencocokkan *Gas Group* dan *Temperature Class* terhadap material di lapangan.
* **Keamanan Ekosistem:** Baterai, pengisi daya, aksesori, dan modul Bluetooth merupakan bagian tak terpisahkan dari integritas sertifikasi Ex.
* **Kondisi Khusus (X):** Selalu cermati manual untuk *Special Conditions of Use*, khususnya aturan pembersihan elektrostatik dan penutupan antarmuka *port*.

---

## ❓ Antisipasi Pertanyaan Karyawan (FAQ Otomatis)

### Q1: Kenapa tim kita tidak boleh membeli smartphone tahan banting biasa (rugged smartphone) yang ada di marketplace untuk proyek kilang Zona 2?
**A:** Smartphone *rugged consumer* umumnya hanya mengantongi sertifikasi ketahanan fisik seperti IP68 atau standar militer MIL-STD (tahan air, debu, dan jatuh), **bukan sertifikasi proteksi ledakan Ex/ATEX**. Perangkat biasa memiliki kapasitansi internal, induktansi, dan baterai yang dapat memicu percikan listrik atau panas permukaan melebihi titik nyala gas berbahaya. Menggunakan perangkat tanpa rating `Ex ic` atau `Ex ib` di lingkungan berbahaya melanggar aturan K3 migas dan berisiko memicu ledakan fatal.

### Q2: Apakah boleh kita menukar baterai tablet Ex dengan baterai cadangan merk pihak ketiga yang kapasitas mAh-nya lebih besar dan lebih murah?
**A:** **Sangat dilarang.** Sertifikasi *Intrinsic Safety* (Ex i) menguji unit bersama pack baterai spesifik, termasuk rangkaian pembatas arus, sekring internal, dan bahan kimia baterainya. Menggunakan baterai pihak ketiga langsung membatalkan sertifikat Ex perangkat tersebut dan mengubah tablet menjadi sumber bahaya penyalaan aktif.

### Q3: Jika kita memiliki smartphone Zona 1 (Ex ib), apakah boleh dipinjamkan ke tim yang bekerja di Zona 2?
**A:** Boleh. Prinsip baku peralatan Ex menyatakan bahwa perangkat dengan tingkat proteksi lebih tinggi diperbolehkan "turun zona". Perangkat Zona 1 (`Ex ib` / EPL Gb) memiliki faktor keamanan arus $1{,}5\times$ dan tahan 1 kesalahan, sehingga sangat aman digunakan di Zona 2.

### Q4: Apakah boleh operator melakukan pengisian daya (charging) tablet Ex di shelter atau ruang istirahat yang berada di dalam Zona 1/2?
**A:** Tidak boleh, kecuali stasiun pengisian baterai tersebut secara khusus didesain dan bersertifikat Ex untuk lokasi tersebut. Proses pengisian daya baterai menghasilkan panas dan melibatkan pin kontak terbuka yang bertegangan tinggi tanpa pembatasan IS, sehingga port pengisian wajib ditutup rapat dan proses *charging* dilakukan di *Safe Area* (area aman non-berbahaya).

### Q5: Apa arti huruf "X" di akhir nomor sertifikat perangkat mobile Ex?
**A:** Huruf "X" menandakan adanya *Special Conditions for Safe Use* (Kondisi Khusus Penggunaan Aman). Contohnya: instruksi bahwa layar hanya boleh dibersihkan menggunakan kain lembap untuk menghindari muatan elektrostatis, penutup karet port USB harus selalu terkunci rapat saat di area berisiko, atau batasan suhu ambien pemakaian tertentu. Kondisi ini tercantum lengkap di buku manual alat dan wajib dipatuhi.

---

## 📚 Glosarium & Istilah Penting

* **ATEX:** *Appareils destinés à être utilisés en ATmosphères EXplosibles* – Petunjuk keselamatan dan standar kepatuhan peralatan untuk lingkungan eksplosif di Uni Eropa.
* **EPL (Equipment Protection Level):** Tingkat perlindungan peralatan yang ditentukan oleh standar IEC/ATEX untuk mengidentifikasi risiko penyalaan (Ga, Gb, Gc untuk gas; Da, Db, Dc untuk debu).
* **Ex d (*Flameproof*):** Metode proteksi di mana enclosure mekanis dibuat cukup kuat untuk menahan ledakan gas internal tanpa membiarkan api keluar ke lingkungan luar.
* **Ex i (*Intrinsic Safety*):** Metode proteksi yang membatasi energi listrik dan termal di dalam sirkuit di bawah ambang batas yang dibutuhkan untuk menyalakan gas atau debu yang mudah meledak.
  * **Ex ia:** Tingkat proteksi IS tertinggi, aman terhadap 2 kesalahan komponen bersamaan (cocok untuk Zona 0).
  * **Ex ib:** Tingkat proteksi IS menengah, aman terhadap 1 kesalahan komponen (cocok untuk Zona 1 dan 2).
  * **Ex ic:** Tingkat proteksi IS dasar, aman pada operasi normal tanpa kesalahan komponen (hanya untuk Zona 2).
* **MIE (*Minimum Ignition Energy*):** Energi percikan listrik terkecil yang diperlukan untuk memicu penyalaan campuran gas/udara tertentu.
* **Temperature Class (T-Class):** Klasifikasi suhu permukaan maksimum yang dapat dicapai oleh peralatan (contoh: T4 $\le 135^\circ\text{C}$, T6 $\le 85^\circ\text{C}-90^\circ\text{C}$).
* **Lone Worker Protection:** Fitur keselamatan terintegrasi pada perangkat mobile untuk mendeteksi pekerja yang terisolasi atau mengalami kecelakaan melalui sensor *man-down* (jatuh), *no-motion* (tidak bergerak), dan tombol darurat darurat (SOS).