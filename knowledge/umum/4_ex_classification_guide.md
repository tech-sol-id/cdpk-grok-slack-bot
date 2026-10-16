---
sumber_dokumen: "4_Ex_Classification_Guide.pdf"
gdrive_file_id: "1vAsjdQMtk9TJFThbE-w1Hi0KpYAqodDS"
gdrive_modified_time: "2026-07-21T15:41:02.000Z"
folder_asal: "Root Knowledge / ATEX & Ex Knowledge"
tanggal_ekstraksi: "2026-10-16"
tingkat_akses: "SEMUA_MEMBER"
---

# Handbook ATEX, Ex, HazLoc — PART IV: Klasifikasi Zat & Peralatan

## 📌 Executive Summary
1. **Zona Tidak Berdiri Sendiri**: Mengetahui klasifikasi Zona saja (0/1/2) tidak mencukupi untuk memilih peralatan Ex; diperlukan integrasi jenis zat (*Gas/Dust Group*), batas panas permukaan (*Temperature Class*), dan toleransi gangguan peralatan (*Equipment Protection Level / EPL*).
2. **Prinsip Inklusif Menaik Group Gas & Debu**: Gas dikelompokkan ke dalam IIA, IIB, dan IIC berdasarkan MESG (*Maximum Experimental Safe Gap*) dan rasio MIC. Debu dikelompokkan ke IIIA, IIIB, dan IIIC. Peralatan dengan grup proteksi lebih tinggi (misal IIC atau IIIC) aman mencakup dan digunakan pada grup di bawahnya (IIB/IIA atau IIIB/IIIA), namun tidak sebaliknya.
3. **Independensi Gas Group dan Batas Suhu (T-Class)**: Kemudahan gas menyala akibat percikan (*Gas Group*) independen dari suhu penyalaan mandirinya (*Auto-ignition Temperature*). Suhu permukaan maksimum alat harus selalu lebih rendah dari suhu penyalaan zat.
4. **Hierarki Keandalan "Boleh Turun Zona, Tidak Boleh Naik"**: Peralatan dengan EPL atau Kategori ATEX lebih tinggi (misal EPL Ga / 1G) bebas dipasang di zona risiko lebih rendah (Zona 1 atau Zona 2), namun peralatan EPL rendah (Gc / 3G) dilarang keras dipasang di zona berisiko lebih tinggi.
5. **Sintesis 4 Parameter Pemilihan**: Pemilihan peralatan Ex yang sah (*compliant*) mensyaratkan kecocokan mutlak keempat pilar: Zona Lingkungan $\rightarrow$ EPL/Kategori Minimum; Jenis Zat $\rightarrow$ Gas/Dust Group Minimum; Suhu Penyalaan $\rightarrow$ Temperature Class Maksimum; serta Kondisi Fisik $\rightarrow$ Metode Proteksi & Kode IP.

---

## 📖 Salinan Lengkap & Terstruktur

### 1. Informasi Dokumen
* **Judul**: HANDBOOK ATEX, Ex, HazLoc — PART IV: Klasifikasi Zat & Peralatan
* **Subjudul**: Panduan Teknis Explosion Protection untuk Engineer Instrumentasi, Listrik & HSE.
* **Edisi**: 2.3 — 2026
* **Editor**: Adrian Bany Kansil

---

### 2. Mengapa Mengetahui 'Zona' Saja Tidak Cukup?
Mengetahui Zona (berdasarkan pembahasan PART III: ZONA) hanya menjawab: **DI MANA & SEBERAPA SERING** atmosfer eksplosif muncul (Zona 0, Zona 1, atau Zona 2). 

Untuk merangkai dan membaca *Marking* Peralatan Ex secara utuh, diperlukan pemahaman terhadap tiga pertanyaan krusial lainnya:
* **ZAT APA? (Bab 12)**: Menentukan seberapa mudah zat menyala (*Gas/Dust Group*).
* **BERAPA SUHUNYA? (Bab 13)**: Menentukan batas panas permukaan alat (*Temperature Class* / °C).
* **SEBERAPA ANDAL? (Bab 14)**: Menentukan toleransi gangguan alat (*Equipment Protection Level / EPL*).

> **Catatan Konseptual**: PART IV berfungsi sebagai 'tata bahasa' komprehensif untuk merangkai dan membaca pelat penandaan (*Ex Marking*) pada peralatan Ex.

