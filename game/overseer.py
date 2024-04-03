from game.board import Board

class Overseer:

    def __init__(self, board: Board):
        self.board = board

    def upkeep_and_refresh(self):
        # TODO: spent armies become usable again
        # TODO: writers return to their homes
        # TODO: return governor state to normal?
        # TODO: return ships to sea?
        self.board.map.w.num_extra_ships = 0
        self.board.map.e.num_extra_ships = 0
        self.board.map.s.num_extra_ships = 0
        self.board.map.c.num_extra_ships = 0