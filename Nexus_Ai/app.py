from flask import Flask, render_template, request, Response
from google import genai
from google.genai import types

app = Flask(__name__)

# 🔑 API KEY 
API_KEY = "AQ.Ab8RN6I2m4zIrU8jQ3hpc_fYnuc-_-kzLcvbfki5CTQHX1Zjkw"
client = genai.Client(api_key=API_KEY)

@app.route("/")
def home():
    return render_template("index.html")

@app.route("/stream", methods=["POST"])
def stream():
    data = request.get_json()
    user_message = data.get("msg", "").strip()

    if not user_message:
        return Response("Pesan tidak boleh kosong!", mimetype="text/plain")

    def generate():
        try:
            response = client.models.generate_content_stream(
                model="gemini-3.6-flash",
                contents=user_message,
                config=types.GenerateContentConfig(
                    system_instruction="Kamu adalah Nexus AI. Jawab pertanyaan user dengan santai, cerdas, ramah, dan rapi."
                )
            )
            for chunk in response:
                if chunk.text:
                    yield chunk.text
        except Exception as e:
            err_msg = str(e)
            if "429" in err_msg:
                yield "⚠️ Batas kuota tercapai (Rate Limit)! Tunggu 1–2 menit lalu coba lagi ya."
            elif "404" in err_msg:
                yield "⚠️ Model AI sedang tidak tersedia, coba beberapa saat lagi."
            else:
                yield f"⚠️ Terjadi kesalahan: {err_msg}"

    return Response(generate(), mimetype="text/plain")

if __name__ == "__main__":
    app.run(debug=True)