from aoc.Day import Day
from aoc.day05.Input import Input
from aoc.day05.Move import Move
from aoc.util.util import *

class Day05(Day):
    day = "05"
    use_dummy = False

    def convert(self, lines):
        input = Input()
        parts = split_list(lines, "")
        input.add_stacks(parts[0])
        for line in parts[1]:
            input.add_move(Move.from_line(line))
        return input

    def run1(self):
        input = self.data
        for move in input.moves:
            for i in range(move.count):
                input.stacks[move.end - 1].append(input.stacks[move.start - 1].pop())
        return self.result(input.stacks)

    def run2(self):
        input = self.data
        for move in input.moves:
            removed = []
            for i in range(move.count):
                removed.append(input.stacks[move.start - 1].pop())            
            removed.reverse()
            input.stacks[move.end - 1].extend(removed)

        return self.result(input.stacks)

    def result(self, stacks):
        result = ""
        for stack in stacks:
            result += stack[-1]
        return result
