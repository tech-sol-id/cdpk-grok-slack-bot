---
sumber_dokumen: "Certificate Calibration.pdf"
gdrive_file_id: "1DyuqOXQJMsOHRbloZJbCU6mTGll3PzW5"
gdrive_modified_time: "2025-01-04T05:40:46.143Z"
folder_asal: "Root Knowledge / OPERATIONS / Technicians"
tanggal_ekstraksi: "2026-10-16"
tingkat_akses: "SEMUA_MEMBER"
---

# Sertifikat Kalibrasi Communication System Analyzer General Dynamics R8000 (No: JCL/24/1567/HS)

## 📌 Executive Summary

* **Identitas Unit & Kepemilikan:** Kalibrasi resmi untuk unit *Communication System Analyzer* General Dynamics R8000 (Serial Number: `800LNY0018`) milik PT Citra Data Purna Kharisma oleh Laboratorium Kalibrasi Terakreditasi PT Telkom Indonesia Tbk (LK-016-IDN / KAN).
* **Periode Kalibrasi:** Diterima tanggal 19 Juni 2024, selesai dikalibrasi pada 28 Juni 2024, dan sertifikat resmi diterbitkan pada 05 Juli 2024.
* **Standar & Ketertelusuran:** Prosedur mengacu pada standar internal Telkom (TCL-WI-V009, TCL-WI-F003, TCL-WI-F007) yang tertelusur ke SNSU-BSN dan Keysight Technologies.
* **Temuan Khusus (Out of Spec):** Sebagian besar parameter generator, modulasi AM/FM, digital voltmeter, dan spectrum analyzer berada dalam batas toleransi, namun terdapat 1 catatan deviasi pada pengujian **Spectrum Analyzer - Frequency Response Test** pada frekuensi 1500 MHz (*Indicated*: -7.5 dBm vs *Applied*: -21.029 dBm, Correction: -13.529 dB) dengan status **Out Of Spec**.

---

## 📖 Salinan Lengkap & Terstruktur

### 1. Informasi Umum Dokumen & Laboratorium

* **Penerbit:** PT TELKOM INDONESIA Tbk - KAN ACCREDITED CALIBRATION LABORATORY (LK-016-IDN)
* **Nomor Dokumen:** Form TCL-QP-19-01
* **Nomor / Tanggal Terbit Form:** 01 / 20 Juli 2017
* **Nomor / Tanggal Revisi Form:** 02 / 04 Januari 2021
* **Nomor Sertifikat:** `JCL/24/1567/HS`
* **Penandatangan Resmi (Approved Signatory):** M. Ilyas
* **Kontak Laboratorium:**
  * Jakarta: Jl. Percetakan Negara No. 17-19 Jakarta Pusat 10570 | Telp: 021-21480341
  * Medan: Jl. Gaharu No. 1 Medan 20235 | Telp: 061-4531311 | Fax: 061-4147434
  * Surabaya: Jl. Gayungan PTT No. 17-19 Surabaya 60235 | Telp: 031-8283678 | Fax: 031-8283388
  * Makassar: Jl. AP Pettarani No. 4 Makassar 90221 | Telp: 0411-861153

### 2. Rincian Pengajuan & Unit Uji (UUT)

* **Tanggal Terbit Sertifikat (Date of Issue):** 05-Jul-2024
* **Pemilik Alat (Submitted by):** PT. CITRA DATA PURNA KHARISMA
* **Alamat Pemilik:** Jl. Kramat I No. 54 Kwitang, Senen, Jakarta Pusat
* **Deskripsi Alat:** Communication System Analyzer
* **Pabrikan / Model:** General Dynamics / R8000
* **Nomor Seri (Serial Number):** 800LNY0018
* **Kondisi Lingkungan Kalibrasi:**
  * Suhu: 22.9 °C ± 0.2 °C
  * Kelembapan Relatif: 53.1 % ± 1.8 % RH
* **Lokasi Kalibrasi:** In-House
* **Tanggal Diterima:** 19-Jun-2024
* **Tanggal Selesai Kalibrasi:** 28-Jun-2024

