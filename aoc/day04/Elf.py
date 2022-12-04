import re
from dataclasses import dataclass

@dataclass
class Elf:
    start: int
    end: int

    @staticmethod
    def from_part(part):
        return Elf(int(part.split("-")[0]), int(part.split("-")[1]))