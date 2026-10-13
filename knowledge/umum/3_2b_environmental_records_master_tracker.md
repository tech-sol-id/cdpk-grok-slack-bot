### Sheet: B3 Log Summary
ENVIRONMENTAL RECORDS MASTER TRACKER — B3 LOG SUMMARY |  |  |  |  |  |  |  |  |  |  |  |  | 
Agregat dari FR-ENV-001 (B3 Generation & TPS Log) — jumlah per jenis limbah B3 per bulan |  |  |  |  |  |  |  |  |  |  |  |  | 
Jenis Limbah B3 | Jan | Feb | Mar | Apr | Mei | Jun | Jul | Agu | Sep | Okt | Nov | Des | Total
Baterai Li-ion | 0 | 0 | 0 | 0 | 0 | 0 | 0 | 0 | 0 | 0 | 0 | 0 | 0
PCB & Komponen Elektronik | 0 | 0 | 0 | 0 | 0 | 0 | 0 | 0 | 0 | 0 | 0 | 0 | 0
Kimia Cair (IPA/Flux bekas) | 0 | 0 | 0 | 0 | 0 | 0 | 0 | 0 | 0 | 0 | 0 | 0 | 0
E-waste BER | 0 | 0 | 0 | 0 | 0 | 0 | 0 | 0 | 0 | 0 | 0 | 0 | 0
Lain-lain | 0 | 0 | 0 | 0 | 0 | 0 | 0 | 0 | 0 | 0 | 0 | 0 | 0
Total per Bulan | 0 | 0 | 0 | 0 | 0 | 0 | 0 | 0 | 0 | 0 | 0 | 0 | 0
Catatan: Update angka bulanan secara manual berdasarkan rekap FR-ENV-001. Sel ini terhubung ke total otomatis. |  |  |  |  |  |  |  |  |  |  |  |  | 

### Sheet: E-Waste & Manifest Tracker
E-WASTE & MANIFEST B3 TRACKER |  |  |  |  |  |  | 
Status seluruh manifest B3 (FR-ENV-003) — ALERT otomatis jika Lembar 7 belum diterima > 90 hari |  |  |  |  |  |  | 
No. Manifest | Tanggal Kirim | Jenis B3 / E-waste | Volume | Vendor | Tgl Lembar 7 Diterima | Hari Berjalan | Status
Legenda Status: |  |  |  |  |  |  | 
Diterima = Lembar 7 sudah kembali | Pending = belum 90 hari | ALERT >90 HARI = mendekati batas | OVERDUE = >120 hari, wajib lapor KLHK |  |  |  |  |  |  | 

### Sheet: Incident & Drill Log
ENVIRONMENTAL INCIDENT & DRILL LOG |  |  |  |  |  | 
Rekap dari FR-ENV-004 (Incident Report) dan FR-ENV-005 (Emergency Drill Record) |  |  |  |  |  | 
A. INCIDENT LOG |  |  |  |  |  | 
No. Insiden | Tanggal | Lokasi | Deskripsi Singkat | Lapor Regulasi? | No. CAPA | Status
B. EMERGENCY DRILL LOG |  |  |  |  |  | 
Tanggal | Jenis Simulasi | Lokasi/Workshop | Jumlah Peserta | Tindak Lanjut Terbuka? | Status | 

### Sheet: Chemical Inventory Digital
CHEMICAL INVENTORY & SDS REGISTER (DIGITAL) |  |  |  |  |  |  |  |  |  | 
Versi digital dari FR-ENV-007 — ALERT otomatis jika SDS mendekati/melewati masa berlaku (asumsi review 3 tahun) atau stok mendekati kadaluarsa |  |  |  |  |  |  |  |  |  | 
Nama Bahan Kimia | Supplier | No. SDS | Tgl SDS | Lokasi Penggunaan | Kompatibilitas ATEX | Kode B3 | Volume Stok | Tgl Kadaluarsa | Status SDS | Status Stok
IPA 70%/99% | PT Kimia Sejahtera | SDS-IPA-001 | 2024-01-15 | Workshop i-safe, Joy Factory, Motorola | Ya | B3 Cair | 20 | 2027-01-15 | Valid | Valid
Flux Remover | PT Kimia Sejahtera | SDS-FLX-002 | 2024-01-15 | Workshop i-safe, Joy Factory | Perlu verifikasi | B3 Cair | 10 | 2026-12-01 | Valid | Valid
Contact Cleaner | PT Elektro Chemical | SDS-CC-003 | 2023-06-10 | Workshop Motorola | Tidak | B3 Cair | 8 | 2026-08-01 | EXPIRED - REVIEW | Valid
Thermal Paste | PT Elektro Chemical | SDS-TP-004 | 2024-03-01 | Workshop i-safe, Joy Factory, Motorola | Ya | Non-B3 | 5 | 2028-03-01 | Valid | Valid
Review wajib setiap 6 bulan sesuai FR-ENV-007. Status SDS dihitung otomatis dari Tgl SDS (asumsi masa berlaku internal 3 tahun / 1095 hari). |  |  |  |  |  |  |  |  |  | 

### Sheet: Environmental KPI Dashboard
ENVIRONMENTAL KPI DASHBOARD |  |  |  |  |  | 
Terhubung ke EO-001 (Environmental Objectives) — status RAG (Red-Amber-Green) otomatis berdasarkan capaian vs target |  |  |  |  |  | 
Kode Objective (ref EO-001) | Deskripsi KPI | Target | Realisasi Saat Ini | Satuan | % Capaian | Status RAG
EO-001-01 | Pengurangan volume limbah B3 per unit servis | 5 | 0 | % YoY | 0 | RED
EO-001-02 | Tingkat ketepatan waktu pengembalian Lembar 7 Manifest | 100 | 0 | % | 0 | RED
EO-001-03 | Insiden lingkungan signifikan | 0 | 0 | kejadian |  | Belum ada data
EO-001-04 | Pelaksanaan simulasi tanggap darurat | 2 | 0 | kali/tahun | 0 | RED
EO-001-05 | SDS bahan kimia ter-review tepat waktu | 100 | 0 | % | 0 | RED
EO-001-06 | Unit e-waste BER dengan Certificate of Destruction lengkap | 100 | 0 | % | 0 | RED
Catatan: Untuk KPI 'Insiden lingkungan signifikan', capaian dihitung terbalik (semakin rendah realisasi semakin baik). |  |  |  |  |  | 
Update Realisasi Saat Ini secara berkala (disarankan bulanan) untuk menjaga akurasi dashboard. |  |  |  |  |  | 