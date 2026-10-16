---
sumber_dokumen: "710477444-BS-60079-10-1-2015-Explosive-atmospheres-Part-10-1.pdf"
gdrive_file_id: "1KE90SbwOAsWFo8Y1Tf7zxhZ51jTW4P48"
gdrive_modified_time: "2026-07-20T08:17:39.000Z"
folder_asal: "Root Knowledge / ATEX & Ex Knowledge"
tanggal_ekstraksi: "2026-10-16"
tingkat_akses: "SEMUA_MEMBER"
---

# BS EN 60079-10-1:2015 — Explosive Atmospheres — Part 10-1: Classification of Areas — Explosive Gas Atmospheres

## 📌 Executive Summary

* **Tujuan & Ruang Lingkup:** Standar ini mengatur metodologi identifikasi, evaluasi, dan klasifikasi area berbahaya (*hazardous area classification*) di mana uap atau gas mudah terbakar dapat terbentuk di udara, guna memandu pemilihan dan instalasi peralatan Ex (*explosion-protected*) yang aman dan tepat.
* **Klasifikasi Zona Berdasarkan Probabilitas:** Membagi area menjadi Zona 0 (*continuous/long periods/frequently*), Zona 1 (*likely in normal operation*), Zona 2 (*not likely and for short duration only*), serta konsep Zona NE (*Negligible Extent*) di mana volume gas sangat kecil sehingga dampak ledakannya dapat diabaikan.
* **Peran Kunci Ventilasi & Pengenceran (*Dilution*):** Efektivitas ventilasi (*high, medium, low*) dan ketersediaan ventilasi (*good, fair, poor*) secara fundamental menentukan atau menurunkan tingkat keparahan zona (misal: mereduksi Zona 1 menjadi Zona 2 atau Non-hazardous).
* **Pendekatan Kuantitatif Sumber Lepasan (*Sources of Release*):** Menyediakan formulasi matematis untuk menghitung laju lepasan (*release rate* $W_g$), penguapan kolam cairan (*pool evaporation* $W_e$), konsentrasi latar belakang (*background concentration* $X_b$), serta penentuan jarak berbahaya (*hazardous distance* $r$) menggunakan kurva karakteristik lepasan.
* **Dokumentasi Lengkap:** Mensyaratkan dokumen klasifikasi area sebagai dokumen hidup (*living document*), yang mencakup *Hazardous Area Classification Data Sheets* (Daftar Substansi dan Daftar Sumber Lepasan) serta gambar layout (*elevation and plan drawings*) bertanda simbol zona standar.

---

## 📖 Salinan Lengkap & Terstruktur

### 1. Informasi Standar & Foreword

* **Identifikasi Dokumen:** BS EN 60079-10-1:2015 (Menggabungkan *corrigendum* Desember 2016). Identik dengan IEC 60079-10-1:2015 + COR1:2015.
* **Penggantian:** Menggantikan BS EN 60079-10-1:2009 yang telah ditarik (*withdrawn*).
* **Catatan Komite Nasional Inggris (BSI / UK Committee):**
  * Komite UK memberikan catatan kritis terhadap metodologi dalam Annex C dan Annex D, menyarankan pengguna mempertimbangkan bahwa laju ventilasi (*ventilation rate/volume air per unit time*) relatif terhadap laju pelepasan zat adalah penentu utama pengenceran, sedangkan *ventilation velocity* hanya memiliki efek sekunder.
  * Klasifikasi Zona 2 NE disarankan dibatasi untuk sumber tekanan kurang dari 10 barg sesuai panduan industri.
  * Penguapan kolam hidrokarbon volatil disarankan divalidasi silang dengan standar industri spesifik untuk memastikan prinsip ALARP (*as low as reasonably practicable*).

---

### 2. Ruang Lingkup (Clause 1 - Scope)

Standar ini berlaku untuk klasifikasi area di mana bahaya gas atau uap mudah terbakar dapat timbul bersama udara pada kondisi atmosfer standar:
* Tekanan atmosfer referensi: $101{,}3\text{ kPa}$ ($1\,013\text{ mbar}$).
* Suhu referensi: $20^\circ\text{C}$ ($293\text{ K}$).