### 3. Ketertelusuran & Standar Acuan

PT. Telkom Indonesia, Tbk. menyatakan bahwa instrumen ini telah dikalibrasi di bawah kondisi lingkungan tersebut menggunakan standar yang tertelusur ke Sistem Satuan Internasional (SI) melalui SNSU-BSN dan Keysight Technologies.

**Metode Kalibrasi:**
Dilaksanakan berdasarkan Prosedur Kalibrasi Standar Telkom: `TCL-WI-V009`, `TCL-WI-F003`, dan `TCL-WI-F007`.

**Daftar Alat Standar Acuan:**

| No. | Deskripsi Alat Standar | Serial Number (S/N) | Tanggal Kalibrasi Terakhir | Tanggal Jatuh Tempo Kalibrasi |
|:---:|:---|:---:|:---:|:---:|
| 1 | Rubidium Frequency Standard | 216 | 18-Jan-2024 | 17-Jan-2025 |
| 2 | Universal Counter | 3736A04911 | 24-Oct-2023 | 23-Oct-2024 |
| 3 | Signal Generator | 3546A00791 | 27-Mar-2024 | 26-Mar-2025 |
| 4 | Measuring Receiver | 3704A04336 | 08-Jun-2022 | 07-Jun-2025 |
| 5 | Sensor Module | 3528A02097 | 14-Dec-2023 | 13-Dec-2024 |
| 6 | Calibrator | 4066802 | 31-Oct-2023 | 30-Oct-2024 |

*Catatan Ketidakpastian:* Nilai ketidakpastian bentangan (*reported uncertainty*) didasarkan pada ketidakpastian standar dikalikan faktor cakupan k=2, memberikan tingkat kepercayaan sekitar 95%.

---

### 4. Data Hasil Pengujian Kalibrasi

#### 1. Generator Part @ Generate Port

##### 1.1 Frequency Accuracy Test
| Test No. | UUT Setting Frequency | Measured Value | Correction | Uncertainty |
|:---:|:---:|:---:|:---:|:---:|
| 1 | 50 MHz | 49.9999908 MHz | -0.9 Hz | ± 1.2 Hz |
| 2 | 100 MHz | 99.99999813 MHz | -1.9 Hz | ± 2.3 Hz |
| 3 | 400 MHz | 399.9999914 MHz | -8.6 Hz | ± 9.2 Hz |
| 4 | 800 MHz | 799.9999833 MHz | -16.7 Hz | ± 18 Hz |
| 5 | 1000 MHz | 999.9999795 MHz | -20.5 Hz | ± 23 Hz |
| 6 | 1800 MHz | 1799.9999486 MHz | -51.4 Hz | ± 41 Hz |
| 7 | 2000 MHz | 1999.9999578 MHz | -42.2 Hz | ± 46 Hz |
| 8 | 2500 MHz | 2499.9999464 MHz | -53.6 Hz | ± 58 Hz |
| 9 | 2900 MHz | 2899.9999430 MHz | -57.0 Hz | ± 67 Hz |

