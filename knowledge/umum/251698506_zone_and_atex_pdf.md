---
sumber_dokumen: "251698506-Zone-and-ATEX-pdf.pdf"
gdrive_file_id: "1H-4PlEVK3J-_JZILfxD3pMUzGTuUTpcN"
gdrive_modified_time: "2026-07-21T16:34:58.432Z"
folder_asal: "Root Knowledge / ATEX & Ex Knowledge"
tanggal_ekstraksi: "2026-10-15"
tingkat_akses: "SEMUA_MEMBER"
---

# Panduan Komprehensif ATEX Ratings, Intrinsic Safety, Hazardous Areas, dan Explosive Atmospheres

## 📌 Executive Summary

* **Klasifikasi Area Berbahaya (Zonasi vs Divisi):** Standar Eropa/IEC mengklasifikasikan area gas menjadi Zone 0, Zone 1, dan Zone 2, serta area debu menjadi Zone 20, Zone 21, dan Zone 22 berdasarkan frekuensi dan durasi keberadaan atmosfer eksplosif. Standar Amerika Utara (NEC/NFPA) membaginya menjadi Class I, II, III dengan sistem Division 1 dan Division 2.
* **Tingkat Perlindungan dan Metode Proteksi Peralatan (Ex):** Peralatan listrik di area berbahaya dilindungi menggunakan berbagai konsep proteksi terstandarisasi, antara lain *Flameproof* (`d`), *Increased Safety* (`e`), *Intrinsic Safety* (`ia`/`ib`/`ic`), *Pressurised* (`p`), *Encapsulation* (`m`), *Oil Immersion* (`o`), *Powder Filling* (`q`), serta konsep ganda (*multiple protection*, misal `EEx de`).
* **Pengelompokan Gas dan Karakteristik Temperatur:** Gas dibagi menjadi Grup I (tambang bawah tanah) dan Grup II (industri permukaan: IIA/Propana, IIB/Etilena, IIC/Hidrogen/Asetilena sebagai kelompok paling mudah meledak). Kelas suhu diatur dari T1 (maks. 450°C) hingga T6 (maks. 85°C), di mana suhu permukaan peralatan tidak boleh melebihi 80% dari suhu penyalaan mandiri (*auto-ignition temperature*) gas terkait.
* **Transisi Regulasi Directive ATEX:** Direktif perlindungan peralatan ATEX 94/9/EC digantikan secara resmi oleh Direktif baru 2014/34/EU (efektif penuh sejak 20 April 2016).
* **Standar Pelabelan dan Verifikasi:** Peralatan ATEX/IECEx wajib memiliki penandaan heksagonal 'Ex', nomor *Notified Body* (misalnya Baseefa, Sira), grup peralatan, kategori, kode proteksi, grup gas, serta kelas temperatur. Di Amerika Utara, sertifikasi harus diterbitkan oleh laboratorium uji NRTL (seperti UL, FM, CSA, MET, Intertek).

---

## 📖 Salinan Lengkap & Terstruktur

### 1. Ringkasan Konsep Proteksi dan Zonasi (ATEX / IEC)

#### Konsep Proteksi Berdasarkan Zona Gas

| Zone | Hazard (Tingkat Bahaya) | Protection Concepts (Konsep Proteksi) |
| :--- | :--- | :--- |
| **0** | Campuran gas/udara eksplosif hadir secara terus-menerus (*continuously present*) untuk periode yang lama. | `Exia` atau `Exs` |
| **1** | Campuran gas/udara eksplosif berpotensi muncul dalam operasi normal (*likely to occur in normal operation*). | `Exd`, `Exe`, `Exib`, `Exp`, `Exia`, `Exs` |
| **2** | Campuran gas/udara eksplosif tidak mungkin muncul dalam operasi normal (*not likely to occur*), dan jika terjadi hanya sesaat. | Semua konsep yang cocok untuk Zone 0 & 1, ditambah `ExN`, `ExO`, dan `Exq` |

#### Standar Metode Proteksi (*Standards for Methods of Protection*)

