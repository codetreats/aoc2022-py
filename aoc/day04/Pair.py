import re
from dataclasses import dataclass
from aoc.day04.Elf import Elf

@dataclass
class Pair:
    first: Elf
    second: Elf

    @staticmethod
    def from_line(line):
        return Pair(Elf.from_part(line.split(",")[0]), Elf.from_part(line.split(",")[1]))

