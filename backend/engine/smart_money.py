from providers.crypto.coingecko import get_crypto_signals
from providers.stocks.finnhub import get_stock_signals


def get_all_signals():

    signals = []

    signals.extend(get_crypto_signals())
    signals.extend(get_stock_signals())

    signals.sort(
        key=lambda signal: signal.score,
        reverse=True
    )

    return signals
