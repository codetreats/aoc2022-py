import re
from dataclasses import dataclass
from aoc.day05.Move import Move

@dataclass
class Input:
    stacks: []
    moves: []

    def __init__(self):
        self.stacks = []
        self.moves = []

    def add_move(self, move: Move):
        self.moves.append(move)

    def add_stacks(self, lines):
        lines.reverse()
        stack_count = int((len(lines.pop(0)) + 1) / 4)
        for i in range(stack_count):
            self.stacks.append([])
        for line in lines:
            for index in range(stack_count):
                crate = line[index * 4 + 1]
                if crate != " ":
                    self.stacks[index].append(crate)