| Method of Protection | Permitted Zone of Use in UK | Code Letter (IEC, EX.., CENELEC, EEX) |
| :--- | :--- | :--- |
| General requirement | - | - |
| Oil immersion | 2 | `o` |
| Pressurisation | 1 or 2 | `p` |
| Powder filling | 2 | `q` |
| Flameproof | 1 or 2 | `d` |
| Increased safety | 1 or 2 | `e` |
| Intrinsic safety | \* 0, 1 or 2 | `ia` or `ib` |
| Non-incendive | 2 | `n` # |
| Encapsulation | 1 or 2 | `m` |
| Special | 1 or 2 | `s` |

*\* Catatan:* 
* `ia`: Zone 0, 1, 2
* `ib`: Zone 1 or 2 (tidak boleh untuk Zone 0)
* `# n`: Digunakan secara lokal di UK

---

### 2. Pengelompokan Gas dan Klasifikasi Temperatur

#### Gas Grouping & Temperature Classification

| Gas # Group (CENELEC EN 5014, IEC) | Representative Gas | T Class / IEC 79-7 | Max. Surface Temp (°C) |
| :--- | :--- | :--- | :--- |
| **I\*** *(mining)* | Methane | **T1** | 450°C |
| **IIA** | Propane | **T2** | 300°C |
| **IIB** | Ethylene | **T3** | 200°C |
| **IIC** | Hydrogen | **T4** | 135°C |
| - | - | **T5** | 100°C |
| - | - | **T6** | 85°C |

---

### 3. Struktur Kode Sertifikasi (CENELEC Marking Information)

Contoh Penandaan: **`[EEx ia] IIC T4`**

| Elemen | Arti / Penjelasan |
| :--- | :--- |
| **`[`** | Associated apparatus\* |
| **`E`** | Certified to the CENELEC standard |
| **`Ex`** | Explosion protected |
| **`ia`** | Protection concept (Intrinsic Safety) |
| **`]`** | Associated apparatus\* |
| **`IIC`** | Apparatus group (gas group) |
| **`T4`** | Temperature classification (not Gp I) |

*\* Catatan:* Tanda kurung siku `[ ... ]` menandakan *associated apparatus* (berada di area aman (*safe area*) dan terhubung ke sirkuit di area berbahaya).

---

### 4. Grup Peralatan dan Kategori (*Device Group & Category*)

| Device Group | Device Category | Zone Kesesuaian |
| :--- | :--- | :--- |
| **Group I**<br>Mining (Pit Gas &/or Flammable Dusts) | **M = Mining**<br>• M 1<br>• M 2 | -<br>-<br>- |
| **Group II**<br>Other areas (Explosive Atmosphere) | **G = Gas**<br>• 1 G<br>• 2 G<br>• 3 G | <br>0, 1, 2<br>1, 2<br>2 |
| *D is added after G in the certification class number (i.e. GD) if device is dust category approved also* | **D = Dust**<br>• 1 D<br>• 2 D<br>• 3 D | <br>20, 21, 22<br>21, 22<br>22 |

#### Penjelasan Kategori Peralatan:
* **Category 1 (Very high safety):** Keamanan perangkat harus terjamin bahkan jika terjadi kegagalan langka pada perangkat (*rare device failures*), misalnya kegagalan simultan dari dua komponen independen.
* **Category 2 (High safety):** Keamanan perangkat harus terjamin jika sering terjadi kegagalan yang dapat diantisipasi (*frequent failures*), misalnya kegagalan satu komponen.
* **Category 3 (Safe in normal operation):** Keamanan perangkat terjamin dalam operasi normal.

*Catatan:* Angka dalam tanda kurung sebelum penunjukan kategori menandakan bahwa perangkat memenuhi persyaratan kategori tambahan dari kategori utama yang ditentukan.  
*Contoh:* `II (1) 2G` mengartikan bahwa perangkat memenuhi persyaratan untuk `1 G` sekaligus `2 G`.

---

### 5. Karakteristik Substansi & Material

* **Flashpoint (Titik Nyala):** Suhu terendah di mana suatu cairan menghasilkan uap yang cukup untuk mendukung penyalaan (*ignition*). Uap ini dapat menyala oleh suhu tinggi atau energi (seperti percikan api).
* **Ignition Temperature (Suhu Penyalaan):** Suhu terendah di mana uap akan menyala dengan sendirinya (*ignited*). Karakteristik ini mendefinisikan batas kelas temperatur peralatan.

#### Klasifikasi Suhu Permukaan Maksimum Peralatan Listrik (CENELEC):
* **T1:** < 450°C
* **T2:** < 300°C
* **T3:** < 200°C
* **T4:** < 135°C
* **T5:** < 100°C
* **T6:** < 85°C