**Pengecualian (Tidak berlaku untuk):**
1. Tambang bawah tanah yang rentan terhadap gas tambang (*firedamp*).
2. Pemrosesan dan pembuatan bahan peledak (*explosives*).
3. Kegagalan katastropik (*catastrophic failures*) atau malafungsi langka di luar batas abnormal yang wajar (misal: pecahnya bejana tekan total).
4. Ruangan untuk keperluan medis.
5. Pemanfaatan gas bahan bakar bertekanan rendah komersial dan domestik (misal: kompor, pemanas air) yang tunduk pada kode gas relevan.
6. Premis domestik/rumah tangga.
7. Bahaya debu atau serat mudah terbakar (diatur dalam IEC 60079-10-2), namun prinsipnya dapat digunakan untuk analisis campuran hibrida (*hybrid mixtures*).

---

### 3. Istilah dan Definisi Penting (Clause 3)

* **Explosive Atmosphere (3.1):** Campuran zat mudah terbakar (gas, uap, debu, serat, partikel layang) dengan udara pada kondisi atmosferik yang setelah terjadi penyalaan menyebabkan perambatan api secara mandiri (*self-sustaining flame propagation*).
* **Explosive Gas Atmosphere (3.2):** Campuran gas atau uap mudah terbakar dengan udara pada kondisi atmosferik yang dapat merambatkan api setelah tersulut.
* **Hazardous Area (3.3.1):** Area di mana atmosfer gas eksplosif hadir atau diperkirakan dapat hadir dalam jumlah sedemikian rupa sehingga memerlukan tindakan pencegahan khusus pada konstruksi, pemasangan, dan penggunaan peralatan.
* **Non-Hazardous Area (3.3.2):** Area di mana atmosfer gas eksplosif diperkirakan tidak akan hadir dalam jumlah yang memerlukan tindakan pencegahan khusus.
* **Zones (3.3.3):**
  * **Zone 0 (3.3.4):** Area di mana atmosfer gas eksplosif hadir secara terus-menerus (*continuously*), untuk periode yang lama (*long periods*), atau sering (*frequently*).
  * **Zone 1 (3.3.5):** Area di mana atmosfer gas eksplosif kemungkinan besar terjadi secara periodik atau sesekali dalam operasi normal (*normal operation*).
  * **Zone 2 (3.3.6):** Area di mana atmosfer gas eksplosif kecil kemungkinannya terjadi dalam operasi normal, dan jika terjadi, hanya akan berlangsung dalam waktu yang singkat (*short period only*).
* **Extent of Zone (3.3.7):** Jarak ke segala arah dari sumber lepasan hingga campuran gas/udara terencerkan di bawah Batas Mudah Terbakar Bawah (*Lower Flammable Limit* / LFL).
* **Source of Release (3.4.1):** Titik atau lokasi dari mana gas, uap, kabut, atau cairan mudah terbakar dapat terlepas ke atmosfer.
* **Grades of Release:**
  * **Continuous Grade (3.4.2):** Lepasan yang terjadi terus-menerus atau untuk durasi lama atau sering terjadi.
  * **Primary Grade (3.4.3):** Lepasan yang diperkirakan terjadi secara berkala atau sesekali selama operasi normal.
  * **Secondary Grade (3.4.4):** Lepasan yang tidak diperkirakan terjadi dalam operasi normal, dan bila terjadi, hanya jarang dan berlangsung singkat.
* **Ventilation & Dilution (3.5):**
  * *Ventilation:* Pergerakan udara dan pergantiannya dengan udara segar.
  * *Dilution:* Pencampuran uap/gas mudah terbakar dengan udara seiring waktu yang menurunkan konsentrasi zat.
  * *Dilution Volume ($V_z$):* Volume di sekitar sumber lepasan di mana konsentrasi belum terencerkan ke batas aman.
  * *Background Concentration ($X_b$):* Konsentrasi rata-rata zat mudah terbakar di dalam volume ruangan di luar batas *plume/jet* lepasan.
* **Karakteristik Zat Mudah Terbakar (3.6):**
  * *Flashpoint (3.6.8):* Suhu cairan terendah di mana cairan menghasilkan uap yang cukup untuk membentuk campuran yang dapat menyala di udara.
  * *LFL / Lower Flammable Limit (3.6.12):* Batas konsentrasi minimum gas/uap di udara di mana ledakan/pembakaran dapat terjadi.
  * *UFL / Upper Flammable Limit (3.6.13):* Batas konsentrasi maksimum zat di udara di atas mana ledakan tidak dapat terjadi.
  * *Auto-Ignition Temperature (3.6.11):* Suhu terendah permukaan yang dipanaskan yang mampu menyulut zat mudah terbakar dalam bentuk gas/uap.

---