---

### 3. Peta Pengelompokan Lingkungan Standar IEC 60079
Berdasarkan standar IEC 60079, lingkungan berbahaya (*Hazardous Areas*) dipetakan ke dalam 3 grup utama:

| Grup Lingkungan | Definisi & Karakteristik Area | Detail / Contoh Zat |
| :--- | :--- | :--- |
| **GROUP I** | Tambang Bawah Tanah | *Firedamp* (Gas Metana Tambang) & Debu Batubara |
| **GROUP II** | Industri Permukaan (Gas & Uap) | Gas mudah terbakar, uap cairan kimiawi / hidrokarbon |
| **GROUP III** | Industri Permukaan (Debu / *Dust*) | Partikel debu yang mudah menyala/meledak |

> ⚠️ **PERINGATAN**: Peralatan Group II tidak otomatis cocok untuk Group I karena adanya perbedaan standar pengujian. Fokus utama panduan ini adalah **Group II (Gas)** dan **Group III (Debu)**.

---

### 4. Hierarki Gas Group (Group II) & Prinsip Inklusif Menaik
Tingkat bahaya penyalaan gas meningkat dari IIA hingga IIC:
* **IIA — Paling mudah diproteksi**: Propana, Gas Alam, Amonia.
* **IIB — Menengah**: Etilena, Dietil Eter.
* **IIC — Paling sulit diproteksi / Kasus terberat**: Hidrogen, Asetilena, Karbon disulfida.

#### Prinsip Inklusif Menaik:
Peralatan bersertifikat **IIC** aman digunakan pada atmosfer **IIB** dan **IIA**. Namun, peralatan bertanda **IIA TIDAK BOLEH** dipakai di area **IIC**.

---

### 5. Mekanisme Batas Zat: MESG & MIC Ratio
Pengelompokan gas didasarkan pada dua parameter pengujian fisik:
* **MESG (*Maximum Experimental Safe Gap*)**: Celah maksimum antara dua bagian dinding ruang uji yang mampu mendinginkan gas hasil ledakan internal sehingga atmosfer eksplosif di luar celah TIDAK ikut menyala.
* **MIC (*Minimum Igniting Current*) Ratio**: Rasio arus penyalaan minimum gas uji relatif terhadap gas metana.

| Gas Group | Karakter Proteksi | MESG (Celah Aman) | MIC Ratio |
| :--- | :--- | :--- | :--- |
| **IIA** | Paling Mudah | $> 0{,}9\text{ mm}$ | $> 0{,}8$ |
| **IIB** | Menengah | $0{,}5\text{ mm} - 0{,}9\text{ mm}$ | $0{,}45 - 0{,}8$ |
| **IIC** | Paling Sulit | $< 0{,}5\text{ mm}$ | $< 0{,}45$ |

*Aturan Dasar: Semakin kecil nilai MESG suatu gas, semakin mudah lidah apinya menembus celah fisik, sehingga semakin sulit diproteksi (membutuhkan grup peralatan yang lebih tinggi).*

---

### 6. Dust Group (Group III): Fokus pada Penetrasi & Lapisan
Pengelompokan bahaya debu/serat mudah terbakar:

* **IIIA: Combustible Flyings**
  * Definisi: Partikel padat berukuran besar ($> 500\ \mu\text{m}$).
  * Contoh: Serpih kayu, serat kapas, rayon.
* **IIIB: Non-Conductive Dust**
  * Definisi: Debu halus ($ \le 500\ \mu\text{m}$) yang tidak menghantarkan arus listrik.
  * Contoh: Tepung gandum/beras, gula, serbuk plastik.
* **IIIC: Conductive Dust** ⚠️
  * Definisi: Debu halus penghantar listrik. Paling berbahaya.
  * Contoh: Serbuk logam, karbon/grafit.

#### Perbedaan Kritis Gas vs Debu:
* Pada bahaya debu, ketahanan terhadap masuknya partikel atau **Ingress Protection (IP)** dan **pembatasan suhu** jauh lebih krusial dibandingkan dimensi celah pendingin ledakan (MESG). 
* Debu kategori IIIC sangat berbahaya karena konduktivitasnya dapat langsung menjembatani sirkuit listrik (*short circuit* internal).
* **Prinsip Inklusif Menaik Debu**: Kategori sertifikasi **IIIC** mencakup penggunaan untuk **IIIB** dan **IIIA**.

