from models.signal import Signal
 

def get_crypto_signals():

    signals = []

    signals.append(

        Signal(

            time="LIVE",

            market="Crypto",

            asset="BTC",

            action="BUY",

            size="25 M$",

            who="Wallet -----",

            source="Demo",

            score=94

        )

    )

    return signals
