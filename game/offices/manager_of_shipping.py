from dataclasses import dataclass
from offices.office import Office

@dataclass
class ManagerOfShipping(Office):
    _treasury: int = 0

    def fit_company_ship(self):
        print(self._treasury)
        if self._treasury >= 5:
            self._treasury -= 5


