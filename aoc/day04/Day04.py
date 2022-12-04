from aoc.Day import Day
from aoc.day04.Pair import Pair
from aoc.day04.Elf import Elf


class Day04(Day):
    day = "04"
    use_dummy = False

    def convert(self, lines):
        return [Pair.from_line(line) for line in lines]

    def run1(self):
        count=0
        for pair in self.data:
            if self.is_in(pair.first, pair.second) or self.is_in(pair.second, pair.first):
                count=count + 1
        return count

    def run2(self):
        count=0
        for pair in self.data:
            if self.overlaps(pair.first, pair.second) or self.overlaps(pair.second, pair.first):
                count=count + 1
        return count

    def is_in(self, first, second):
        return first.start <= second.start and first.end >= second.end

    def overlaps(self, first, second):
        return first.end >= second.start and second.end >= first.start