##### 1.2 Output Level Test @ Generate Port
| Test No. | UUT Setting Freq | UUT Setting Level | Measured Value | Correction | Uncertainty |
|:---:|:---:|:---:|:---:|:---:|:---:|
| 1 | 100 MHz | -1 dBm | -0.713 dBm | 0.287 dB | ± 0.17 dB |
| | | -5 dBm | -5.056 dBm | -0.056 dB | ± 0.17 dB |
| | | -10 dBm | -9.686 dBm | 0.314 dB | ± 0.17 dB |
| | | -20 dBm | -19.851 dBm | 0.149 dB | ± 0.17 dB |
| | | -30 dBm | -29.815 dBm | 0.185 dB | ± 0.17 dB |
| | | -40 dBm | -39.970 dBm | 0.030 dB | ± 0.17 dB |
| | | -50 dBm | -49.824 dBm | 0.176 dB | ± 0.17 dB |
| | | -60 dBm | -59.887 dBm | 0.113 dB | ± 0.17 dB |
| 2 | 400 MHz | -1 dBm | -1.817 dBm | -0.817 dB | ± 0.17 dB |
| | | -5 dBm | -5.747 dBm | -0.747 dB | ± 0.17 dB |
| | | -10 dBm | -10.533 dBm | -0.533 dB | ± 0.17 dB |
| | | -20 dBm | -20.853 dBm | -0.853 dB | ± 0.17 dB |
| | | -30 dBm | -30.915 dBm | -0.915 dB | ± 0.17 dB |
| | | -40 dBm | -40.802 dBm | -0.802 dB | ± 0.17 dB |
| | | -50 dBm | -50.838 dBm | -0.838 dB | ± 0.17 dB |
| | | -60 dBm | -60.750 dBm | -0.750 dB | ± 0.17 dB |
| 3 | 800 MHz | -1 dBm | -0.445 dBm | 0.555 dB | ± 0.17 dB |
| | | -5 dBm | -4.645 dBm | 0.355 dB | ± 0.17 dB |
| | | -10 dBm | -9.650 dBm | 0.350 dB | ± 0.17 dB |
| | | -20 dBm | -19.830 dBm | 0.170 dB | ± 0.17 dB |
| | | -30 dBm | -29.998 dBm | 0.002 dB | ± 0.17 dB |
| | | -40 dBm | -39.684 dBm | 0.316 dB | ± 0.17 dB |
| | | -50 dBm | -49.662 dBm | 0.338 dB | ± 0.17 dB |
| | | -60 dBm | -59.735 dBm | 0.265 dB | ± 0.17 dB |
| 4 | 1000 MHz | -1 dBm | -1.163 dBm | -0.163 dB | ± 0.17 dB |
| | | -5 dBm | -5.252 dBm | -0.252 dB | ± 0.17 dB |
| | | -10 dBm | -10.426 dBm | -0.426 dB | ± 0.17 dB |
| | | -20 dBm | -20.550 dBm | -0.550 dB | ± 0.17 dB |
| | | -30 dBm | -30.567 dBm | -0.567 dB | ± 0.17 dB |
| | | -40 dBm | -40.352 dBm | -0.352 dB | ± 0.17 dB |
| | | -50 dBm | -50.310 dBm | -0.310 dB | ± 0.17 dB |
| | | -60 dBm | -60.193 dBm | -0.193 dB | ± 0.17 dB |
| 5 | 1800 MHz | -1 dBm | -0.483 dBm | 0.517 dB | ± 0.17 dB |
| | | -5 dBm | -4.507 dBm | 0.493 dB | ± 0.17 dB |
| | | -10 dBm | -10.295 dBm | -0.295 dB | ± 0.17 dB |
| | | -20 dBm | -19.980 dBm | 0.020 dB | ± 0.17 dB |
| | | -30 dBm | -30.017 dBm | -0.017 dB | ± 0.17 dB |
| | | -40 dBm | -40.143 dBm | -0.143 dB | ± 0.17 dB |
| | | -50 dBm | -49.914 dBm | 0.086 dB | ± 0.17 dB |
| | | -60 dBm | -60.299 dBm | -0.299 dB | ± 0.17 dB |
| 6 | 2500 MHz | -1 dBm | -1.841 dBm | -0.841 dB | ± 0.17 dB |
| | | -5 dBm | -4.832 dBm | 0.168 dB | ± 0.17 dB |
| | | -10 dBm | -10.253 dBm | -0.253 dB | ± 0.17 dB |
| | | -20 dBm | -19.859 dBm | 0.141 dB | ± 0.17 dB |
| | | -30 dBm | -30.210 dBm | -0.210 dB | ± 0.17 dB |
| | | -40 dBm | -40.090 dBm | -0.090 dB | ± 0.17 dB |
| | | -50 dBm | -49.992 dBm | 0.008 dB | ± 0.17 dB |
| | | -60 dBm | -60.217 dBm | -0.217 dB | ± 0.17 dB |

