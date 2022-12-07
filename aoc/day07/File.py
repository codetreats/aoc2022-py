import re
from dataclasses import dataclass
from aoc.day05.Move import Move

@dataclass
class File:
    name: str
    size: int

    @staticmethod
    def from_line(line):
        return File(line.split()[1], int(line.split()[0]))