---

### 7. Aturan Emas Temperature Class (Gas)
Klasifikasi suhu (*T-Class*) membatasi suhu permukaan tertinggi yang boleh dicapai oleh peralatan agar tidak menyulut atmosfer gas sekitarnya:

$$\text{Suhu Permukaan Maksimal Peralatan} < \text{Suhu Penyalaan (Ignition Temp) Zat}$$

| T-Class | Suhu Permukaan Maksimum Alat | Tingkat Keketatan Standar |
| :--- | :--- | :--- |
| **T1** | $450^\circ\text{C}$ | Standar terendah |
| **T2** | $300^\circ\text{C}$ | $\downarrow$ |
| **T3** | $200^\circ\text{C}$ | $\downarrow$ |
| **T4** | $135^\circ\text{C}$ | $\downarrow$ |
| **T5** | $100^\circ\text{C}$ | $\downarrow$ Makin ketat |
| **T6** | $85^\circ\text{C}$ | Paling Ketat / Paling Aman |

*(Arah panah: Suhu permukaan maksimum makin rendah $\rightarrow$ proteksi makin ketat).*

#### Independensi Gas Group dan T-Class:
Klasifikasi **Gas Group** dan **T-Class** berdiri sendiri (*independen*):
* **Hidrogen**: Sangat mudah menyala oleh energi percikan kecil (Grup IIC), namun membutuhkan suhu penyalaan termal mandiri yang sangat tinggi ($560^\circ\text{C}$), sehingga cukup menggunakan peralatan kelas **T1**.
* **Karbon Disulfida**: Termasuk Grup IIC, namun memiliki suhu penyalaan sangat rendah ($90^\circ\text{C}$), sehingga menuntut peralatan bersertifikat kelas ketat **T6**.

---

### 8. Dua Ancaman Termal Debu (Group III)
Debu **tidak menggunakan sistem kelas kode T1–T6**. Marking peralatan proteksi debu wajib mencantumkan **nilai suhu aktual langsung** (contoh: $\text{T}125^\circ\text{C}$).

Terdapat 2 skenario bahaya termal debu:
1. **Dust Cloud (Awan Debu)**
   * Kondisi partikel debu melayang tersuspensi di udara (*aerated state*).
   * Syarat Batas:
     $$\text{Suhu Alat} \le \frac{2}{3} \times \text{Suhu Penyalaan Awan (MIT / Cloud Ignition Temp)}$$
2. **Dust Layer (Lapisan Debu Menumpuk $5\text{ mm}$)**
   * Kondisi debu mengendap di atas permukaan peralatan (*compacted layer*) setebal $5\text{ mm}$, membentuk insulasi termal (*thermal insulation*).
   * Syarat Batas:
     $$\text{Suhu Alat} \le (\text{Suhu Penyalaan Lapisan} - 75\text{ K})$$

> **KESIMPULAN METODE PENETAPAN**: Hitung kedua formula kriteria di atas, kemudian ambil nilai batas suhu **TERKECIL** sebagai batas toleransi suhu permukaan maksimum peralatan Anda.

---

### 9. EPL & Konsep Toleransi Gangguan (Fault Tolerance)
EPL (*Equipment Protection Level*) mengukur keandalan peralatan dalam menjamin tidak timbulnya sumber percikan atau bahaya panas:

* **Level "c" (Tingkat Dasar / Normal)**:
  * Kode EPL: **Gc** (Gas), **Dc** (Debu). ATEX: **3G** / **3D**.
  * Tingkat Keandalan: Aman pada saat operasi normal (0 gangguan).
* **Level "b" (Tingkat Tinggi)**:
  * Kode EPL: **Gb** (Gas), **Db** (Debu). ATEX: **2G** / **2D**.
  * Tingkat Keandalan: Aman saat operasi normal ditambah **1 gangguan** independen (*single fault*).
* **Level "a" (Tingkat Sangat Tinggi)**:
  * Kode EPL: **Ga** (Gas), **Da** (Debu). ATEX: **1G** / **1D**.
  * Tingkat Keandalan: Aman saat operasi normal ditambah **2 gangguan** independen (*rare faults / double fault*).

*(Keterangan huruf awal EPL: **G** = Gas, **D** = Debu/Dust, **M** = Tambang/Mines).*

---

