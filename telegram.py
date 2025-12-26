import requests, os

TOKEN = os.getenv("8564253749:AAE6jcZeKBvL54g662-cJ-kgoWi046YJ0Z0")
CHAT = os.getenv("1086680348")

def send(msg):
    if not TOKEN or not CHAT:
        return
    requests.post(
        f"https://api.telegram.org/bot{TOKEN}/sendMessage",
        json={"chat_id": CHAT, "text": msg}
    )
