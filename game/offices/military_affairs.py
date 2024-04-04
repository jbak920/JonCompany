from game.board import Board
from game.family import Family

class MilitaryAffairs:

    def __init__(self, board: Board):
        self.board = board

    def assign_officer(self, family, army):
        if family in self.board.officers_in_training:
            self.board.officers_in_training.remove(family)
            self.board.armies[army].ready_officers.append(family)

    def transfer_officer(self, family, source, destination):
        if family in self.board.armies[source].ready_officers:
            self.board.armies[source].ready_officers.remove(family)
            self.board.armies[destination].ready_officers.append(family)

    def transfer_regiment(self, source, destination):
        if self.board.armies[source].ready_regiments > 0:
            self.board.armies[source].ready_regiments -= 1
            self.board.armies[destination].ready_regiments += 1
