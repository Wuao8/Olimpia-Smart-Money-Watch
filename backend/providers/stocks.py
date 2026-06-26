from models.signal import Signal


def get_stock_signals():

    signals = []

    signals.append(

        Signal(

            time="LIVE",

            market="Stocks",

            asset="AAPL",

            action="BUY",

            size="800 K$",

            who="CEO",

            source="Demo",

            score=82

        )

    )

    return signals
