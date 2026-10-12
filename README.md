# Grok Slack Bot untuk CDPK HQ

Integrasi bot Slack resmi menggunakan xAI Grok API (`grok-2` / `grok-2-mini`) dengan Slack Socket Mode.

## Fitur
- **Socket Mode**: Tanpa perlu IP publik atau ngrok.
- **Thread Context**: Bot mengingat hingga 10 pesan riwayat di thread yang sama.
- **Direct Message**: Dapat dihubungi via DM 1-on-1.
- **Thinking Indicator**: Menampilkan emoji reaksi saat sedang memproses respon dari Grok.

## Cara Menjalankan

1. **Salin file environment:**
   ```bash
   cp .env.example .env
   ```
2. **Isi variabel di `.env`:**
   - `SLACK_BOT_TOKEN` (`xoxb-...`)
   - `SLACK_APP_TOKEN` (`xapp-...`)
   - `XAI_API_KEY` (`xai-...`)

3. **Install dependensi:**
   ```bash
   python3 -m venv venv
   source venv/bin/activate
   pip install -r requirements.txt
   ```

4. **Jalankan Bot:**
   ```bash
   python3 app.py
   ```
