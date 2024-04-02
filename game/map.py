from dataclasses import dataclass
from typing import List

@dataclass
class SeaZone:
    _name: str
    _num_company_ships: int = 0

    def add_company_ship(self):
        self._num_company_ships += 1

@dataclass
class Map:
    _w: SeaZone = SeaZone("w")
    _e: SeaZone = SeaZone("e")
    _s: SeaZone = SeaZone("s")
    _c: SeaZone = SeaZone("c")

    def add_company_ship_to_sea_zone(self, sea_zone: str):
        if sea_zone == "w":
            self._w.add_company_ship()
        if sea_zone == "e":
            self._e.add_company_ship()
        if sea_zone == "s":
            self._s.add_company_ship()
        if sea_zone == "c":
            self._c.add_company_ship()