##### 1.3 Output Level Test @ RF IN/OUT Port
| Test No. | UUT Setting Freq | UUT Setting Level | Measured Value | Correction | Uncertainty |
|:---:|:---:|:---:|:---:|:---:|:---:|
| 1 | 100 MHz | -40.00 dBm | -41.934 dBm | -1.934 dB | ± 0.17 dB |
| | | -50.00 dBm | -50.583 dBm | -0.583 dB | ± 0.17 dB |
| | | -60.00 dBm | -61.739 dBm | -1.739 dB | ± 0.17 dB |
| | | -70.00 dBm | -69.733 dBm | 0.267 dB | ± 0.17 dB |
| 2 | 400 MHz | -40.00 dBm | -41.693 dBm | -1.693 dB | ± 0.17 dB |
| | | -50.00 dBm | -51.331 dBm | -1.331 dB | ± 0.17 dB |
| | | -60.00 dBm | -61.105 dBm | -1.105 dB | ± 0.17 dB |
| | | -70.00 dBm | -69.108 dBm | 0.892 dB | ± 0.17 dB |
| 3 | 800 MHz | -40.00 dBm | -39.851 dBm | 0.149 dB | ± 0.17 dB |
| | | -50.00 dBm | -50.312 dBm | -0.312 dB | ± 0.17 dB |
| | | -60.00 dBm | -60.070 dBm | -0.070 dB | ± 0.17 dB |
| | | -70.00 dBm | -69.236 dBm | 0.764 dB | ± 0.17 dB |
| 4 | 1000 MHz | -40.00 dBm | -41.108 dBm | -1.108 dB | ± 0.17 dB |
| | | -50.00 dBm | -51.343 dBm | -1.343 dB | ± 0.17 dB |
| | | -60.00 dBm | -61.161 dBm | -1.161 dB | ± 0.17 dB |
| | | -70.00 dBm | -69.587 dBm | 0.413 dB | ± 0.17 dB |
| 5 | 1800 MHz | -40.00 dBm | -40.453 dBm | -0.453 dB | ± 0.17 dB |
| | | -50.00 dBm | -50.690 dBm | -0.690 dB | ± 0.17 dB |
| | | -60.00 dBm | -59.832 dBm | 0.168 dB | ± 0.17 dB |
| | | -70.00 dBm | -70.337 dBm | -0.337 dB | ± 0.17 dB |
| 6 | 2000 MHz | -40.00 dBm | -39.654 dBm | 0.346 dB | ± 0.17 dB |
| | | -50.00 dBm | -49.701 dBm | 0.299 dB | ± 0.17 dB |
| | | -60.00 dBm | -60.371 dBm | -0.371 dB | ± 0.17 dB |
| | | -70.00 dBm | -69.632 dBm | 0.368 dB | ± 0.17 dB |
| 7 | 2500 MHz | -40.00 dBm | -41.938 dBm | -1.938 dB | ± 0.17 dB |
| | | -50.00 dBm | -51.655 dBm | -1.655 dB | ± 0.17 dB |
| | | -60.00 dBm | -61.300 dBm | -1.300 dB | ± 0.17 dB |
| | | -70.00 dBm | -70.197 dBm | -0.197 dB | ± 0.17 dB |

##### 1.4 Reference Osc. Output
| Test No. | UUT Setting | Measured Value | Correction | Uncertainty |
|:---:|:---:|:---:|:---:|:---:|
| 1 | 10 MHz | 9.999999994 MHz | 0.006 Hz | ± 0.00094 Hz |

---

#### 2. Monitor Part

##### 2.1 AM Modulation Measurement @ Antenna Port
*(Kondisi: Frequency carrier 500 MHz, -50 dBm MOD. Bandwidth 25 kHz)*

