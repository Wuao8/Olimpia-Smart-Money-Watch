from providers.crypto.coingecko import get_crypto_signals


def get_all_signals():
    signals = []

    signals.extend(get_crypto_signals())

    signals.sort(key=lambda s: s.score, reverse=True)

    return signals
