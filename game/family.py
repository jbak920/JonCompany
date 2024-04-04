from dataclasses import dataclass, field


ALLOWED_FAMILIES = ["Paxton", "Larkin", "Hastings", "Walsh", "Benyon", "Sykes"]

@dataclass
class Family:
    name: str = field(init=True)

    def __post_init__(self):
        if self.name not in ALLOWED_FAMILIES:
            raise ValueError(f"{self.name} is not one of the 6 allowed families")