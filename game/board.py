from dataclasses import dataclass

from map import Map

@dataclass
class Board:
    map: Map = Map()