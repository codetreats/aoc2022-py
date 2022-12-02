import re
from dataclasses import dataclass
from aoc.day02.Move import Move

@dataclass
class Round:
    first: Move
    second: Move
   
    @staticmethod
    def from_line(line):
        parts = line.split()
        return Round(Move.from_char(parts[0]), Move.from_char(parts[1]))