### 10. 'Batu Rosetta' Ex: Pemetaan Zona, EPL, dan ATEX
Tabel Konversi Hubungan Zona, EPL (IECEx), dan Kategori (ATEX):

| Zona Gas | Zona Debu | EPL (IECEx) | Kategori (ATEX) | Tingkat Keandalan Peralatan |
| :---: | :---: | :---: | :---: | :---: |
| **0** | **20** | **Ga / Da** | **1G / 1D** | Sangat Tinggi |
| **1** | **21** | **Gb / Db** | **2G / 2D** | Tinggi |
| **2** | **22** | **Gc / Dc** | **3G / 3D** | Dasar / Normal |

* **Penempatan Penulisan**:
  * Kategori ATEX ditulis **sebelum** kata 'Ex' (contoh: `II 2G`).
  * EPL IECEx ditulis **di akhir** rangkaian marking (contoh: `Ex db IIC T4 Gb`).
  * Keduanya menyatakan level keandalan operasional yang sama persis.

---

### 11. Prinsip "Boleh Turun Zona, Tidak Boleh Naik"
Peralatan dengan EPL lebih tinggi (lebih andal) diizinkan dipasang pada zona operasional yang lebih ringan/rendah:
* Peralatan **Ga / 1G**: **Boleh** dipasang di Zona 0, Zona 1, dan Zona 2.
* Peralatan **Gb / 2G**: **Boleh** dipasang di Zona 1 dan Zona 2; **DILARANG KERAS** dipasang di Zona 0.
* Peralatan **Gc / 3G**: **Hanya boleh** dipasang di Zona 2; **DILARANG KERAS** dipasang di Zona 1 dan Zona 0.

> **Tips Lapangan**: Fasilitas industri sering kali menstandarkan pengadaan peralatan pada EPL tingkat tinggi (Gb atau Ga) demi menjaga fleksibilitas dan mempermudah manajemen inventaris suku cadang.

---

### 12. Sintesis Final: 4 Parameter Pemilihan Peralatan
Sebelum menerbitkan *purchase order* atau memasang unit instrumen/listrik, pastikan pemenuhan 4 pilar verifikasi berikut:

1. **[ZONA LINGKUNGAN]** $\rightarrow$ Menentukan $\rightarrow$ **[EPL / KATEGORI MINIMUM]**
   *(Contoh: Terpasang di Zona 1 $\rightarrow$ Butuh minimum Gb / 2G).*
2. **[JENIS ZAT]** $\rightarrow$ Menentukan $\rightarrow$ **[GAS/DUST GROUP MINIMUM]**
   *(Contoh: Zat berupa Hidrogen $\rightarrow$ Butuh sertifikasi IIC).*
3. **[SUHU PENYALAAN ZAT]** $\rightarrow$ Menentukan $\rightarrow$ **[TEMPERATURE CLASS MAKSIMUM]**
   *(Contoh: Suhu penyalaan gas $425^\circ\text{C}$ $\rightarrow$ Butuh rating T2 atau kelas di atasnya seperti T3, T4, T5, T6).*
4. **[KONDISI FISIK AREA]** $\rightarrow$ Menentukan $\rightarrow$ **[METODE PROTEKSI & IP RATING]**
   *(Contoh: Tuntutan *flameproof* `db`, tingkat kedap cuaca luar IP66 — dibahas detail pada Part V).*

Contoh Hasil Pembacaan Pelat Marking Lengkap:
$$\mathbf{Ex\ db\ IIC\ T4\ Gb}$$

> 🔴 **PERINGATAN MUTLAK**: Keempat pilar parameter ini harus saling cocok (*compatible*). Jika ada SATU saja parameter yang tidak memenuhi syarat batas, peralatan tersebut secara teknis dan legal **TIDAK SAH DIGUNAKAN**.

---

## ❓ Antisipasi Pertanyaan Karyawan (FAQ Otomatis)

### Q1: Kenapa tim kita tidak boleh hanya mencantumkan "Kebutuhan Alat: Zona 1" saat mengajukan form pembelian ke Procurement?
**A**: Spesifikasi "Zona 1" baru menjawab pilar EPL minimum (yaitu butuh Gb atau 2G). Tim pengadaan dan vendor masih membutuhkan jenis gas/zat (IIA/IIB/IIC) untuk toleransi celah percikan, serta kelas suhu (T1–T6) agar suhu alat tidak memicu ledakan mandiri. Tanpa T-Class dan Gas Group yang jelas, alat yang dibeli berisiko salah spesifikasi dan ditolak saat inspeksi HSE.

