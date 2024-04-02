from dataclasses import dataclass

from board import Board
from offices.manager_of_shipping import ManagerOfShipping

@dataclass
class GameState:
    """Class for tracking the public state of the game"""
    board: Board = Board()
    manager_of_shipping: ManagerOfShipping = ManagerOfShipping()

    def add_company_ship_to_sea_zone(self, zone: str):
        self.manager_of_shipping.fit_company_ship()
        self.board.map.add_company_ship_to_sea_zone(zone)
