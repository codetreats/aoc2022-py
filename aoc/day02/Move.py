import re
from dataclasses import dataclass


@dataclass
class Move:
    def shape_score(self):
        raise

    def score(self, opponentMove):
        raise

    @staticmethod
    def from_char(ch):
        if ch == "A" or ch == "X":
            return Rock()
        if ch == "B" or ch == "Y":
            return Paper()
        if ch == "C" or ch == "Z":
            return Scissors()

@dataclass
class Rock(Move):
    def shape_score(self):
        return 1

    def score(self, opponentMove):
        if isinstance(opponentMove, Rock):
            return self.shape_score() + 3
        if isinstance(opponentMove, Paper):
            return self.shape_score() + 0
        if isinstance(opponentMove, Scissors):
            return self.shape_score() + 6

@dataclass
class Paper(Move):
    def shape_score(self):
        return 2

    def score(self, opponentMove):
        if isinstance(opponentMove, Rock):
            return self.shape_score() + 6
        if isinstance(opponentMove, Paper):
            return self.shape_score() + 3
        if isinstance(opponentMove, Scissors):
            return self.shape_score() + 0

@dataclass
class Scissors(Move):
    def shape_score(self):
        return 3

    def score(self, opponentMove):
        if isinstance(opponentMove, Rock):
            return self.shape_score() + 0
        if isinstance(opponentMove, Paper):
            return self.shape_score() + 6
        if isinstance(opponentMove, Scissors):
            return self.shape_score() + 3