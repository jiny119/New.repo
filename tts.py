from http.server import BaseHTTPRequestHandler
from gtts import gTTS
import json
import base64
from io import BytesIO  # نئی لائبریری

class Handler(BaseHTTPRequestHandler):
    def do_OPTIONS(self):  # نیا میتھڈ
        self.send_response(200)
        self.send_header("Access-Control-Allow-Origin", "*")
        self.send_header("Access-Control-Allow-Methods", "POST, OPTIONS")
        self.send_header("Access-Control-Allow-Headers", "Content-Type")
        self.end_headers()

    def do_POST(self):
        try:
            content_length = int(self.headers["Content-Length"])
            post_data = self.rfile.read(content_length)
            data = json.loads(post_data)
            text = data["text"]

            # میموری میں آواز بنائیں
            tts = gTTS(text=text, lang="ur", slow=False)
            audio_buffer = BytesIO()
            tts.write_to_fp(audio_buffer)
            
            audio_base64 = base64.b64encode(audio_buffer.getvalue()).decode("utf-8")

            self.send_response(200)
            self.send_header("Content-type", "application/json")
            self.send_header("Access-Control-Allow-Origin", "*")
            self.send_header("Access-Control-Allow-Methods", "POST, OPTIONS")  # نئے ہیڈر
            self.send_header("Access-Control-Allow-Headers", "Content-Type")  # نئے ہیڈر
            self.end_headers()
            self.wfile.write(json.dumps({"audio": f"data:audio/mp3;base64,{audio_base64}"}).encode())
            
        except Exception as e:
            self.send_response(500)
            self.send_header("Content-type", "application/json")
            self.end_headers()
            self.wfile.write(json.dumps({"error": f"Server error: {str(e)}"}).encode())
