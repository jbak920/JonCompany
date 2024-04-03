from dataclasses import dataclass

from game.board import Board
from game.offices.manager_of_shipping import ManagerOfShipping
from game.offices.chairman import Chairman

@dataclass
class GameState:
    """Class for tracking the public state of the game"""
    board: Board = Board()
    manager_of_shipping: ManagerOfShipping = ManagerOfShipping()
    chairman: Chairman = Chairman(manager_of_shipping)

    def add_company_ship_to_sea_zone(self, zone: str):
        if self.manager_of_shipping._treasury < 5:
            return
        self.manager_of_shipping.fit_company_ship()
        self.board.map.add_company_ship_to_sea_zone(zone)

    def add_extra_ship_to_sea_zone(self, zone: str):
        if self.manager_of_shipping._treasury < 2:
            return
        self.manager_of_shipping.fit_extra_ship()
        self.board.map.add_extra_ship_to_sea_zone(zone)

    def upkeep_and_refresh(self):
        # TODO: spent armies become usable again
        # TODO: writers return to their homes
        # TODO: return governor state to normal?
        # TODO: return ships to sea?
        self.board.map._w._num_extra_ships = 0
        self.board.map._e._num_extra_ships = 0
        self.board.map._s._num_extra_ships = 0
        self.board.map._c._num_extra_ships = 0