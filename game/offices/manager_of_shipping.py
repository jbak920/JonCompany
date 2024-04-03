from game.board import Board

class ManagerOfShipping:

    def __init__(self, board: Board):
        self.board = board

    def fit_company_ship(self, sea_zone):
        if self.board.manager_of_shipping_treasury < 5:
            return
        self.board.manager_of_shipping_treasury -= 5
        if sea_zone == 'w':
            self.board.map.w.num_company_ships += 1 
        if sea_zone == 's':
            self.board.map.s.num_company_ships += 1
        if sea_zone == 'e':
            self.board.map.e.num_company_ships += 1
        if sea_zone == 'c':
            self.board.map.c.num_company_ships += 1

    def fit_extra_ship(self, sea_zone):
        if self.board.manager_of_shipping_treasury < 2:
            return
        self.board.manager_of_shipping_treasury -= 2
        if sea_zone == 'w':
            self.board.map.w.num_extra_ships += 1 
        if sea_zone == 's':
            self.board.map.s.num_extra_ships += 1
        if sea_zone == 'e':
            self.board.map.e.num_extra_ships += 1
        if sea_zone == 'c':
            self.board.map.c.num_extra_ships += 1