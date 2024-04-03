import sys
import os
import unittest

sys.path.insert(0, os.path.abspath(os.path.join(os.path.dirname(__file__), '..')))

from game.board import Board
from game.overseer import Overseer
from game.offices.manager_of_shipping import ManagerOfShipping
from game.offices.chairman import Chairman

class TestManagerOfShipping(unittest.TestCase):
    def setUp(self):
        self.board = Board()
        self.manager_of_shipping = ManagerOfShipping(self.board)
        self.chairman = Chairman(self.board)
        self.overseer = Overseer(self.board)

    def test_nominal_fitting_company_ships(self):
        self.board.manager_of_shipping_treasury = 10
        self.manager_of_shipping.fit_company_ship('w')
        self.assertEqual(self.board.map.w.num_company_ships, 1)

    def test_funding_and_allocating(self):
        self.chairman.allocate_funds_to_manager_of_shipping(5)
        self.assertEqual(self.board.manager_of_shipping_treasury, 5)
        self.assertEqual(self.board.company_balance, 0)
        self.manager_of_shipping.fit_company_ship('w')
        self.assertEqual(self.board.map.w.num_company_ships, 1)
        self.assertEqual(self.board.manager_of_shipping_treasury, 0)
        self.assertEqual(self.board.company_balance, 0)

    def test_two_types_of_ship(self):
        self.board.company_balance = 7
        self.chairman.allocate_funds_to_manager_of_shipping(7)
        self.manager_of_shipping.fit_company_ship('e')
        self.manager_of_shipping.fit_extra_ship('s')        
        self.assertEqual(self.board.map.e.num_company_ships, 1)
        self.assertEqual(self.board.map.s.num_extra_ships, 1)
        self.assertEqual(self.board.manager_of_shipping_treasury, 0)
        self.assertEqual(self.board.company_balance, 0)
        self.overseer.upkeep_and_refresh()
        self.assertEqual(self.board.map.e.num_company_ships, 1)
        self.assertEqual(self.board.map.s.num_extra_ships, 0)
        self.assertEqual(self.board.manager_of_shipping_treasury, 0)
        self.assertEqual(self.board.company_balance, 0)

if __name__ == "__main__":
    unittest.main(verbosity=2)