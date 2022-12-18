import re
from dataclasses import dataclass

@dataclass
class Droplet:
    x: int
    y: int
    z: int
    is_lava: bool
    is_reachable: bool

    def __init__(self, x, y, z, is_lava):
        self.x = x
        self.y = y
        self.z = z
        self.is_lava = is_lava
        self.is_reachable = False

    def is_air(self):
        return self.is_reachable and not self.is_lava

    def neighbours(self):
        x = self.x
        y = self.y
        z = self.z
        neighbours = []
        neighbours.append((x + 1, y, z))
        neighbours.append((x - 1, y, z))
        neighbours.append((x, y + 1, z))
        neighbours.append((x, y - 1, z))
        neighbours.append((x, y, z + 1))
        neighbours.append((x, y, z - 1))
        return neighbours

    @staticmethod
    def from_line(line):
        parts = line.split(",")
        return Droplet(int(parts[0]), int(parts[1]), int(parts[2]), True)