#### Pembagian Energi Penyalaan Grup Peralatan (*Apparatus Group Energy Ignition*):
Semua gas/uap industri permukaan diklasifikasikan sebagai gas Group II, yang terbagi dalam 3 sub-grup:
* **IIA:** Membutuhkan energi tinggi untuk menyala. Daya ledak kurang intens (*Less intense explosion*). Gas referensi: Propana (*Propane*).
* **IIB:** Membutuhkan energi sedang untuk menyala. Daya ledak lebih kuat (*More intense explosion*). Gas referensi: Etilena (*Ethylene*).
* **IIC:** Membutuhkan energi sangat kecil untuk menyala. Daya ledak paling dahsyat (*Most intense explosion*). Gas referensi: Hidrogen (*Hydrogen*).

#### Karakteristik Sejumlah Material Mudah Terbakar yang Umum:

| Gas / Vapour | Flashpoint | Gas Group | Ignition Temp. | Temp. Class |
| :--- | :--- | :--- | :--- | :--- |
| **Acetone** | 19°C | IIA | 535°C | T1 |
| **Butane** | -60°C | IIA | 365°C | T2 |
| **Heptane** | -4°C | IIA | 215°C | T3 |
| **Ethyl Methyl Ether** | 37°C | IIB | 190°C | T4 |

*Catatan Penting:* Tidak ada korelasi langsung antara energi penyalaan (*ignition energy*) dan suhu penyalaan (*ignition temperature*).

---

### 6. Deskripsi Area Menurut Standar ANSI / NFPA (Amerika Utara)

* **Class I, Div. 1:** Area di mana konsentrasi gas, uap, atau cairan yang mudah terbakar berada dalam konsentrasi yang dapat menyala secara terus-menerus atau sering kali dalam kondisi operasi normal.
* **Class I, Div. 2:** Area di mana konsentrasi gas, uap, atau cairan yang mudah terbakar berada dalam konsentrasi yang dapat menyala hanya dalam kondisi operasi abnormal.
* **Class II, Div. 1:** Area di mana konsentrasi debu yang mudah terbakar (*combustible dusts*) berada dalam atmosfer dalam kondisi operasi normal.
* **Class II, Div. 2:** Area di mana konsentrasi debu yang mudah terbakar berada dalam atmosfer hanya dalam kondisi operasi abnormal.
* **Class III, Div. 1:** Area di mana serat yang mudah menyala (*easily ignitable fibers*) atau material pembawa partikel melayang mudah terbakar (*combustible flyings*) berada dalam kondisi operasi normal.
* **Class III, Div. 2:** Area di mana serat yang mudah menyala atau partikel melayang berada di bawah kondisi operasi abnormal.

#### Klasifikasi Grup Material Menurut Standar ANSI/NFPA:
* **Class I Areas:**
  * **Group A:** Acetylene
  * **Group B:** Hydrogen
  * **Group C:** Propane and Ethylene
  * **Group D:** Benzene, Butane, Methane & Propane
* **Class II Areas:**
  * **Group E:** Metal Dust
  * **Group F:** Carbon & Charcoal
  * **Group G:** Flour, Starch, Wood & Plastic
* **Class III Areas:**
  * **NO GROUP:** Cotton & Sawdust

*(Referensi lebih lanjut: Article 500 of NFPA 70 - The National Electric Code / NEC).*

---

### 7. Perbandingan Klasifikasi Area: IEC/Eropa vs. NEC/ANSI

| European and IEC Classification | Definisi Zona atau Divisi | North American Classification (NEC/ANSI) |
| :--- | :--- | :--- |
| **Zone 0 (gases / Vapors)** | Area di mana campuran eksplosif hadir secara terus-menerus atau untuk periode lama (> 1000 jam/tahun atau > 10% waktu operasi). | **Class I Division 1** (gases) |
| **Zone 1 (gases / Vapors)** | Area di mana campuran eksplosif berpotensi muncul dalam operasi normal (10 – 1000 jam/tahun atau 0.1 – 10% waktu operasi). | **Class I Division 1** (gases) |
| **Zone 2 (gases / Vapors)** | Area di mana campuran eksplosif tidak mungkin terjadi dalam operasi normal, dan jika terjadi hanya berlangsung singkat (< 10 jam/tahun atau 0 – 0.1% waktu operasi). | **Class I Division 2** (gases) |
| **Zone 20 (dusts)** | Area di mana campuran debu eksplosif hadir terus-menerus atau untuk periode yang lama. | **Class II Division 1** (dusts) |
| **Zone 21 (dusts)** | Area di mana campuran debu eksplosif berpotensi muncul dalam operasi normal. | **Class II Division 1** (dusts) |
| **Zone 22 (dusts)** | Area di mana campuran debu eksplosif tidak mungkin terjadi dalam operasi normal, dan jika terjadi hanya berlangsung singkat. | **Class II Division 2** (dusts) |

