from dataclasses import dataclass

from game.map import Map

@dataclass
class Board:
    map: Map = None
    company_balance: int = 5
    director_of_trade_treasury: int = 0
    manager_of_shipping_treasury: int = 0
    bombay_treasury: int = 0
    madras_treasury: int = 0
    bengal_treasury: int = 0

    def __post_init__(self):
        if self.map is None:
            self.map = Map()