import re
from dataclasses import dataclass
from aoc.common.Point import Point

@dataclass
class Tail(Point):
    visited: {}

    def __init__(self):
        self.x = 0
        self.y = 0
        self.visited = set([Point(0,0)])

    def set(self, x, y):
        self.x = x
        self.y = y

    def follow(self, head):
        if abs(head.x - self.x) > 1 or abs(head.y - self.y) > 1:
            self.x = self.x + self.sign(head.x - self.x)
            self.y = self.y + self.sign(head.y - self.y)
            self.visited.add(Point(self.x, self.y))

    def sign(self, val):
        if val > 0:
            return 1
        if val < 0:
            return -1
        return 0