---

### 8. Peralatan Listrik di Area Berbahaya (*Electrical Equipment in Hazardous Areas*)

#### Bahaya Percikan Listrik (*Electrical Ignition Hazard*)
Sakelar lampu rumah tangga dapat menghasilkan percikan api kecil yang tidak berbahaya di udara normal. Namun, di fasilitas kimia atau kilang minyak, percikan tersebut dapat memicu ledakan besar. Peralatan listrik untuk area berbahaya dirancang untuk menahan ledakan di dalam wadah (*contain*), atau dirancang agar energinya tidak cukup untuk memicu penyalaan (*prevent spark/thermal ignition*).

Strategi penanganan keselamatan instalasi:
1. Menempatkan peralatan di luar area berbahaya (*safe area*).
2. Memperbaiki ventilasi udara bersih agar konsentrasi uap berbahaya encer di bawah 25% LEL (*Lower Explosive Limit*).
3. Menggunakan konsep *Intrinsic Safety* (daya rendah dan penyimpanan energi dibatasi).
4. Menjaga selungkup bertekanan positif (*positive pressure pressurisation*) menggunakan udara bersih atau gas inert.
5. Mengisolasi elemen pembakar dari atmosfer sekitar melalui metode *encapsulation*, pencelupan oli (*oil immersion*), atau pasir/kuarsa.
6. Membatasi suhu permukaan peralatan di bawah suhu *auto-ignition* bahan kimia terkait.

#### Sejarah Singkat
Setelah listrik mulai diperkenalkan ke tambang batu bara, ledakan mematikan kerap dipicu oleh peralatan listrik seperti lampu, sinyal, atau motor karena keberadaan gas metana (*firedamp*) dan debu batu bara. Sedikitnya dua insiden ledakan tambang di Inggris disebabkan oleh sistem bel sinyal listrik kawat terbuka: induksi koil bel sinyal yang terputus menghasilkan percikan listrik yang menyalakan metana.

---

### 9. Equipment Protection Level (EPL)

Standar modern menetapkan tingkat perlindungan peralatan (*Equipment Protection Level* / EPL) berdasarkan zona dan tingkat risiko:

| Group | Ex Risk | Zone | EPL | Minimum Type of Protection |
| :--- | :--- | :--- | :--- | :--- |
| **I (mines)** | energized | - | **Ma** | - |
| **I (mines)** | de-energized in presence of Ex atmosphere | - | **Mb** | - |
| **II (gas)** | explosive atmosphere > 1000 hrs/yr | 0 | **Ga** | `ia`, `ma` |
| **II (gas)** | explosive atmosphere between 10 and 1000 hrs/yr | 1 | **Gb** | `ib`, `mb`, `px`, `py`, `e`, `o`, `q`, `s` |
| **II (gas)** | explosive atmosphere between 1 and 10 hrs/yr | 2 | **Gc** | `n`, `ic`, `pz` |
| **III (dust)**| explosive surface > 1000 hrs/yr | 20 | **Da** | `ia` |
| **III (dust)**| explosive surface between 10 and 1000 hrs/yr | 21 | **Db** | `ib` |
| **III (dust)**| explosive surface between 1 and 10 hrs/yr | 22 | **Dc** | `ic` |

---

### 10. Klasifikasi Temperatur dan Titik *Auto-Ignition*

Suhu permukaan peralatan listrik tidak boleh melampaui **80%** dari suhu *auto-ignition* gas atau uap spesifik di area penempatan.

#### Perbandingan Skala Temperatur Operasi Internasional

