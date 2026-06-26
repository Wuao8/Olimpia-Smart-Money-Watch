from fastapi import FastAPI
from fastapi.middleware.cors import CORSMiddleware

from engine.smart_money import get_all_signals

app = FastAPI(title="Olimpia Smart Money Watch")

app.add_middleware(
    CORSMiddleware,
    allow_origins=["*"],
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"],
)


@app.get("/")
def home():
    return {
        "project": "Olimpia Smart Money Watch",
        "status": "online"
    }


@app.get("/api/live")
def live():

    signals = get_all_signals()

    return {
        "signals": [
            vars(signal)
            for signal in signals
        ]
    }
