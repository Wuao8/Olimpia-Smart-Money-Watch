import requests

from config.settings import COINGECKO_API_KEY, COINGECKO_URL
from models.signal import Signal


def get_crypto_signals():

    headers = {
        "x-cg-demo-api-key": COINGECKO_API_KEY
    }

    response = requests.get(
        f"{COINGECKO_URL}/search/trending",
        headers=headers,
        timeout=20
    )

    data = response.json()

    signals = []

    for coin in data["coins"]:

        item = coin["item"]

        signals.append(
            Signal(
                time="LIVE",
                market="Crypto",
                asset=item["symbol"].upper(),
                action="WATCH",
                size="-",
                who="CoinGecko",
                source="Trending",
                score=80
            )
        )

    return signals