| Test No. | Calibrator Output Mod Freq (Audio) | Calibrator Output Mod Level | UUT Measured Value | Correction | Uncertainty |
|:---:|:---:|:---:|:---:|:---:|:---:|
| 1 | 1 kHz | 10 % | 10 % | 0 % | ± 1.3 % |
| 2 | 1 kHz | 20 % | 21 % | -1 % | ± 1.3 % |
| 3 | 1 kHz | 30 % | 31 % | -1 % | ± 1.3 % |
| 4 | 1 kHz | 40 % | 41 % | -1 % | ± 1.3 % |
| 5 | 1 kHz | 50 % | 51 % | -1 % | ± 1.3 % |
| 6 | 1 kHz | 60 % | 61 % | -1 % | ± 1.3 % |
| 7 | 1 kHz | 70 % | 72 % | -2 % | ± 1.3 % |
| 8 | 1 kHz | 80 % | 82 % | -2 % | ± 1.3 % |
| 9 | 1 kHz | 90 % | 93 % | -3 % | ± 1.3 % |

##### 2.2 FM Modulation Measurement @ Antenna Port
*(Kondisi: Frequency carrier 500 MHz, -50 dBm, MOD. Bandwidth 25 kHz)*

| Test No. | Calibrator Output Mod Freq (Audio) | Calibrator Output Deviation | Measured Value | Correction | Uncertainty |
|:---:|:---:|:---:|:---:|:---:|:---:|
| 1 | 1 kHz | 1 kHz | 1.01 kHz | -0.01 kHz | ± 0.014 kHz |
| 2 | 1 kHz | 2 kHz | 2.00 kHz | 0.00 kHz | ± 0.027 kHz |
| 3 | 1 kHz | 3 kHz | 3.00 kHz | 0.00 kHz | ± 0.041 kHz |
| 4 | 1 kHz | 5 kHz | 5.00 kHz | 0.00 kHz | ± 0.069 kHz |
| 5 | 1 kHz | 8 kHz | 8.00 kHz | 0.00 kHz | ± 0.11 kHz |
| 6 | 1 kHz | 10 kHz | 10.01 kHz | -0.01 kHz | ± 0.14 kHz |
| 7 | 1 kHz | 12.5 kHz | 12.60 kHz | -0.10 kHz | ± 0.17 kHz |

##### 2.3 FM Modulation Measurements @ IN/OUT Port
*(Kondisi: Frequency carrier 100 MHz, 0 dBm)*

| Test No. | Calibrator Output Mod Freq (Audio) | Calibrator Output Deviation | UUT Indicated Value | Correction | Uncertainty |
|:---:|:---:|:---:|:---:|:---:|:---:|
| 1 | 400 Hz | 5 kHz | 5.23 kHz | -0.23 kHz | ± 0.072 kHz |
| | | 8 kHz | 8.21 kHz | -0.21 kHz | ± 0.11 kHz |
| | | 10 kHz | 10.27 kHz | -0.27 kHz | ± 0.14 kHz |
| | | 12 kHz | 12.24 kHz | -0.24 kHz | ± 0.17 kHz |
| 2 | 1000 Hz | 5 kHz | 5.15 kHz | -0.15 kHz | ± 0.071 kHz |
| | | 8 kHz | 8.22 kHz | -0.22 kHz | ± 0.11 kHz |
| | | 10 kHz | 10.21 kHz | -0.21 kHz | ± 0.14 kHz |
| | | 12 kHz | 12.41 kHz | -0.41 kHz | ± 0.17 kHz |

##### 2.4 AM Modulation Measurements @ IN/OUT Port
*(Kondisi: Frequency carrier 100 MHz, 0 dBm)*

