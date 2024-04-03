from game.offices.office import Office
from game.board import Board

class Chairman(Office):

    def __init__(self, board: Board):
        self.board = board

    def allocate_funds_to_manager_of_shipping(self, funds):
        if self.board.company_balance < funds:
            return
        self.board.manager_of_shipping_treasury += funds
        self.board.company_balance -= funds