### 4. Prinsip Keselamatan & Metodologi Klasifikasi (Clauses 4 & 5)

#### 4.1 Prinsip Dasar Keselamatan
1. Hilangkan kemungkinan terbentuknya atmosfer gas eksplosif di sekitar sumber penyalaan (*eliminate explosive atmosphere*).
2. Hilangkan sumber penyalaan (*eliminate source of ignition*).
3. Jika tidak memungkinkan, rancang instalasi dan prosedur kerja sedemikian rupa agar probabilitas terjadinya koinsidensi antara atmosfer eksplosif dan sumber penyalaan ditekan serendah mungkin (*ALARP*).
4. Minimalkan jumlah dan luasan Zona 0 dan Zona 1 melalui desain pabrik yang baik; upayakan instalasi sebagian besar berupa Zona 2 atau non-hazardous.

#### 4.2 Kompetensi Personel (Clause 4.4)
Klasifikasi area harus dilaksanakan oleh personel yang memahami karakteristik zat mudah terbakar, prinsip dispersi gas/uap, serta proses dan peralatan mekanikal/elektrikal yang terlibat.

#### 4.3 Metodologi Klasifikasi (Clause 5)
* **Classification by Sources of Release (5.2):**
  1. Identifikasi sumber lepasan.
  2. Tentukan laju lepasan (*release rate*) dan tingkat lepasan (*grade of release*).
  3. Evaluasi kondisi ventilasi/pengenceran dan efektivitasnya.
  4. Tentukan tipe zona (*Zone 0, 1, 2, atau NE*).
  5. Tentukan luasan/jarak zona (*extent of zone*).
* **Use of Industry Codes and National Standards (5.3 & Annex K):** Contoh: Energy Institute IP15, IGEM/SR/25, API RP 505, NFPA 497.
* **Simplified Methods (5.4):** Pendekatan konservatif standar untuk unit-unit tipikal pabrik tanpa analisis rinci tiap titik.

---

### 5. Karakteristik Lepasan & Bentuk-Bentuk Rilis (Clause 6 & Annex B)

#### 5.1 Bentuk Lepasan (Forms of Release - 6.3 & B.6)
* **Gas / Uap Bebas Tekanan Rendah:** Dipengaruhi oleh densitas relatif (gas ringan seperti $H_2$, $CH_4$ bergerak ke atas secara apung; gas berat seperti propana, butana mengalir ke bawah/permukaan tanah dan masuk ke cekungan/parit).
* **Gas / Uap Bertekanan Tinggi:** Membentuk pancaran jet supersonik/sonik (*choked flow*) yang menyedot udara (*entrainment*) dan mengencerkan dirinya sendiri (*self-diluting*).
* **Gas Cair di Bawah Tekanan (*Liquefied under Pressure*):** Mengalami ekspansi kilat (*flash evaporation*), pembentukan aerosol dingin yang bertindak sebagai gas berat, serta potensi genangan dingin (*cold pool*).
* **Gas Cair Berpendingin (*Cryogenic / Refrigerated*):** Menghasilkan kolam mendidih dan awan gas dingin pekat yang mula-mula lebih berat dari udara sebelum menghangat.
* **Cairan Mudah Terbakar (Penguapan Kolam / *Pool Evaporation*):** Membentuk uap di atas permukaan cairan tergantung pada tekanan uap (*vapour pressure*) dan kecepatan angin di atas permukaan.

#### 5.2 Perhitungan Laju Lepasan (Annex B.7)

##### A. Laju Lepasan Cairan (B.7.2.2 - Persamaan B.1)
$$W = C_d \cdot S \cdot \sqrt{2 \cdot \rho \cdot \Delta p} \quad (\text{kg/s})$$

Di mana:
* $C_d$: Koefisien buang / *discharge coefficient* ($0{,}50 - 0{,}75$ untuk orifice tajam; $0{,}95 - 0{,}99$ untuk lubang teratur).
* $S$: Luas penampang lubang bocor ($\text{m}^2$).
* $\rho$: Densitas massa cairan ($\text{kg/m}^3$).
* $\Delta p$: Perbedaan tekanan pada lubang bocor ($\text{Pa}$).

##### B. Tekanan Kritis Aliran Gas (Persamaan B.2)
$$p_c = p_a \left(\frac{\gamma + 1}{2}\right)^{\frac{\gamma}{\gamma - 1}} \quad (\text{Pa})$$

