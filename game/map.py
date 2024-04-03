from dataclasses import dataclass, field

@dataclass
class SeaZone:
    name: str
    num_company_ships: int = 0
    num_extra_ships: int = 0

@dataclass
class Map:
    def default_sea_zone():
        return SeaZone("default")

    w: SeaZone = field(default_factory=default_sea_zone)
    e: SeaZone = field(default_factory=default_sea_zone)
    s: SeaZone = field(default_factory=default_sea_zone)
    c: SeaZone = field(default_factory=default_sea_zone)