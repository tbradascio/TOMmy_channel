from fastapi import FastAPI
import os, requests

app = FastAPI()

TOKEN = os.environ["TG_BOT_TOKEN"]
CHAT_ID = os.environ["TG_CHAT_ID"]

def send_message(text: str):
    url = f"https://api.telegram.org/bot{TOKEN}/sendMessage"
    payload = {"chat_id": CHAT_ID, "text": text, "parse_mode": "HTML"}
    requests.post(url, data=payload, timeout=10)

@app.get("/")
def health():
    return {"ok": True, "service": "TOMmy API"}

@app.get("/notify")
def notify(msg: str = "🚀 Test da Render!"):
    send_message(msg)
    return {"sent": msg}