* Jika tekanan bejana $p > p_c$, aliran berkecepatan sonik (*choked release*).
* Untuk gas ideal: $\gamma = \frac{M \cdot c_p}{M \cdot c_p - R}$. Umumnya $p_c \approx 1{,}89 \cdot p_a$ (sekitar $1{,}9\text{ bar absolute}$).

##### C. Laju Lepasan Gas Subsonik / Non-choked ($p < p_c$) (Persamaan B.3)
$$W_g = C_d \cdot S \cdot p \cdot \sqrt{\frac{M}{Z \cdot R \cdot T} \cdot \frac{2\gamma}{\gamma - 1} \left[ 1 - \left(\frac{p_a}{p}\right)^{\frac{\gamma - 1}{\gamma}} \right]} \cdot \left(\frac{p_a}{p}\right)^{\frac{1}{\gamma}} \quad (\text{kg/s})$$

##### D. Laju Lepasan Gas Sonik / Choked ($p \ge p_c$) (Persamaan B.4)
$$W_g = C_d \cdot S \cdot p \cdot \sqrt{\frac{M}{Z \cdot R \cdot T} \cdot \gamma \left(\frac{2}{\gamma + 1}\right)^{\frac{\gamma + 1}{\gamma - 1}}} \quad (\text{kg/s})$$

##### E. Laju Alir Volumetrik Gas (Persamaan B.5)
$$Q_g = \frac{W_g}{\rho_g} \quad (\text{m}^3\text{/s}) \quad \text{dengan} \quad \rho_g = \frac{p_a \cdot M}{R \cdot T_a}$$

##### F. Laju Penguapan Kolam Cairan (Persamaan B.6 & B.7)
$$W_e = \frac{6{,}55 \cdot u_w^{0{,}78} \cdot A_p \cdot p_v \cdot M^{0{,}667}}{R \cdot \bar{T}} \quad (\text{kg/s})$$

$$Q_g \approx \frac{6{,}5 \cdot u_w^{0{,}78} \cdot A_p \cdot p_v}{10^5 \cdot M^{0{,}333}} \cdot \frac{T_a}{T} \quad (\text{m}^3\text{/s})$$

Jika diasumsikan kondisi tenang $u_w = 0{,}5\text{ m/s}$, luas kolam $A_p = 1{,}0\text{ m}^2$, dan suhu cairan sama dengan suhu ruang (Persamaan B.8):
$$Q_g \approx \frac{3{,}78 \times 10^{-5} \cdot p_v}{M^{0{,}333}} \quad (\text{m}^3\text{/s})$$

#### 5.3 Rekomendasi Luas Lubang Bocor untuk Tingkat Lepasan Sekunder (Table B.1)

| Tipe Komponen | Item / Kondisi | Kondisi Tidak Membesar: $S$ ($\text{mm}^2$) | Kondisi Erosi/Membesar: $S$ ($\text{mm}^2$) | Kondisi Rusak Parah (Blow-out): $S$ ($\text{mm}^2$) |
| :--- | :--- | :--- | :--- | :--- |
| **Elemen Sealing pada Bagian Diam** | Flens dengan paking serat terkompresi | $\ge 0{,}025 \text{ s/d } 0{,}25$ | $> 0{,}25 \text{ s/d } 2{,}5$ | (Sektor antar baut) $\times$ (tebal gasket $\ge 1\text{ mm}$) |
| | Flens dengan spiral wound gasket | $0{,}025$ | $0{,}25$ | (Sektor antar baut) $\times$ (tebal gasket $\ge 0{,}5\text{ mm}$) |
| | Sambungan cincin (*ring joint*) | $0{,}1$ | $0{,}25$ | $0{,}5$ |
| | Sambungan pipa kecil (*small bore* $\le 50\text{ mm}$) | $\ge 0{,}025 \text{ s/d } 0{,}1$ | $> 0{,}1 \text{ s/d } 0{,}25$ | $1{,}0$ |
| **Elemen Bergerak (Kecepatan Rendah)** | Packing batang katup (*valve stem*) | $0{,}25$ | $2{,}5$ | Data manufaktur ($\ge 2{,}5\text{ mm}^2$) |
| | Katup pelepas tekanan (*relief valve*) | $0{,}1 \times (\text{luas penampang})$ | N/A | N/A |
| **Elemen Bergerak (Kecepatan Tinggi)** | Pompa dan kompresor | N/A | $\ge 1 \text{ s/d } 5$ | Data manufaktur ($\ge 5\text{ mm}^2$) |

---