### Q2: Jika di pabrik kita terdapat gas propana (Grup IIA), apakah kita boleh memasang sensor yang memiliki label IIC?
**A**: Boleh. Berlaku prinsip inklusif menaik: rating IIC dirancang untuk gas yang paling sulit diproteksi (seperti Hidrogen). Oleh karena itu, peralatan berlabel IIC otomatis aman dan kompatibel digunakan untuk atmosfer gas IIB dan IIA.

### Q3: Apakah peralatan berlabel gas T6 otomatis aman digunakan untuk semua jenis gas Group IIC?
**A**: Ya, dari segi suhu permukaan alat T6 adalah yang paling aman dan dingin (maksimal $85^\circ\text{C}$), sehingga tidak akan menyulut gas dengan suhu penyalaan rendah seperti Karbon Disulfida sekalipun. Namun, tetap pastikan label Gas Group-nya juga mencantumkan sertifikasi IIC (bukan IIA atau IIB saja), karena T-Class dan Gas Group adalah dua parameter independen.

### Q4: Mengapa penandaan suhu pada area debu (Group III) tidak memakai kode T1 sampai T6 seperti pada gas?
**A**: Karakteristik bahaya debu sangat dipengaruhi oleh ketebalan akumulasi lapisan debu (*layer*) yang memicu efek insulasi panas, serta kerapatan awan debu (*cloud*). Oleh sebab itu, standar IEC mengharuskan pencantuman angka suhu batas permukaan aktual langsung (misalnya $\text{T}125^\circ\text{C}$), yang dihitung dari nilai terkecil antara $\frac{2}{3}$ Suhu Penyalaan Awan (*MIT*) atau (Suhu Penyalaan Lapisan dikurangi batas aman $75\text{ K}$).

### Q5: Bolehkan kita menggunakan transmitter cadangan bersertifikat Ga di area yang diklasifikasikan sebagai Zona 1 atau Zona 2?
**A**: Boleh. Berdasarkan aturan "Boleh Turun Zona, Tidak Boleh Naik", peralatan dengan EPL Ga (Kategori ATEX 1G) memiliki toleransi kerusakan sangat tinggi (aman hingga 2 gangguan independen), sehingga sangat aman diturunkan untuk instalasi di Zona 1 maupun Zona 2.

---

## 📚 Glosarium & Istilah Penting

* **ATEX (*Atmosphères Explosibles*)**: Arahan regulasi wajib Uni Eropa mengenai standardisasi keselamatan peralatan dan lingkungan kerja yang berpotensi ledakan.
* **IEC 60079**: Kumpulan standar teknis internasional dari IEC (*International Electrotechnical Commission*) yang mengatur persyaratan peralatan listrik dan non-listrik di atmosfer ledakan gas dan debu.
* **EPL (*Equipment Protection Level*)**: Tingkat proteksi peralatan yang dialokasikan berdasarkan risiko dan toleransi peralatan terhadap kemungkinan menjadi sumber penyalaan ledakan (Ga, Gb, Gc untuk Gas; Da, Db, Dc untuk Debu).
* **MESG (*Maximum Experimental Safe Gap*)**: Celah transmisi maksimum terukur antara dua permukaan sambungan logam ruang uji standar yang mampu mencegah penjalaran api ledakan dari dalam ke atmosfer gas di sekitarnya.
* **MIC (*Minimum Igniting Current*) Ratio**: Rasio perbandingan arus listrik minimum yang dibutuhkan suatu gas/uap untuk menyala akibat percikan busur listrik relatif terhadap gas metana.
* **Combustible Flyings (IIIA)**: Partikel serat padat mudah terbakar yang melayang di udara dengan ukuran penampang partikel lebih besar dari $500\ \mu\text{m}$.
* **Conductive Dust (IIIC)**: Partikel debu halus dengan nilai resistivitas listrik rendah ($\le 10^3\ \Omega\cdot\text{m}$) yang mampu menghantarkan arus listrik dan memicu hubungan pendek.
* **T-Class (*Temperature Class*)**: Sistem klasifikasi batas temperatur permukaan terluar peralatan listrik (T1 hingga T6) saat beroperasi pada beban penuh dalam rentang suhu ambien standar.