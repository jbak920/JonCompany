import sys
import os
import unittest

sys.path.insert(0, os.path.abspath(os.path.join(os.path.dirname(__file__), '..')))

from game.board import Board
from game.family import Family
from game.offices.military_affairs import MilitaryAffairs
from game.overseer import Overseer

class TestManagerOfShipping(unittest.TestCase):
    def setUp(self):
        self.board = Board()
        self.military_affairs = MilitaryAffairs(self.board)
        self.overseer = Overseer(self.board)

    def test_assign_officer(self):
        self.board.officers_in_training.append(Family("Paxton"))
        self.military_affairs.assign_officer(Family("Paxton"), "Bengal")
        self.assertEqual(self.board.officers_in_training, [])
        self.assertEqual(self.board.armies["Bengal"].ready_officers, [Family("Paxton")])

    def test_assign_many_officers(self):
        self.board.officers_in_training.append(Family("Paxton"))
        self.board.officers_in_training.append(Family("Larkin"))
        self.board.officers_in_training.append(Family("Hastings"))
        self.military_affairs.assign_officer(Family("Paxton"), "Bengal")
        self.military_affairs.assign_officer(Family("Larkin"), "Madras")
        self.military_affairs.assign_officer(Family("Hastings"), "Bombay")
        self.assertEqual(self.board.officers_in_training, [])
        self.assertEqual(self.board.armies["Bengal"].ready_officers, [Family("Paxton")])
        self.assertEqual(self.board.armies["Madras"].ready_officers, [Family("Larkin")])
        self.assertEqual(self.board.armies["Bombay"].ready_officers, [Family("Hastings")])

    def test_transfer_officers(self):
        self.board.armies["Bengal"].ready_officers.append(Family("Paxton"))
        self.board.armies["Bengal"].ready_officers.append(Family("Larkin"))
        self.board.armies["Bengal"].ready_officers.append(Family("Hastings"))
        self.military_affairs.transfer_officer(Family("Paxton"), "Bengal", "Madras")
        self.military_affairs.transfer_officer(Family("Larkin"), "Bengal", "Bombay")
        self.assertEqual(self.board.armies["Bengal"].ready_officers, [Family("Hastings")])
        self.assertEqual(self.board.armies["Madras"].ready_officers, [Family("Paxton")])
        self.assertEqual(self.board.armies["Bombay"].ready_officers, [Family("Larkin")])

    def test_transfer_regiments(self):
        self.board.armies["Bengal"].ready_regiments = 6
        self.military_affairs.transfer_regiment("Bengal", "Madras")
        self.military_affairs.transfer_regiment("Bengal", "Madras")
        self.military_affairs.transfer_regiment("Bengal", "Bombay")
        self.assertEqual(self.board.armies["Bengal"].ready_regiments, 3)
        self.assertEqual(self.board.armies["Madras"].ready_regiments, 2)
        self.assertEqual(self.board.armies["Bombay"].ready_regiments, 1)

    def test_refresh_armies(self):
        self.board.armies["Bengal"].ready_regiments = 1
        self.board.armies["Bengal"].exhausted_regiments = 2
        self.board.armies["Bengal"].ready_officers = [Family("Paxton")]
        self.board.armies["Bengal"].exhausted_officers = [Family("Larkin")]
        self.overseer.upkeep_and_refresh()
        self.assertEqual(self.board.armies["Bengal"].ready_regiments, 3)
        self.assertEqual(self.board.armies["Bengal"].exhausted_regiments, 0)
        self.assertEqual(self.board.armies["Bengal"].ready_officers, [Family("Paxton"), Family("Larkin")])
        self.assertEqual(self.board.armies["Bengal"].exhausted_officers, [])

    def test_promote_commander(self):


if __name__ == "__main__":
    unittest.main(verbosity=2)