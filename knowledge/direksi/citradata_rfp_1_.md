### Sheet: Marketing
 | Requirement | Use Case Scenario | Mandatory (Yes/No) | Vendor Response |  |  |  |  |  |  | 
 |  |  |  | Compliance (Fully Comply/ Not Comply/ Partially Complies) |  |  |  | Remarks |  |  | 
1.0 | Integrasi dengan tools finance | Marketing butuh tahu progres lead sampai tahap apa, tapi sering tidak ada update dari sales. Jika terhubung dengan sistem finance, marketing bisa langsung tahu lead mana yang sudah closing.

CRM terintegrasi dengan sistem finance/invoice agar status closing dapat dipantau otomatis oleh marketing. |  | FC |  |  |  | Freshsales Suite menyediakan fitur Lifecycle Stage, dimana kita dapat mencatat status dari masing-masing lead baik itu dari New, Qualified hingga Won. Silahkan temukan referensi artikel mengenai Lifecycle Stage.
https://crmsupport.freshworks.com/support/solutions/articles/50000002542-how-to-manage-lifecycle-stages-and-status-for-contacts-

Freshsales Suite juga menyediakan fitur Workflow, dimana setiap ada perubahan yang dilakukan oleh sales pada status lead dapat dikirimkan ke Sistem Finance/CRM via API. Berikut referensi artikel mengenai fitur Workflow.
https://crmsupport.freshworks.com/support/solutions/articles/50000002143-how-to-configure-a-workflow-

Boleh saya tahu ekspektasi data yang akan dipass antar Sistem Finance/Invoice dengan sistem CRM? 
Apakah sistem Finance/Invoice sudah Open API?

Kalau open api bisa, cuma tergantung mau diintegrasikan nya spt apa, krn itu sdh ke bahasa pemograman |  |  | 
2.0 | Otomatisasi distribusi leads | Saat ini data leads dari ads dipindahkan manual ke satu data lalu dibagi ke sales per wilayah. Proses ini lama dan tidak efisien. 

Sistem CRM yang otomatis mendistribusikan leads berdasarkan kota/wilayah ke sales yang bertanggung jawab. |  | FC |  |  |  | Freshsales Suite menyediakan integrasi dengan Facebook Leads, dimana informasi yang telah disubmit oleh leads akan masuk secara langsung ke sistem CRM tanpa perlu dipindahkan secara manual. Bisa dilihat di artikel referensi dibawah ini.
https://crmsupport.freshworks.com/support/solutions/articles/50000003637-how-to-sync-facebook-leads-with-the-crm-and-use-them-in-marketing-journeys-

Apabila leads yang masuk sudah memiliki informasi lokasi, kita dapat mengoptimalkan fitur Territories. Dengan fitur ini, leads akan secara otomatis dialokasikan kepada sales yang bertugas berdasarkan cakupan wilayah mereka.
https://crmsupport.freshworks.com/support/solutions/articles/50000002702-how-to-create-and-use-territories-

Sesuai diskusi sebelumnya dengan Pak Adrian sebelumnya, untuk Ads yang dicantumkan melalui Instagram maupun Facebook akan redirect leads untuk mengisi informasi tersebut menggunakan Form yang telah digenerate melalui Facebook. Apakah bisa dibantu konfirmasinya terkait hal ini?

Juga, boleh kami tahu ada berapa Facebook yang saat ini digunakan untuk generate leads? 1 |  |  | 
3.0 | Integrasi WhatsApp | Leads yang masuk via WhatsApp sering tidak tercatat jika hanya melalui chat, sehingga data hilang dan tidak ter-track.

Integrasi WhatsApp ke CRM agar setiap chat masuk otomatis tercatat sebagai lead beserta riwayat komunikasinya. |  | FC |  |  |  | Freshsales Suite menyediakan integrasi dengan WhatsApp Business API, maupun sosial media seperti Instagram maupun Facebook. Semua percakapan yang masuk akan direcord di masing-masing contact. 
https://crmsupport.freshworks.com/support/solutions/articles/50000004438-overview-of-whatsapp-business-integration

