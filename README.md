# 🤖 Nexus AI Engine

Aplikasi chatbot AI web berbasis **Flask** dan **Google Gemini 3.6 Flash** dengan fitur *streaming response* real-time dan antarmuka *dark mode* modern.

## 📂 Struktur Proyek

```text
Nexus-Ai-/
├── app.py
└── templates/
    └── index.html

✨ Fitur Utama
Real-Time Streaming: Balasan AI dikirim secara langsung menggunakan client.models.generate_content_stream.

Typewriter Queue Engine: Efek pengetikan halus per karakter di frontend dengan antrean JavaScript (setTimeout render queue).

Dark Theme UI: Tampilan chat card futuristik dengan animasi slide-in, avatar glow, dan custom scrollbar biru.

Quick Suggestion Chips: Tombol shortcut untuk mengajukan pertanyaan umum secara cepat.

Error Handling: Penanganan otomatis untuk status Rate Limit (429) dan error koneksi backend.

🛠️ Tech Stack
Backend: Python 3.x, Flask, google-genai

Frontend: HTML5, CSS3, JavaScript (Fetch & Stream API), FontAwesome 6

🚀 Cara Menjalankan
Instal Library Python:

Bash
pip install flask google-genai
Jalankan Aplikasi:

Bash
python app.py
Buka di Browser:
Akses http://127.0.0.1:5000 di browser kamu.