| USA (°C) | USA (°C) | International (IEC) (°C) | Germany (°C) Continuous - Short Time |
| :--- | :--- | :--- | :--- |
| **T1** - 450 | **T3A** - 180 | **T1** - 450 | **G1**: 360 - 400 |
| **T2** - 300 | **T3B** - 165 | **T2** - 300 | **G2**: 240 - 270 |
| **T2A** - 280 | **T3C** - 160 | **T3** - 200 | **G3**: 160 - 180 |
| **T2B** - 260 | **T4** - 135 | **T4** - 135 | **G4**: 110 - 125 |
| **T2C** - 230 | **T4A** - 120 | **T5** - 100 | **G5**: 80 - 90 |
| **T2D** - 215 | **T5** - 100 | **T6** - 85 | - |
| **T3** - 200 | **T6** - 85 | - | - |

#### Daftar Suhu Auto-Ignition Gas Umum:
* **Methane:** 580°C
* **Hydrogen:** 560°C
* **Propane:** 493°C
* **Ethylene:** 425°C
* **Acetylene:** 305°C
* **Naphtha:** 290°C
* **Carbon disulfide:** 102°C

#### Daftar Suhu Auto-Ignition Debu (*Dust*):
* **Sugar:** 460°C
* **Wood:** 340°C
* **Flour:** 340°C
* **Grain dust:** 300°C
* **Tea:** 300°C

---

### 11. Jenis-Jenis Metode Proteksi (*Types of Protection*)

> ⚠️ **Catatan Regulasi ATEX:** Direktif perlindungan peralatan lama **ATEX 94/9/EC** sudah tidak berlaku sejak **20 April 2016**, dan digantikan oleh direktif baru **2014/34/EU** yang disahkan oleh Parlemen Eropa pada 29 Maret 2014.

| Ex Code | Deskripsi Metode | Standar | Lokasi Zona | Contoh Penggunaan |
| :---: | :--- | :--- | :--- | :--- |
| **Flameproof (`d`)** | Konstruksi peralatan dirancang untuk menahan ledakan internal dan membuang tekanan gas keluar melalui *flamepath/flamegap* (celah ulir/flensa). Gas yang keluar didinginkan agar suhunya tidak lagi mampu memicu ledakan di atmosfer sekitar.<br>• Max flamegap: 0.006" (150 µm) untuk propana/etilena; 0.004" (100 µm) untuk asetilena/hidrogen. | IEC/EN 60079-1 | Zone 1 (jika grup gas & kelas suhu sesuai) | Motor listrik, lampu (*lighting*), kotak sambungan (*junction box*), komponen elektronik. |
| **Increased Safety (`e`)** | Peralatan dirancang sangat kokoh dengan komponen berkualitas tinggi guna meminimalkan risiko busur listrik atau panas berlebih. | IEC/EN 60079-7 | Zone 2 or Zone 1 | Motor listrik, lampu, kotak sambungan. |
| **Oil Filled (`o`)** | Komponen listrik terendam sepenuhnya di dalam minyak isolasi untuk memutus kontak dengan atmosfer luar. | IEC/EN 60079-6 | Zone 2 or Zone 1 | *Switchgear* tegangan tinggi. |
| **Sand/Powder/ Quartz Filled (`q`)** | Komponen listrik tertutup rapat oleh lapisan pasir atau kuarsa guna mencegah penyebaran nyala api. | IEC/EN 60079-5 | Zone 2 or Zone 1 | Perangkat elektronik, telepon, *chokes*. |
| **Encapsulated (`m`)** | Komponen listrik dicor (*resin encapsulation*) sehingga uap atau gas eksplosif tidak dapat bersentuhan dengan komponen panas/berpercikan. | IEC/EN 60079-18 | Zone 1 (Ex mb) atau Zone 0 (Ex ma) | Rangkaian elektronik (yang tidak menghasilkan panas berlebih). |
| **Pressurised / Purged (`p`)** | Selungkup peralatan diberi tekanan positif (*overpressure*) menggunakan udara bersih atau gas inert sehingga gas berbahaya tidak dapat masuk. Tekanan dipantau terus-menerus. | IEC/EN 60079-2 | Zone 1 (`px` or `py`), atau Zone 2 (`pz`) | Alat analisis kimia (*analysers*), motor besar, ruang panel kontrol, komputer industri. |
| **Intrinsically Safe (`i`)** | Energi listrik dan termal dibatasi sangat rendah sehingga percikan atau panas tidak mampu memantik ledakan uap.<br>Memerlukan *Zener Barrier* atau *Galvanic Isolator* di sirkuitnya. Enclosure minimal IP54.<br>Mencakup konsep Fieldbus FISCO (Zone 0, 1, atau 2). | IEC/EN 60079-25<br>IEC/EN 60079-11<br>IEC/EN 60079-27 | • `ia`: Zone 0 & 1<br>• `ib`: Zone 1<br>• `ic`: Zone 2 | Instrumentasi, sensor industri, transmitter, perangkat kontrol instrumentasi. |
| **Non Incendive (`n`)** | Peralatan bersifat non-incendive atau tidak memicu percikan (*non-sparking*) dalam operasi normal. Mengakomodasi konsep FNICO (*Fieldbus Non-Incendive Concept*). | IEC/EN 60079-15<br>IEC/EN 60079-27 | Zone 2 | Motor listrik, lampu, kotak sambungan, peralatan elektronik. |
| **Special Protection (`s`)** | Metode khusus yang tidak memiliki aturan spesifik baku, tetapi telah terbukti secara pengujian memiliki tingkat keselamatan setara standar yang dipersyaratkan. | IEC/EN 60079-33 | Tergantung sertifikasi pabrikan (*As its certification states*) | Sesuai spesifikasi sertifikasi masing-masing manufaktur. |