Boleh saya tahu apakah percakapan yang masuk dari WhatsApp akan dihandle oleh siapa? Dan bagaimana action selanjutnya untuk leads yang telah menghubungi melalui WhatsApp tersebut?
- Sales, namun berencana telemarketing 
- Follow up, penawaran, demo, penjualan |  |  | 
4.0 | WhatsApp Broadcast & Nurturing | Leads sudah masuk, tapi belum ada alur nurturing yang jelas dan terstruktur.

Sistem broadcast dan nurturing (edukasi, reminder, follow-up) berbasis CRM untuk menjaga lead tetap hangat sebelum dan sesudah di-handle sales. |  | FC |  |  |  | Untuk menjalakan WhatsApp Broadcast kepada leads dengan tujuan nurturing ataupun lainnya, Freshsales menyediakan fitur Customer Journey yang dapat diset oleh tim Marketing untuk menjalankan campaign sesuai dengan kebutuhan. Tim Marketing dapat menentukan siapa saja list PIC yang akan dihubungi dan konten message yang akan disiapkan ketika melakukan proses broadcast
https://crmsupport.freshworks.com/support/solutions/articles/50000002625-how-to-configure-a-marketing-journey-

Perlu diperhatikan bahwa untuk broadcasting akan ada mengonsumsi Marketing Contact, dimana akan diberikan 500 Marketing Contact dari sisi Freshsales Suite setiap bulannya, apabila pengiriman broadcast melebihi 500, maka akan ada biaya tambahan sebesar $100 untuk setiap 5000 Marketing Contact.
 https://crmsupport.freshworks.com/support/solutions/articles/50000003081-what-are-marketing-contacts-how-are-they-measured- |  |  | 

### Sheet: Sales
No | Requirement | Use Case Scenario | Mandatory (Yes/No) | Vendor Response |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  | 
 |  |  |  | Compliance (Fully Comply/ Not Comply/ Partially Complies) |  |  |  | Remarks |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  | 
