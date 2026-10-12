# Rencana pilot Grok Bot di Slack

Sumber konteks: chat **Deploy Grokbot Ke Slack** (`6ac5352e-e270-83ec-aa9c-b66e0f3af965`) dan chat implementasi ini. Diperbarui 7 Oktober 2026.

## Tujuan yang disepakati

- Pilot beberapa pengguna di `#ask-grok`, dengan `@mention` dan DM jika didukung.
- Gunakan jalur resmi SuperGrok → Grok Bot → Slack, tanpa xAI API berbayar dan tanpa server atau hosting tambahan.
- Jawaban ringkas, akurat, sesuai bahasa pengguna, menyatakan ketidakpastian, dan menyebut sumber jika tersedia.
- Akses Slack, file, dan knowledge perusahaan dibatasi seminimal mungkin. Uji pemilik dan dua pengguna lain, pemisahan percakapan, izin, serta dampak allowance.
- Jangan membeli seat, mengaktifkan billing, atau melakukan perubahan workspace yang tidak diperlukan. Hentikan rollout jika entitlement SuperGrok pribadi tidak mencakup penggunaan tim.

## Keputusan arsitektur

Team Bot resmi adalah jalur yang diprioritaskan untuk penggunaan multi-user di Slack. Usulan lama untuk menjadikan Grok Bot pribadi sebagai pengguna Slack yang memantau channel lewat browser adalah hipotesis, bukan integrasi resmi, dan tidak dipakai untuk pilot ini. Alternatif free hosting/Ollama juga tidak memenuhi prioritas tanpa server tambahan.

## Temuan implementasi saat ini

- Akun Grok Bot yang aktif: SuperGrok pribadi; pengguna menyatakan tidak memiliki akun Cursor Teams.
- Aplikasi Grok Bot versi 0.68.1 tidak menampilkan **Create new Team Bot**. Bot pribadi Office Boy juga tidak menampilkan **Publish to Team**.
- Menurut dokumentasi resmi, Team Bot di Slack hanya melayani anggota tim yang menautkan akun Slack mereka; penggunaan dihitung ke allowance masing-masing anggota, bukan SuperGrok pemilik.
- Aplikasi **Grok** sudah terpasang di Slack CDPK HQ. Ini adalah integrasi terpisah yang menggunakan xAI API key dan menyediakan kemampuan pencarian workspace yang luas. Riwayat DM menyebut key telah ditambahkan, tetapi status aktif dan billing belum diverifikasi. Jangan mengirim pertanyaan uji melalui aplikasi ini di bawah batas tanpa API.
- Batas on-demand Grok Bot terlihat **None**. Belum ada `#ask-grok`, Team Bot Slack, perubahan scope oleh pekerjaan ini, atau pengujian end-to-end multi-user.
- Instruction pilot pernah dikirim ke chat utama Grok Bot, tetapi bot masih menanyakan bot mana yang harus menerima instruction itu. Instruction belum menjadi konfigurasi Team Bot. Jangan mempublikasikan Office Boy yang memiliki konteks akses pribadi tanpa peninjauan izin terpisah.

## Syarat untuk melanjutkan pilot resmi

1. Ada tim Cursor yang memenuhi syarat dan seat untuk pemilik serta pengguna uji.
2. Buat Team Bot baru tanpa plugin, secret, file, atau konektor perusahaan untuk tahap pertama.
3. Tinjau izin aplikasi Slack sebelum instalasi; undang bot hanya ke `#ask-grok`.
4. Tautkan akun Slack masing-masing pengguna uji dan jalankan checklist pengujian.
5. Catat pemakaian tiap akun dan pastikan tidak ada xAI API call maupun billing tambahan.

Sumber resmi: [Team Bots](https://docs.x.ai/grok-bot/team-bots), [Plans and billing](https://cursor.com/help/grok-bot/plans), [Grok for Slack berbasis API key](https://slack.hooks.x.ai/).