### 6. Panduan Ventilasi & Derajat Pengenceran (Clause 6.4, 6.5 & Annex C)

#### 6.1 Karakteristik Ventilasi & Pengenceran
* **Derajat Pengenceran (*Degree of Dilution*):**
  * **High Dilution:** Konsentrasi di dekat sumber lepasan menurun sangat cepat; praktis tidak ada persistensi atmosfer gas eksplosif setelah pelepasan berhenti. Menghasilkan volume bahaya sangat kecil ($V_z < 0{,}1\text{ m}^3$).
  * **Medium Dilution:** Konsentrasi terkontrol menghasilkan batas zona yang stabil selama pelepasan berlangsung; gas tidak bertahan lama setelah rilis berakhir.
  * **Low Dilution:** Konsentrasi signifikan bertahan selama rilis atau persistensi signifikan setelah pelepasan berhenti.
* **Ketersediaan Ventilasi (*Availability of Ventilation*):**
  * **Good:** Ventilasi hadir secara terus-menerus (*virtually continuous*).
  * **Fair:** Diharapkan hadir selama operasi normal; diskontinuitas jarang dan berdurasi singkat.
  * **Poor:** Tidak memenuhi kriteria Good maupun Fair, namun diskontinuitas tidak berlangsung dalam periode lama.

#### 6.2 Evaluasi Ventilasi Ruangan Tertutup (C.3.6)
Konsentrasi latar belakang dalam ruang berventilasi:
$$X_b = \frac{f \cdot Q_g}{Q_g + Q_1} = \frac{f \cdot Q_g}{Q_2} \quad (\text{vol/vol}) \quad (\text{Persamaan C.1})$$
$$Q_2 = C \cdot V_0 \quad (\text{m}^3\text{/s})$$

Di mana:
* $f$: Faktor inefisiensi ventilasi / pencampuran non-ideal ($f = 1$ untuk pencampuran sempurna/homogen; $f = 1{,}5 - 5$ untuk pencampuran tidak sempurna).
* $C$: Frekuensi pergantian udara per detik ($\text{s}^{-1}$).
* $V_0$: Volume total ruangan ($\text{m}^3$).
* **Kriteria:** Jika konsentrasi latar belakang $X_b > 0{,}25 \times \text{LFL}$ ($X_{\text{crit}}$), pengenceran harus diklasifikasikan sebagai **Low Dilution**.

#### 6.3 Ventilasi Alami Bangunan (C.5)
* Aliran udara akibat angin (*wind-induced*):
  $$Q_a = C_d \cdot A_e \cdot u_w \sqrt{\frac{\Delta C_p}{2}} \quad (\text{Persamaan C.2})$$
* Luas bukaan efektif ekuivalen:
  $$A_e = \frac{\sqrt{2} \cdot A_1 \cdot A_2}{\sqrt{A_1^2 + A_2^2}} \quad (\text{Persamaan C.3 & C.5})$$
* Aliran udara akibat gaya apung termal (*stack effect / buoyancy*):
  $$Q_a = C_d \cdot A_e \sqrt{\frac{\Delta T}{T_{\text{in}} + T_{\text{out}}} \cdot g \cdot H} \quad (\text{Persamaan C.4})$$

---

### 7. Penentuan Tipe Zona & Jarak Bahaya (Clause 7, 8 & Annex D)

#### 7.1 Matriks Estimasi Tipe Zona (Table D.1)

| Tingkat Lepasan (*Grade of Release*) | Efektivitas Ventilasi: High Dilution | | | Efektivitas Ventilasi: Medium Dilution | | | Efektivitas Ventilasi: Low Dilution |
| :--- | :--- | :--- | :--- | :--- | :--- | :--- | :--- |
| | **Good** | **Fair** | **Poor** | **Good** | **Fair** | **Poor** | **Good / Fair / Poor** |
| **Continuous** | Non-hazardous (Zone 0 NE)$^\text{a}$ | Zone 2 (Zone 0 NE)$^\text{a}$ | Zone 1 (Zone 0 NE)$^\text{a}$ | Zone 0 | Zone 0 + Zone 2 | Zone 0 + Zone 1 | Zone 0 |
| **Primary** | Non-hazardous (Zone 1 NE)$^\text{a}$ | Zone 2 (Zone 1 NE)$^\text{a}$ | Zone 2 (Zone 1 NE)$^\text{a}$ | Zone 1 | Zone 1 + Zone 2 | Zone 1 + Zone 2 | Zone 1 atau Zone $0^\text{c}$ |
| **Secondary**$^\text{b}$ | Non-hazardous (Zone 2 NE)$^\text{a}$ | Non-hazardous (Zone 2 NE)$^\text{a}$ | Zone 2 | Zone 2 | Zone 2 | Zone 2 | Zone 1 dan bahkan Zone $0^\text{c}$ |