| Test No. | Calibrator Output Mod Freq (Audio) | Calibrator Output Mod Level | UUT Indicated Value | Correction | Uncertainty |
|:---:|:---:|:---:|:---:|:---:|:---:|
| 1 | 400 Hz | 10 % | 12 % | -2 % | ± 1.3 % |
| | | 20 % | 23 % | -3 % | ± 1.3 % |
| | | 30 % | 33 % | -3 % | ± 1.3 % |
| | | 40 % | 43 % | -3 % | ± 1.3 % |
| | | 50 % | 53 % | -3 % | ± 1.3 % |
| | | 60 % | 63 % | -3 % | ± 1.3 % |
| | | 70 % | 74 % | -4 % | ± 1.3 % |
| | | 80 % | 85 % | -5 % | ± 1.3 % |
| 2 | 1000 Hz | 10 % | 12 % | -2 % | ± 1.3 % |
| | | 20 % | 23 % | -3 % | ± 1.3 % |
| | | 30 % | 33 % | -3 % | ± 1.3 % |
| | | 40 % | 43 % | -3 % | ± 1.3 % |
| | | 50 % | 53 % | -3 % | ± 1.3 % |
| | | 60 % | 63 % | -3 % | ± 1.3 % |
| | | 70 % | 74 % | -4 % | ± 1.3 % |
| | | 80 % | 84 % | -4 % | ± 1.3 % |

---

#### 3. Spectrum Analyzer Part

##### 3.1 Frequency Read Out (Using Find Peak Marker)
| Test No. | UUT Setting Center Freq | UUT Setting Span | Calibrator Output | UUT Indicated Value | Correction | Uncertainty |
|:---:|:---:|:---:|:---:|:---:|:---:|:---:|
| 1 | 1000 MHz | 10 kHz | 1000 MHz | 1000.000011 MHz | -0.011 kHz | ± 0.00057 kHz |
| | | 50 kHz | 1000 MHz | 1000.000057 MHz | -0.057 kHz | ± 0.00057 kHz |
| | | 100 kHz | 1000 MHz | 1000.000114 MHz | -0.114 kHz | ± 0.00057 kHz |
| | | 1 MHz | 1000 MHz | 1000.001139 MHz | -1.139 kHz | ± 0.00057 kHz |
| 2 | 800 MHz | 10 kHz | 800 MHz | 800.000011 MHz | -0.011 kHz | ± 0.00045 kHz |
| | | 50 kHz | 800 MHz | 800.000068 MHz | -0.068 kHz | ± 0.00045 kHz |
| | | 100 kHz | 800 MHz | 800.000110 MHz | -0.110 kHz | ± 0.00045 kHz |
| | | 1 MHz | 800 MHz | 800.001264 MHz | -1.264 kHz | ± 0.00045 kHz |
| 3 | 2000 MHz | 10 kHz | 2000 MHz | 2000.000000 MHz | 0.000 kHz | ± 0.0011 kHz |
| | | 50 kHz | 2000 MHz | 2000.000068 MHz | -0.068 kHz | ± 0.0011 kHz |
| | | 100 kHz | 2000 MHz | 2000.000125 MHz | -0.125 kHz | ± 0.0011 kHz |

##### 3.2 Frequency Span Accuracy
| Test No. | UUT Setting Center Freq | UUT Setting Span | Applied Value | UUT Indicated Value | Correction | Uncertainty |
|:---:|:---:|:---:|:---:|:---:|:---:|:---:|
| 1 | 1000 MHz | 10 kHz | 8 kHz | 8.041 kHz | -0.04 kHz | ± 0.0045 kHz |
| 2 | 1000 MHz | 50 kHz | 40 kHz | 40.091 kHz | -0.091 kHz | ± 0.0227 kHz |
| 3 | 1000 MHz | 100 kHz | 80 kHz | 80.016 kHz | -0.016 kHz | ± 0.045 kHz |
| 4 | 1000 MHz | 1 MHz | 0.8 MHz | 0.801822 MHz | -1.822 kHz | ± 0.45 kHz |

