import re
from dataclasses import dataclass

@dataclass
class Move:
    count: int
    start: int
    end: int

    @staticmethod
    def from_line(line):
        pattern = re.compile(r"move (\d*) from (\d*) to (\d*)")
        match = pattern.match(line)
        return Move(int(match.group(1)), int(match.group(2)), int(match.group(3)))