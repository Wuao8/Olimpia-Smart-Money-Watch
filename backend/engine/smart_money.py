from providers.crypto import get_crypto_signals
from providers.stocks import get_stock_signals


def get_all_signals():

    signals = []

    signals.extend(get_crypto_signals())

    signals.extend(get_stock_signals())

    signals.sort(

        key=lambda x: x.score,

        reverse=True

    )

    return signals
