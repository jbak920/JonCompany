from game.board import Board

class Chairman:

    def __init__(self, board: Board):
        self.board = board

    def allocate_funds_to_manager_of_shipping(self, funds):
        if self.board.company_balance < funds:
            return
        self.board.manager_of_shipping_treasury += funds
        self.board.company_balance -= funds

    def take_debt(self, debt):
        if debt < 0:
            return
        if debt > (8 - self.board.debt_track):
            return
        self.board.debt_track += debt
        self.board.company_balance += (5 * debt)