1.0 | Status leads | 1. data source leads dari platform apa? leads dari campaing apa? agar terfokus dan segmented
2. stage leads udah ditahap apa (new, contacted (ada tanggalnya), qualified, proposal, closing, dan lost
3. input manual leads atau calon cust dari sales langsung |  | FC |  |  |  | 1. Contact dapat digunakan untuk mencatat informasi leads yang msauk berasal dari platform maupun campaign yang telah dibuat. Apabila ada kebutuhan untuk mencatat informasi lainnya, field dapat dikustomisasi sesuai dengan kebuuthan bisnis.
https://crmsupport.freshworks.com/support/solutions/articles/50000002373-how-to-add-and-use-contacts- 

2. Lifecycle Stage yang terdapat didalam modul contact dapat digunakan oleh sales untuk menentukan tahapan dari masing-masing leads dan tahapan tersebut dapat dikustomisasi.
https://crmsupport.freshworks.com/support/solutions/articles/50000002542-how-to-manage-lifecycle-stages-and-status-for-contacts-

3. Sales dapat menambahkan leads secara langsung melalui fitur Add Contact, ketika menambahkan leads baru sales juga dapat menambahkan maka informasi dari leads tersebut. Apabila dari sisi sales memiliki data lead dalam format CSV/Excel, sales dapat import data tersebut secara langsung ke platform Freshsales Suite.
https://crmsupport.freshworks.com/support/solutions/articles/50000002373-how-to-add-and-use-contacts- 

Silahkan temukan pertanyaan saya dibawah ini.
2. Apakah tanggal contacted ini akan diupdate secara terus menerus mengikuti tanggal dimana contact telah dihubungi? (iya, sebagai bukti ke marketing bahwa leads telah dihubungi sales)
>> Custom Field pada Contact dapat ditambahkan agar sales bisa mencatat informasi tanggal terakhir kontak tersebut dihubungi. |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  | 
2.0 | riwayat kontak, aktivitas, history | 1. Data cust (nama, jabatan, nomor, email, industri, wilayah)
2. Contacted by (telp, wa, email, meeting) - update dengan tanggal
3. reminder otomatis sudah berapa lama tidak follow up leads dan pelanggan
4. susun jadwal follow up dan pertemuan (integrasi dengan google calendar)
5. Catatan aktivitas atau point-point follow up selanjutnya
6. dashboard customer (catatan, customer own by sales siapa, pain point customer, total penjualan, status customer (new, silver, golden, platinum) |  | FC |  |  |  | 1. Contact dapat digunakan untuk mencatat informasi detail leads yang seperti nama, nomor, email, industri maupun wilyah. Apabila ada kebutuhan untuk mencatat informasi lainnya, field dapat dikustomisasi sesuai dengan kebuuthan bisnis.
https://crmsupport.freshworks.com/support/solutions/articles/50000002373-how-to-add-and-use-contacts- 

2. Pencatatan pada Contact dapat menggunakan Custom Field agar sales bisa menambahkan informasi tanggal terakhir kontak dihubungi beserta channel yang digunakan untuk menghubungi contact tersebut. Fitur Opsional seperti Track Field History juga tersedia di Freshsales Suite untuk mendapatkan history update yang telah dilakukan oleh sales pada field contact. Untuk fitur ini tersedia di Plan Enterprise.
https://crmsupport.freshworks.com/support/solutions/articles/50000006313-how-to-track-field-history-of-contacts-and-accounts-

4. Freshsales Suite menyediakan integrasi dengan Google Calendar dimana jadwal seperti follow up maupun meeting dapat disinkronisasikan secara langsung.
https://crmsupport.freshworks.com/support/solutions/articles/50000002453-how-to-sync-my-google-calendar

5. Semua aktivitas sales yang telah dilakukan pada masing-masing leads akan tercatat di detail contact, apabila ada catatan tambahan pada leads bisa kita catat di Notes.
https://crmsupport.freshworks.com/support/solutions/articles/50000002427-how-to-add-notes-in-freshsales-

6. Freshsales Suite menyediakan tampilan detail pada leads mulai dari Aktivitas, Notes (Catatan/Pain Point) Sales Owner, beserta informasi detail yang dibutuhkan dari sisi bisnis.
https://crmsupport.freshworks.com/support/solutions/articles/50000009061-how-to-get-a-360-degree-view-of-customers-contacts-module-

Silahkan temukan pertanyaan saya dibawah ini.
2. Untuk Contacted By, apakah ini diupdate secara manual oleh sales yang memegang leads tersebut? Apakah poin ini refer ke Status Leads di use case skenario 2? (iya di update manual oleh sales yg memegang leads tersebut, iya refer ke use case skenario 2)
>> Custom Field pada Contact dapat ditambahkan agar sales bisa mencatat informasi tanggal terakhir kontak tersebut dihubungi beserta channel yang digunakan untuk menghubungi kontak tersebut.

3. Boleh saya tahu reminder ini akan dikirimkan setelah berapa lama leads atau customer tidak difollow up? Dan apakah ada kriteria tertentu untuk reminder yang ingin dikirimkan kepada sales? (iya, estimasi reminder minimal 2 minggu - maksimal 1 bulan sekali. Reminder notifikasi dan mungkin bisa jadi highlight dalam pagenya kalau leads mana saja yg butuh di follow up)
>> Dengan menggunakan Workflow, sistem dapat membuat task/mengirimkan email kepada Sales apabila kontak tidak dihubungi lebih dari 2 minggu pada stages tertentu. |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  | 
3.0 | Pipeline & forecast | 1. Status pipeline untuk project maupun retail (prospect, qualified, proposal, negotiation, closed) - bisa masukin dokumen2 setiap stage 
2. estimasi nilai project
3. persentase closing
4. Tracking target sales
5. forecast otomatis dari pipeline
6. Kontrak2 project dan renewal reminder otomatis
7. integrasi ke daftar dan qty produk-produk yang di pipeline dan forecast
8. otomasi estimasi target dari pipeline dan forecast (seluruh perusahaan dan per sales) |  | PC |  |  |  | 1. Modul Deals pada Freshsales Suite menyediakan multiple Pipeline yang dapat dikustomisasi untuk tahapannya. Masing-masing deals yang telah dibuat dapat menambahkan dokumen yang terkait, akan tetapi dokumen tersebut tidak dapat dipisahkan untuk setiap stages.
https://support.freshsales.io/support/solutions/articles/228353-how-to-configure-multiple-deal-pipelines-

2. Estimasi Harga/Nilai Project dapat diinput oleh sales pada saat pembuatan deals.

3. Setiap tahapan/stage yang telah dibuat dapat dikustomisasi untuk persentase closingnya.
https://crmsupport.freshworks.com/support/solutions/articles/50000002392-how-to-customize-deal-stages-

4. Freshsales Suite menyediakan fitur Quotas yang dapat menentukan target dari masing-masing sales. 

5. Freshsales Suite menyediakan fitur Forecasting untuk memprediksi estimasi pendapatan secara akurat dengan memantau peluang closing dari setiap deals yang sedang berjalan di seluruh tahapan sales pipeline.
https://crmsupport.freshworks.com/support/solutions/articles/50000002881-how-to-predict-revenue-from-your-team-on-freshworks-crm-

6. Freshsales Suite menyediakan fitur Custom Module yang dapat digunaan untuk mencatat kontrak seperti tanggal kontrak dibuat, masa berakhir kontrak yang dapat dikustomisasi.

Silahkan temukan pertanyaan saya dibawah ini.
6. Boleh saya tahu kapan Renewal reminder ini akan dikirimkan ke sales? (Setiap kontrak project akan berakhir, misal project running 2 tahun sekali, akan ada renewal project reminder minimal 1 tahun dan maksimal 6 bulan sebelum kontrak project benar-benar berakhir)
>> Dengan menggunakan Custom Module, informasi kontrak seperti tanggal pembuatan kontrak, tanggal berakhir masa kontrak dapat dicatat di dalam Freshsales Suite. Reminder ini juga dapat dikirimkan kepada Sales via email apabila masa berakhir kontrak sudah mendekati jangka waktu yang telah ditentukan.

7. Apakah qty produk ini merupakan integrasi antar sistem internal untuk produk-produk yang tersedia di Freshsales Suite? (iya)
>>  Pencatatan Quantity pada produk dapat diakomodasi melalui penggunaan custom field pada fitur Product Catalogue. Namun, perlu diperhatikan bahwa Freshsales Suite tidak dapat melakukan update stock secara otomatis (penambahan atau pengurangan) berdasarkan transaksi pada deals. Informasi quantity hanya tersedia sebagai data referensi yang dapat diakses langsung melalui Product Catalogue atau saat produk tersebut telah dikaitkan ke dalam suatu deal.

8. Apakah data yang ingin didapatkan merupakan target estimasi untuk total nilai project yang ditargetkan beserta achievement dari masing-masing sales di report? Juga, apakah boleh dibantu elaborasi maksud dari "Seluruh perusahaan"?(iya, untuk maksud dari seluruh perusahaan dapat melihat estimasi revenue tahunan perusahaan)
>> Freshsales Suite menyediakan fitur Analytics, dimana data terhadap Deals yang sudah Won maupun Lost bisa didapatkan melalui Report secara langsung. |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  | 
4.0 | Tracking | 1. Platform yang cepat dan ringkas agar bisa update dan follow up sambil di jalan (bisa langsung pakai hp)
2. Notifikasi
3. Delegasi ke sales lain (jika berhalangan masuk kantor) by approval ybs dan manager |  | PC |  |  |  | 1. Freshsales Suite menyediakan Mobile Apps yang dapat diakses oleh sales untuk melakukan update terhadap aktivitas aktivitas seperti follow up, visit ataupun detail informasi kontak secara langsung. 
https://play.google.com/store/apps/details?id=com.freshdesk.freshsales.mobile&hl=en

2. Notifikasi juga dapat dikirimkan kepada sales melalui mobile app apabila ada aktivitias sales yang sudah mendekati waktunya seperti follow up maupun visit.
https://support.freshsales.io/support/solutions/articles/217650-how-to-set-notification-alerts-

3. Freshsales Suite tidak tersedia fitur Approval.

Silahkan temukan pertanyaan saya dibawah ini.
3. Apakah ini refer ke leads akan ditransfer sementara ke sales lain dan akan ditransfer kembali kepada sales yang bersangkutan ketika sudah masuk kantor? (betul)
>> Untuk fitur Approval saat ini tidak tersedia, akan tetapi supervisor dapat melakukan menambahkan Sales ke Leads yang saat ini dipegang oleh Sales YBS dengan menggunakan Contact Team. Supervisor dapat melakukan removal dari sales tersebut apabila Sales YBS sudah kembali masuk ke kantor menggunakan Contact Team. Perlu diperhatikan fitur ini tersedia di plan Enterprise.
https://crmsupport.freshworks.com/support/solutions/articles/50000002416-how-to-create-and-use-record-teams-#:~:text=Note:%20When%20you%20disable%20permissions,run%20based%20on%20set%20conditions. |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  | 
5.0 | Quotation | 1. Upload penawaran dan dokumen dukungan (biar terupdate penawaran terakhir)
2. status quotation (sent, viewed, revised, approved, terbit po) |  | PC |  |  |  | 1. Boleh saya tahu dimana Quotation ini akan diterbitkan? (quotation resmi diterbitkan dari platform Accurate, namun kita disini hanya masukkan dokumen Quotation saja sebagai tracking)
>> Untuk menambahkan file quotation di masing-masing Deals dapat dilakukan, namun untuk masing-masing files yang telah ditambahkan tidak dapat mencatat status dari Quotation tersebut. Sebagai workaround, Custom Field dapat ditambahkan agar dapat mencatat status Quotation yang saat ini berjalan. |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  | 
6.0 | Data produk dan harga | 1. update data produk (new dan discontinue), saran penggantinya yg terbaru, dan saran produk serupa
2. update harga (harga promo marketing, harga ecer, harga grosir, harga standar dealer/partner/user, harga terbawah, harga teratas)
3. data peminjaman produk dari gudang untuk demo presentasi sales (status pengajuan, waktu peminjaman, dan pemulangan) |  | PC |  |  |  | Freshsales Suite menyediakan fitur Product untuk mencatat product yang saat ini tersedia dari sisi Bisnis dan bisa direlasikan dengan Modul Deals. Harga dari dan diskon pada product juga dapat dirubah oleh ketika menambahkan informasi product. https://support.freshsales.io/support/solutions/articles/50000001828-how-to-add-and-use-products-

Silahkan temukan pertanyaan dibawah ini.
1. Boleh dibantu elaborasi lebih lanjut maksud dari saran penggantinya beserta saran produk serupa? (Produk teknologi banyaknya menyesuaikan solusi usernya, sehingga ada beberapa produk yang sudah discontinue/stock sedang kosong, ada pilihan langsung dari platform untuk beberapa produk yang serupa, ini bisa memudahkan sales baru untuk mengetahui lebih cepat)
>> Terkait Product sudah Discontinue/On Stock, informasi ini dapat dicatat pada Product Catalog yang telah ditambahkan. Sales juga dapat melihat detail tersebut ketika Product sudah ditambahkan pada Deals. Saran untuk produk serupa yang dapat ditambahkan oleh sales saat ini masih belum memungkinkan.

2. Product Catalogue tidak dapat menambahkan penawaran harga yang berbeda-beda untuk tipe user yang berbeda-beda. Akan tetapi, ketika sales menambahkan informasi product pada Deals, sales dapat merubah harga beserta menambahkan diskon untuk total harga yang ditawarkan.

3. Boleh saya tahu flow/ekspektasi data peminjaman ini akan dicatat seperti apa di sistem Freshsales Suite?
>> Untuk pencatatan data peminjaman pada sistem Freshsales Suite tidak possible untuk dilakukan. |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  | 
7.0 | Program marketing | 1. highlight program marketing
2. S&K program marketing
3. persentase minat program dan persentase won dari program marketing
4. upcoming program & event marketing |  | FC |  |  |  | Freshsales Suite menyediakan fitur Customer Journey yang dapat melakukan pengiriman Campaign seperti Email maupun WhatsApp Blasting kepada segmentasi leads yang sudah ditentukan.

Silahkan temukan pertanyaan saya dibawah.
1. Boleh dibantu dijelaskan lebih lanjut terkait S&K Program Marketing? (program marketing punya syarat & ketentuan untuk internal mengetahui proses claim programnya, sehingga bisa membantu marketing jika customer memiliki pertanyaan terkait programnya. Maksud saya dalam kolom program marketing ini, digunakan untuk kepentingan internal dalam divisi sales agar teredukasi terkait program marketing yg akan dan sedang berjalan untuk di follow up lebih lanjut oleh sales ke customer, dan bagaimana feedback customer terhadap program marketing yg sedang berjalan)
>> Untuk membantu Tim sales dalam menjawab pertanyaan program marketing, Freshsales Suite menyediakan fitur FAQ yang dapat dijadikan sebagai panduan oleh Sales untuk menjawab  pertanyaan dari customer. Canned Response juga dapat digunakan untuk mengirimkan response template untuk memudahkan sales dalam mengirimkan jawaban template yang telah tersedia.
https://crmsupport.freshworks.com/support/solutions/articles/50000003077-how-to-create-faqs-
https://crmsupport.freshworks.com/support/solutions/articles/50000004372-canned-responses-in-freshchat |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  | 
8.0 | service | 1. status barang (cover garansi atau tidak)
2. serial number (tracking pembelian kapan) - berhubungan dengan status garansi
3. dashboard follow up dengan divisi workshop
4. input data barang rusak dari pabrik/gudang setelah penjualan (untuk cek persentase barang cacat setiap pengiriman dari motorola atau barang rusak karna usang di gudang) (nama produk, partnumber, serial number, kondisi barang, umur barang dari gudang, dan durasi barang selama di customer sejak barang diterima) |  | PC |  |  |  | Custom Module pada Fsales Suite memungkinkan sales mencatat informasi spesifik seperti detail layanan (service) dan status garansi yang dapat dikustomisasi sepenuhnya; fitur ini tersedia pada Plan Enterprise dengan kapasitas hingga 10 custom module.
https://crmsupport.freshworks.com/support/solutions/articles/50000002401-what-are-custom-modules-how-to-add-a-new-module-

Silahkan temukan pertanyaan saya dibawah ini.
Boleh saya tahu flow yang kerja yang berjalan untuk informasi Services? Juga, bagaimana proses follow up dengan divisi workshop? 
(Flow saat ini:
1. Unit service datang ke kantor dan dicatat admin sales menggunakan form secara manual (untuk garansi, biasanya customer bilang ini barang masih baru) - disini kadang tidak terdeteksi barang apakah benar-benar masih dalam garansi atau tidak karna perlu konfirmasi lagi ke tim gudang apakah barang ini dikeluarkan oleh kita atau kapan barang ini keluar di penjualan dengan tracking serial number
2. Unit dalam antrian untuk diperiksa workshop
3. setelah unit diperiksa, divisi workshop akan update status kerusakan dan mengeluarkan quotation service di catat di spreadsheet (disini juga ada beberapa unit service yang harus dioper ke motorola pusat, ada barang yang diganti baru sehingga serial number juga berganti)
4. Admin sales follow up ke customer apakah setuju akan diperbaiki atau tidak, dan beberapa perusahaan perlu mengeluarkan PO Service
5. Customer setuju dan mengeluarkan PO
6. Admin sales mengeluarkan Proforma Invoice terlebih dahulu untuk pembayaran (Service wajib bayar sebelum dikerjakan, hanya sedikir case yg TOP)
7. Customer membayar, dan menunggu antrian untuk dikerjakan
8. Workshop informasi barang sudah selesai, admin sales konfirmasi ke customer untuk diambil ke kantor

>> Apakah bisa dibantu share Sampel Data beserta cara pencatatan yang saat ini dilakukan untuk status barang yang sudah terjual? |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  | 