#### Konsep Proteksi Ganda (*Multiple Protection*)
Banyak peralatan bersertifikasi mengombinasikan lebih dari satu metode proteksi pada unit yang sama. Sebagai contoh, sebuah soket kontak dapat diberi label **`EEx de`**, yang berarti wadah penutup luarnya memakai konsep *Increased Safety* (`e`), sementara sakelar internalnya menggunakan konsep *Flameproof* (`d`).

---

### 12. Regulasi dan Standar Pelabelan (*Labeling*)

#### Wilayah Eropa (ATEX / CENELEC / IECEx)
Label peralatan di Eropa wajib mencantumkan tanda CE dan kode lembaga sertifikasi penguji (*Notified Body*, misal Sira, Baseefa). Penandaan wajib mencakup simbol heksagonal **Ex**, diikuti grup peralatan, kategori, dan penanda atmosfer:
* **`Ex II 1 G`**: Peralatan Group II (non-tambang), Kategori 1 (keselamatan sangat tinggi), untuk gas (G).
* **`EEx ia IIC T4`**: Sertifikasi CENELEC (`E`), Explosion protected (`Ex`), Intrinsically safe (`ia`), Gas Group `IIC`, Kelas Temperatur `T4` (maks. 135°C).
* **`EEx nA II T3 X`**: Tipe proteksi non-sparking (`nA`), Group II, Kelas Temperatur `T3`, dengan kondisi penggunaan khusus (`X`).

#### Wilayah Amerika Utara (NEC / NFPA / OSHA)
Peralatan wajib diuji oleh *Nationally Recognized Testing Laboratory* (NRTL) independen seperti **UL, MET, FM, CSA**, atau **Intertek (ETL)**.
Label mencantumkan:
* Class (Class I, II, atau III)
* Division (Division 1 atau Division 2)
* Gas/Material Group (Grup A, B, C, D, E, F, atau G)
* Temperature Identification Number (T-Code)
* Tanda registrasi lembaga uji lab (listing mark)
* Nama manufaktur, tipe model, nomor seri, dan tahun pembuatan.

---

## ❓ Antisipasi Pertanyaan Karyawan (FAQ Otomatis)

### Q1: Apa perbedaan utama antara perlindungan Flameproof (`Ex d`) dan Intrinsic Safety (`Ex ia`)?
**A:** *Flameproof* (`Ex d`) mengizinkan terjadinya ledakan kecil di dalam bodi/selungkup perangkat jika ada gas yang merembes masuk, namun bodinya dirancang super tebal dan celah sambungannya (*flamepath*) cukup rapat untuk mendinginkan api sebelum bisa menyambar gas di luar. Sedangkan *Intrinsic Safety* (`Ex ia`) bekerja dengan cara membatasi tegangan, arus, dan energi listrik/panas ke tingkat yang sedemikian rendah sehingga mustahil memantik percikan api atau memanaskan permukaan hingga memicu ledakan, bahkan jika dua komponen mengalami kerusakan simultan.