*Catatan Kaki:*
* $^\text{a}$ **Zone NE (*Negligible Extent*):** Mengindikasikan zona teoretis yang luasan atau volumenya sangat kecil ($V_z < 0{,}1\text{ m}^3$) di bawah kondisi normal, sehingga risiko konsekuensi penyalaan dapat diabaikan.
* $^\text{b}$ Luas Zone 2 dari lepasan sekunder dapat melebihi luas zona dari lepasan primer/kontinu; jika demikian, jarak terbesar yang harus diambil.
* $^\text{c}$ Menjadi Zone 0 jika ventilasi sangat lemah sehingga mendekati kondisi *no-ventilation*.
* Catatan: Ketersediaan ventilasi alami di dalam ruangan tertutup **tidak boleh** dikategorikan sebagai *Good*.

#### 7.2 Karakteristik Lepasan & Kurva Jarak Berbahaya (Annex D.3)
Karakteristik pelepasan dihitung melalui parameter:
$$\frac{W_g}{\rho_g \cdot k \cdot \text{LFL}} \quad (\text{m}^3\text{/s})$$
Di mana $k$ adalah faktor keselamatan (biasanya $0{,}5 - 1{,}0$).

Jarak berbahaya (*Hazardous Distance* $r$) diperoleh dari grafik **Figure D.1** berdasarkan jenis pancaran:
1. **Unimpeded Jet Release (kecepatan tinggi):** Kurva paling rendah (*jet curve*).
2. **Diffusive Jet Release (kecepatan rendah atau terhalang rintangan):** Kurva tengah (*diffusive curve*).
3. **Heavy Gas / Pool Evaporation (merambat di permukaan tanah):** Kurva paling atas (*heavy gas curve*).

---

### 8. Contoh Studi Kasus Klasifikasi Area (Annex E)

#### Rangkuman 5 Contoh Tipikal (Annex E.2)

| Parameter | Contoh 1: Pompa Outdoor | Contoh 2: Pompa Indoor | Contoh 3: Katup Breather | Contoh 4: Control Valve | Contoh 5: Pemipaan Gas Kompleks |
| :--- | :--- | :--- | :--- | :--- | :--- |
| **Substansi** | Benzena Cair | Produk Cair Benzena | Uap Benzena | Gas Propana | Gas Alam Basah (*Wet Gas*) |
| **LFL** | $1{,}2\%\text{ vol}$ ($0{,}039\text{ kg/m}^3$) | $1{,}2\%\text{ vol}$ | $1{,}2\%\text{ vol}$ | $1{,}7\%\text{ vol}$ ($0{,}031\text{ kg/m}^3$) | $4{,}0\%\text{ vol}$ ($0{,}033\text{ kg/m}^3$) |
| **Lokasi** | Outdoor terbuka | Ruangan tertutup ($150\text{ m}^3$) | Tangki Outdoor terbuka | Luar ruang terhalang | Ruangan tertutup ($21{,}9\text{ m}^3$) |
| **Tingkat Lepasan** | Sekunder (seal pompa) | Sekunder (seal pompa) | Primer (pengisian) & Sekunder (ruptur) | Sekunder (packing stem) | Kontinu (fitting) + Primer + Sekunder |
| **Laju Alir Rilis ($W_g$)** | $3{,}85 \times 10^{-3}\text{ kg/s}$ | $3{,}85 \times 10^{-3}\text{ kg/s}$ | Primer: $4{,}5 \times 10^{-3}\text{ kg/s}$<br>Sekunder: $4{,}95 \times 10^{-2}\text{ kg/s}$ | $5{,}57 \times 10^{-3}\text{ kg/s}$ | Kontinu: $1 \times 10^{-8}\text{ kg/s}$<br>Sekunder: $2{,}18 \times 10^{-3}\text{ kg/s}$ |
| **Karakteristik Lepasan** | $0{,}1\text{ m}^3\text{/s}$ | $0{,}2\text{ m}^3\text{/s}$ ($k=0{,}5$) | Primer: $0{,}12\text{ m}^3\text{/s}$<br>Sekunder: $1{,}27\text{ m}^3\text{/s}$ | $0{,}22\text{ m}^3\text{/s}$ ($k=0{,}8$) | Kontinu: $6{,}01 \times 10^{-8}\text{ m}^3\text{/s}$<br>Sekunder: $0{,}13\text{ m}^3\text{/s}$ |
| **Derajat Pengenceran** | Medium | Low ($X_b = 7\% > X_{\text{crit}}$) | Medium | Medium | Low ($X_b = 10{,}3\% > X_{\text{crit}}$) |
| **Hasil Zona & Jarak** | **Zone 2**<br>Radius horizontal $3{,}0\text{ m}$, tinggi $1{,}5\text{ m}$ (Heavy gas) | **Zone 1**<br>Mencakup **seluruh volume ruangan** ($r \approx 4\text{ m}$) | **Zone 1:** $r = 1{,}5\text{ m}$ (primer)<br>**Zone 2:** $r = 5{,}0\text{ m}$ (sekunder) | **Zone 2**<br>$r = 1{,}0\text{ m}$ (jet) s/d $2{,}0\text{ m}$ (diffusive) | **Zone 1**<br>Mencakup **seluruh volume ruangan** ($r \approx 1{,}5\text{ m}$) |
| **Group & Temp Class** | IIA T1 | IIA T1 | IIA T1 | IIA T1 | IIA T1 |

