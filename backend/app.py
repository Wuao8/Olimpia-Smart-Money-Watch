from fastapi import FastAPI
from fastapi.middleware.cors import CORSMiddleware

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

    return {
        "signals": [
            {
                "market": "Crypto",
                "asset": "BTC",
                "action": "BUY",
                "size": "25 M$",
                "who": "-----",
                "source": "Demo"
            },
            {
                "market": "Stocks",
                "asset": "AAPL",
                "action": "BUY",
                "size": "800 K$",
                "who": "CEO",
                "source": "Demo"
            }
        ]
    } 