### Q2: Jika kita memiliki perangkat bersertifikasi gas grup IIC, apakah boleh dipasang di area dengan kandungan gas Propana (IIA)?
**A:** Boleh. Pengelompokan gas grup II bersifat menurun tingkat keparahannya: **IIC > IIB > IIA**. Grup IIC adalah kategori gas yang paling mudah terbakar dengan energi penyalaan terkecil (seperti Hidrogen/Asetilena). Maka, perangkat dengan sertifikasi IIC secara otomatis mencakup dan aman digunakan untuk lingkungan gas IIB maupun IIA. Kebalikannya tidak berlaku (perangkat bertanda IIA tidak boleh dipasang di area IIC).

### Q3: Kenapa direktif ATEX lama 94/9/EC sudah tidak dipakai lagi dan diganti ke 2014/34/EU?
**A:** Uni Eropa memperbarui kerangka regulasi harmonisasi teknisnya (*New Legislative Framework*). Sejak tanggal 20 April 2016, direktif 94/9/EC ditarik dan secara resmi digantikan oleh direktif **2014/34/EU**. Perubahan ini memperjelas kewajiban importir, distributor, serta memperketat pengawasan pasar terhadap Notified Body yang mengeluarkan sertifikasi ATEX.

### Q4: Apa arti tanda kurung siku pada sertifikasi peralatan, misalnya `[EEx ia] IIC`?
**A:** Tanda kurung siku mengindikasikan bahwa unit tersebut adalah *Associated Apparatus* (misalnya *Zener Barrier* atau isolator sinyal). Perangkat ini wajib dipasang di area aman (*Safe / Non-Hazardous Area*), namun memiliki terminal kabel keluaran yang terhubung langsung ke sirkuit instrumen yang berada di dalam area berbahaya (Zone 0/1).

### Q5: Apakah Class I Division 1 pada standar Amerika sama persis dengan Zone 1 pada standar Eropa?
**A:** Tidak persis sama. Dalam standar Amerika Utara, **Class I Division 1** mencakup kondisi di mana gas berbahaya ada secara terus-menerus (Zone 0) DAN kondisi di mana gas berpotensi hadir saat operasi normal (Zone 1). Standar IEC/Eropa memisahkan keduanya menjadi Zone 0 (>1000 jam/tahun) dan Zone 1 (10–1000 jam/tahun) agar pemilihan perangkat proteksi dapat lebih presisi dan efisien secara biaya.

---

## 📚 Glosarium & Istilah Penting

* **ATEX:** *Appareils destinés à être utilisés en ATmosphères EXplosibles* — Kerangka hukum dan direktif wajib Uni Eropa yang mengatur persyaratan keselamatan peralatan di lingkungan rawan ledakan.
* **Auto-Ignition Temperature:** Suhu minimum di mana uap atau gas akan menyala spontan tanpa bantuan percikan api eksternal.
* **CENELEC:** *European Committee for Electrotechnical Standardization* — Komite standardisasi elektroteknik Eropa penyusun standar EN 60079.
* **EPL (Equipment Protection Level):** Tingkat proteksi peralatan (Ga, Gb, Gc / Da, Db, Dc / Ma, Mb) yang ditetapkan standar IEC untuk menentukan kesesuaian unit terhadap risiko zona spesifik.
* **Flashpoint:** Titik suhu terendah suatu zat cair untuk menghasilkan uap yang dapat tersulut api.
* **Flamegap:** Celah mekanis terukur pada selungkup peralatan *flameproof* yang berfungsi meredam dan mendinginkan gas hasil ledakan internal sebelum keluar ke atmosfer bebas.
* **LEL (Lower Explosive Limit):** Konsentrasi minimum uap bahan bakar di udara yang dapat menghasilkan ledakan jika tersulut api.
* **Notified Body:** Lembaga pengujian independen yang ditunjuk secara resmi di Uni Eropa (seperti Baseefa, Sira) untuk melakukan audit, pengujian tipe, dan menerbitkan sertifikat ATEX.
* **Zener Barrier:** Komponen pembatas energi berbasis dioda Zener, resistor, dan sekering yang digunakan pada sistem *Intrinsically Safe* untuk mencegah arus/tegangan berlebih masuk ke area berbahaya.