# Knowledge Base CDPK HQ

Direktori ini berisi seluruh basis pengetahuan resmi tim CDPK HQ dalam format Markdown (`.md`), yang terbagi ke dalam subfolder khusus berdasarkan kategori hak akses (3-Tier RBAC):

## Struktur Subfolder Kategori Akses:

```text
knowledge/
├── direksi/        # Khusus DIREKSI (Folder 'Slack - Khusus Direksi', Dokumen 'Gaji', Dividen, Legalitas Direksi)
├── finance/        # Khusus FINANCE & DIREKSI (Folder 'Slack - Finance', 'Finance & Accounting', 'Order Management')
├── umum/           # SEMUA MEMBER (SOP Operasional, FMTCS, IMS Citradata, Produk i.Safe Mobile, POCStar, SafeUEM, Sales, dll)
└── README.md
```

## Mekanisme Keamanan Zero-Trust:
1. **Isolasi Data Level Folder**:
   - Staf Umum hanya memuat dokumen dari `knowledge/umum/`. Dokumen dari `finance/` dan `direksi/` sama sekali tidak pernah dikirim ke konteks prompt AI.
   - Tim Finance memuat dokumen dari `knowledge/umum/` dan `knowledge/finance/`.
   - Direksi memuat seluruh dokumen (`umum/`, `finance/`, dan `direksi/`).
2. **Mandat Gemini 3.8 Flash**:
   - Seluruh dokumen dikonversi dengan menyertakan Frontmatter YAML (`sumber_dokumen`, `folder_asal`, `tingkat_akses`), Executive Summary, Salinan Lengkap tanpa sensor angka/gaji, FAQ Otomatis, dan Glosarium.