---

### 9. Rangkuman Annex Khusus

* **Annex G (Flammable Mists):** Cairan berviskositas tinggi atau cairan dengan flashpoint tinggi dapat membentuk kabut mudah terbakar (*ignitable mist*) jika disemprotkan di bawah tekanan tinggi melalui celah kecil. IEC 60079-14 belum sepenuhnya mencakup proteksi mistik murni tanpa keberadaan uap.
* **Annex H (Hydrogen):** Hidrogen memiliki rentang mampu nyala sangat lebar ($4\% - 77\%$), energi penyalaan minimum (*MIE*) sangat rendah ($0{,}017\text{ mJ}$), gas group IIC, kelas suhu T1 ($560^\circ\text{C}$). Densitas sangat ringan membuatnya berdifusi sangat cepat ke atas; ventilasi di puncak atap/atap miring (*alcoves/dormers*) mutlak diperlukan untuk mencegah perangkap kantong gas.
* **Annex I (Hybrid Mixtures):** Kombinasi gas/uap mudah terbakar dengan debu/serat mudah terbakar. Batas batas eksplosif campuran hibrida dapat berada jauh di bawah LFL gas maupun MEC debu secara individual. Konsentrasi di atas $25\%$ LFL atau $25\%$ MEC harus dianggap eksplosif.
* **Annex J (Persamaan Penunjang Pengenceran):**
  * Waktu teoritis yang dibutuhkan untuk mengencerkan konsentrasi latar belakang dari $X_b$ ke konsentrasi kritis $X_{\text{crit}}$:
    $$t_d = -\frac{1}{C} \ln\left(\frac{X_{\text{crit}}}{X_b}\right) \quad (\text{Persamaan J.2})$$

---

## ❓ Antisipasi Pertanyaan Karyawan (FAQ Otomatis)

### Q1: Apa perbedaan mendasar antara Zone 0, Zone 1, dan Zone 2 dalam pekerjaan operasional kita?
**Jawaban:**
* **Zone 0:** Area di mana gas mudah terbakar ada terus-menerus atau dalam waktu sangat lama (misal: di dalam ruang uap tangki bahan bakar tertutup). Di area ini hanya peralatan ber-EPL 'Ga' yang diizinkan.
* **Zone 1:** Area di mana gas diperkirakan sering muncul saat operasi rutin/normal (misal: sekitar lubang sampling atau relief vent). Memerlukan peralatan ber-EPL minimal 'Gb'.
* **Zone 2:** Area di mana gas hanya mungkin muncul jika terjadi ketidaknormalan/kebocoran sekunder dan langsung hilang dalam waktu singkat. Peralatan ber-EPL 'Gc' dapat dipasang di sini.

### Q2: Apa yang dimaksud dengan "Zone NE" (*Negligible Extent*) dan kapan kita bisa menerapkannya?
**Jawaban:**
Zone NE adalah zona bahaya teoretis yang memiliki volume atau bentangan fisik sangat kecil (biasanya volume awan gas di bawah $0{,}1\text{ m}^3$). Karena jika tersulut energinya tidak menimbulkan ledakan destruktif yang berbahaya, area dengan Zone NE dapat diperlakukan sebagai **Non-Hazardous Area** untuk keperluan pemilihan peralatan listrik. Namun, kriteria ventilasinya harus berderajat *High Dilution*.