##### 3.3 Frequency Response Test
| No. | CF. Freq. (MHz) | Span | Test CF. Freq. (MHz) | Applied Value | UUT Indicated Value | Correction | Uncertainty |
|:---:|:---:|:---:|:---:|:---:|:---:|:---:|:---:|
| 1 | 100 | 1 MHz | 100 | -20.173 dBm | -23.1 dBm | 2.927 dB | ± 0.17 dB |
| 2 | 400 | 1 MHz | 400 | -20.413 dBm | -21.3 dBm | 0.887 dB | ± 0.17 dB |
| 3 | 800 | 1 MHz | 800 | -20.953 dBm | -20.9 dBm | -0.013 dB | ± 0.17 dB |
| 4 | 1000 | 1 MHz | 1000 | -20.830 dBm | -21.4 dBm | 0.610 dB | ± 0.17 dB |
| 5 | 1500 | 1 MHz | 1500 | -21.029 dBm | -7.5 dBm * | -13.529 dB | ± 0.17 dB |
| 6 | 2000 | 1 MHz | 2000 | -20.899 dBm | -21.2 dBm | 0.261 dB | ± 0.17 dB |
| 7 | 2500 | 1 MHz | 2500 | -21.192 dBm | -25.3 dBm | 4.148 dB | ± 0.17 dB |

*\*Keterangan: Hasil uji pada baris No. 5 (1500 MHz) berstatus **Out Of Spec**.*

---

#### 4. Digital Volt Meter Part

##### 4.1 AC Voltage Test
| Test No. | UUT Range Setting | Calibrator Output | UUT Indicated Value | Correction | Uncertainty |
|:---:|:---:|:---:|:---:|:---:|:---:|
| 1 | 1 V | 1 V 50 Hz | 1.00 V | 0.00 V | ± 0.0057 V |
| | | 1 V 1 kHz | 1.01 V | -0.01 V | ± 0.0058 V |
| | | 1 V 5 kHz | 1.01 V | -0.01 V | ± 0.0057 V |
| | | 1 V 10 kHz | 1.01 V | -0.01 V | ± 0.0057 V |
| 2 | 10 V | 10 V 50 Hz | 10.01 V | -0.01 V | ± 0.0065 V |
| | | 10 V 1 kHz | 10.02 V | -0.02 V | ± 0.0065 V |
| | | 10 V 5 kHz | 10.02 V | -0.02 V | ± 0.0065 V |
| | | 10 V 10 kHz | 9.96 V | 0.04 V | ± 0.0065 V |
| 3 | 70 V | 70 V 50 Hz | 70.13 V | -0.13 V | ± 0.046 V |
| | | 70 V 1 kHz | 70.06 V | -0.06 V | ± 0.046 V |
| | | 70 V 5 kHz | 70.01 V | -0.01 V | ± 0.046 V |
| | | 70 V 10 kHz | 69.51 V | 0.49 V | ± 0.045 V |

##### 4.2 DC Voltage Test
| Test No. | UUT Range Setting | Calibrator Output | UUT Indicated Value | Correction | Uncertainty |
|:---:|:---:|:---:|:---:|:---:|:---:|
| 1 | 1 V | 0.00 V | -0.04 V | 0.04 V | ± 0.0023 V |
| | | 0.10 V | 0.07 V | 0.03 V | ± 0.0004 V |
| | | 0.20 V | 0.17 V | 0.03 V | ± 0.0010 V |
| | | 0.40 V | 0.37 V | 0.03 V | ± 0.0021 V |
| | | 0.50 V | 0.47 V | 0.03 V | ± 0.0027 V |
| | | 0.80 V | 0.76 V | 0.04 V | ± 0.0043 V |
| 2 | 10 V | 0.00 V | -0.04 V | 0.04 V | ± 0.0023 V |
| | | 4.00 V | 3.97 V | 0.03 V | ± 0.0022 V |
| | | 9.00 V | 8.96 V | 0.04 V | ± 0.0051 V |
| 3 | 100 V | 0.00 V | -0.04 V | 0.04 V | ± 0.002 V |
| | | 10.00 V | 9.97 V | 0.03 V | ± 0.0056 V |
| | | 20.00 V | 19.96 V | 0.04 V | ± 0.011 V |
| | | 30.00 V | 29.96 V | 0.04 V | ± 0.017 V |
| | | 40.00 V | 39.95 V | 0.05 V | ± 0.023 V |
| | | 50.00 V | 49.95 V | 0.05 V | ± 0.028 V |
| | | 90.00 V | 89.94 V | 0.06 V | ± 0.051 V |

---

## ❓ Antisipasi Pertanyaan Karyawan (FAQ Otomatis)

