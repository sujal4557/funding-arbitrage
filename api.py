from fastapi import FastAPI
from scanner import scan
from telegram import send
import threading, time

app = FastAPI()

latest = []

def background():
    global latest
    while True:
        latest = scan()
        for r in latest[:3]:
            send(f"🚨 {r['symbol']} | LONG {r['long']} | SHORT {r['short']} | {r['diff']}%")
        time.sleep(60)

@app.on_event("startup")
def start():
    threading.Thread(target=background, daemon=True).start()

@app.get("/data")
def data():
    return latest
