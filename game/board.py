from dataclasses import dataclass, field
from typing import List, Dict

from game.map import Map
from game.family import Family

@dataclass 
class Army:
    name: str = field(init=True)
    ready_officers: List[Family] = None
    exhausted_officers: List[Family] = None
    ready_regiments: int = 0
    exhausted_regiments: int = 0

    def __post_init__(self):
        if self.ready_officers is None:
            self.ready_officers = []
        if self.exhausted_officers is None:
            self.exhausted_officers = []

@dataclass
class Board:
    map: Map = None
    company_balance: int = 5
    director_of_trade_treasury: int = 0
    manager_of_shipping_treasury: int = 0
    officers_in_training: List[Family] = field(default_factory=list)
    armies: Dict[str, Army] = None
    bombay_treasury: int = 0
    madras_treasury: int = 0
    bengal_treasury: int = 0
    debt_track: int = 0

    def __post_init__(self):
        if self.map is None:
            self.map = Map()
        if self.armies is None:
            self.armies = {"Bombay": Army("Bombay"), 
                           "Madras": Army("Madras"),
                           "Bengal": Army("Bengal")} 