from dataclasses import dataclass


@dataclass
class Signal:

    time: str

    market: str

    asset: str

    action: str

    size: str

    who: str

    source: str

    score: int
