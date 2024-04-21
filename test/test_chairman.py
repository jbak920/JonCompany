import sys
import os
import unittest

sys.path.insert(0, os.path.abspath(os.path.join(os.path.dirname(__file__), '..')))

from game.board import Board
from game.overseer import Overseer
from game.offices.manager_of_shipping import ManagerOfShipping
from game.offices.chairman import Chairman

class TestChairman(unittest.TestCase):
    def setUp(self):
        self.board = Board()
        self.chairman = Chairman(self.board)

    def test_taking_debt(self):
        self.chairman.take_debt(2)
        self.assertEqual(self.board.debt_track, 2)
        self.assertEqual(self.board.company_balance, 15)
        self.chairman.take_debt(3)
        self.assertEqual(self.board.debt_track, 5)
        self.assertEqual(self.board.company_balance, 30)

if __name__ == "__main__":
    unittest.main(verbosity=2)