**Q1: Alat apa yang tertera pada sertifikat kalibrasi ini dan siapa penanggung jawab unitnya?**  
A: Unit yang dikalibrasi adalah *Communication System Analyzer* General Dynamics R8000 dengan nomor seri `800LNY0018`. Unit ini merupakan aset alat ukur operasional milik PT Citra Data Purna Kharisma yang digunakan tim teknisi/engineering di lapangan maupun lab.

**Q2: Kapan masa berlaku sertifikat kalibrasi ini atau kapan harus dikalibrasi ulang?**  
A: Kalibrasi selesai pada 28 Juni 2024 dan sertifikat diterbitkan 05 Juli 2024. Sesuai siklus standar kalibrasi peralatan ukur lab/lapangan (umumnya 1 tahun), unit direkomendasikan untuk dijadwalkan kalibrasi ulang sebelum akhir Juni 2025.

**Q3: Mengapa ada tanda bintang `*) Out Of Spec` di bagian Spectrum Analyzer?**  
A: Tanda tersebut terdapat pada pengujian *Frequency Response Test* di frekuensi 1500 MHz (1.5 GHz), di mana sinyal masukan sebesar -21.029 dBm terbaca oleh alat sebesar -7.5 dBm (koreksi mencapai -13.529 dB). Artinya, pembacaan daya pada spectrum analyzer di frekuensi 1.5 GHz memiliki deviasi melebihi batas toleransi spesifikasi pabrikan.

**Q4: Apakah alat R8000 ini masih aman dan layak dipakai untuk pengujian radio operasional?**  
A: Alat masih sangat presisi dan layak untuk sebagian besar fungsi: Generator RF, Audio/Modulation Monitor (AM & FM), Digital Voltmeter (AC/DC), serta Spectrum Analyzer di rentang frekuensi radio trunking/konvensional standar (VHF 100–400 MHz, UHF 400–800 MHz, dan 1000 MHz). Namun, **hindari** penggunaan fungsi spectrum analyzer pada rentang sekitar 1500 MHz untuk pengukuran level daya absolut, atau pastikan teknisi memperhitungkan faktor koreksi (-13.529 dB).

**Q5: Apakah sertifikat ini diakui secara nasional maupun audit tender resmi?**  
A: Ya. Laboratorium kalibrasi PT Telkom Indonesia Tbk telah terakreditasi KAN dengan kode akreditasi `LK-016-IDN` dan tertelusur secara resmi ke standar SI melalui SNSU-BSN dan Keysight Technologies.

---

## 📚 Glosarium & Istilah Penting

* **CDPK:** PT Citra Data Purna Kharisma, pemilik resmi unit alat ukur yang diajukan kalibrasi.
* **UUT (Unit Under Test):** Instrumen atau perangkat yang sedang diuji atau dikalibrasi (dalam hal ini General Dynamics R8000 S/N: 800LNY0018).
* **KAN:** Komite Akreditasi Nasional, badan akreditasi resmi di Indonesia yang mengakreditasi laboratorium penguji dan kalibrasi (ISO/IEC 17025).
* **LK-016-IDN:** Nomor registrasi akreditasi laboratorium kalibrasi resmi PT Telkom Indonesia Tbk di KAN.
* **SNSU-BSN:** Standar Nasional Satuan Ukuran - Badan Standardisasi Nasional (lembaga metrologi nasional Indonesia).
* **Expanded Uncertainty ($k=2$):** Ketidakpastian pengukuran yang diperluas dengan faktor cakupan $k=2$, merepresentasikan tingkat kepercayaan (*confidence level*) sekitar 95%.
* **Correction (Koreksi):** Nilai yang harus ditambahkan secara aljabar ke hasil penunjukan instrumen agar sesuai dengan nilai standar sebenarnya ($Nilai\ Sebenarnya = Penunjukan\ Alat + Koreksi$).
* **Out Of Spec (OOS):** Kondisi saat nilai pembacaan atau deviasi parameter alat melampaui batas batas toleransi spesifikasi pabrikan.