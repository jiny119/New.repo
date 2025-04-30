from http.server import BaseHTTPRequestHandler
from gtts import gTTS
import json
import base64

class Handler(BaseHTTPRequestHandler):
    def do_POST(self):
        content_length = int(self.headers["Content-Length"])
        post_data = self.rfile.read(content_length)
        data = json.loads(post_data)
        text = data["text"]

        # ٹیکسٹ کو آواز میں تبدیل کریں (اردو)
        tts = gTTS(text=text, lang="ur", slow=False)
        tts.save("output.mp3")
        with open("output.mp3", "rb") as audio_file:
            audio_base64 = base64.b64encode(audio_file.read()).decode("utf-8")

        self.send_response(200)
        self.send_header("Content-type", "application/json")
        self.send_header("Access-Control-Allow-Origin", "*")
        self.end_headers()
        self.wfile.write(json.dumps({"audio": f"data:audio/mp3;base64,{audio_base64}"}).encode())
