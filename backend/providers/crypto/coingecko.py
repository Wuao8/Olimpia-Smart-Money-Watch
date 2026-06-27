import requests

from config.settings import COINGECKO_API_KEY, COINGECKO_URL
from models.signal import Signal

def calculate_score(coin):

    change = coin["price_change_percentage_24h"] or 0

    return int(min(100, 50 + abs(change) * 3))


def get_crypto_signals():

    headers = {
        "x-cg-demo-api-key": COINGECKO_API_KEY
    }

    response = requests.get(
        f"{COINGECKO_URL}/coins/markets",
        headers=headers,
        params={
            "vs_currency": "usd",
            "order": "market_cap_desc",
            "per_page": 20,
            "page": 1,
            "sparkline": "false"
       },
       timeout=20
    )

    data = response.json()

    signals = []

    for coin in data:
        
        change = coin["price_change_percentage_24h"] or 0

        score = calculate_score(coin)

        signals.append(
            Signal(
                time="LIVE",
                market="Crypto",
                asset=coin["symbol"].upper(),
                action="BUY" if change > 5 else "WATCH",
                size=f"${coin['total_volume']:,.0f}",
                who="CoinGecko",
                source="Markets",
                score=score
            )
        )

    return signals