### Q3: Jika suatu ruangan kompresor tertutup memiliki kebocoran sekunder, mengapa hasilnya bisa menjadi Zone 1 padahal pelepasannya berstatus sekunder?
**Jawaban:**
Berdasarkan Tabel D.1 dan klausul C.3.6, jika ventilasi ruangan buruk (*low dilution* atau konsentrasi akumulasi $X_b$ melebihi $25\%$ LFL), gas yang bocor tidak dapat terbuang cepat dan menetap lama di dalam ruangan. Kegagalan ventilasi ini menaikkan tingkat keparahan klasifikasi dari yang seharusnya Zone 2 menjadi **Zone 1 di seluruh ruangan**.

### Q4: Apakah kebocoran dari pipa yang dilas penuh (*fully welded pipe*) dihitung sebagai sumber lepasan (*source of release*)?
**Jawaban:**
Tidak. Pipa logam yang tersambung penuh dengan pengelasan (*all-welded pipework*) tanpa sambungan flens, ulir, atau katup **tidak dianggap sebagai sumber lepasan** dalam kondisi operasi normal maupun abnormal standar, sehingga tidak menciptakan area berbahaya.

### Q5: Bagaimana pengaruh ventilasi alami di dalam gedung terhadap penetapan ketersediaan ventilasi (*ventilation availability*)?
**Jawaban:**
Menurut standar BS EN 60079-10-1 klausul C.3.7.1 dan Tabel D.1, ketersediaan ventilasi alami di dalam ruangan tertutup **tidak pernah boleh diklasifikasikan sebagai *Good*** karena sangat bergantung pada faktor cuaca eksternal (kecepatan angin dan perbedaan suhu) yang tidak dapat dikendalikan. Kategori maksimumnya adalah *Fair* atau *Poor*.

### Q6: Bagaimana penanganan klasifikasi area untuk instalasi gas hidrogen ($H_2$)?
**Jawaban:**
Hidrogen memiliki massa jenis sangat ringan ($0{,}07$ terhadap udara) dan laju difusi sangat tinggi ke atas, serta termasuk Gas Group IIC. Desain fasilitas hidrogen harus menghindari kantong jebakan di plafon/atap (*dead spots/alcoves*) dan wajib menyediakan ventilasi pasif terbuka di puncak atap (*high-point vents*). Sensor gas hidrogen harus dipasang di titik tertinggi dekat langit-langit atau ventilasi keluar.

---

## 📚 Glosarium & Istilah Penting

* **ATEX:** *Appareils destinés à être utilisés en ATmosphères EXplosibles* — Arahan Uni Eropa (2014/34/EU dan 1999/92/EC) mengenai keselamatan di atmosfer ledakan.
* **EPL (*Equipment Protection Level*):** Tingkat proteksi yang diberikan pada peralatan berdasarkan probabilitas peralatan menjadi sumber penyalaan (Ga, Gb, Gc untuk atmosfer gas).
* **LFL (*Lower Flammable Limit*) / LEL (*Lower Explosive Limit*):** Konsentrasi volume atau massa terendah dari uap/gas mudah terbakar dalam udara yang dapat terbakar atau meledak bila tersulut api.
* **UFL (*Upper Flammable Limit*) / UEL (*Upper Explosive Limit*):** Konsentrasi volume tertinggi dari gas mudah terbakar yang dapat menyala di udara.
* **Flash Point:** Suhu cairan terendah di mana uapnya dapat menyala saat bersentuhan dengan sumber penyalaan.
* **AIT (*Auto-Ignition Temperature*):** Suhu terendah permukaan yang dapat menyulut uap gas tanpa adanya percikan atau api terbuka.
* **Choked Flow:** Kondisi dinamika fluida bertekanan di mana kecepatan aliran mencapai kecepatan suara (*sonic velocity*, Mach 1), sehingga peningkatan penurunan tekanan ke hilir tidak lagi menambah kecepatan alir.
* **Zone NE (*Negligible Extent*):** Zona bahaya dengan luasan fisik/volume awan gas yang sangat kecil sehingga dampak pembakarannya dapat diabaikan secara praktis.
* **Ventilation Velocity ($u_w$):** Kecepatan pergerakan aliran udara segar di area lepasan yang mempengaruhi pencampuran dan dispersi gas.