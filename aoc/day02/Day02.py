from aoc.Day import Day
from aoc.day02.Move import *
from aoc.day02.Round import Round


class Day02(Day):
    day = "02"
    use_dummy = False

    def convert(self, lines):
        return lines

    def run1(self):
        rounds = [Round.from_line(line) for line in self.data]
        return sum([round.second.score(round.first) for round in rounds])

    def run2(self):
        return ""
