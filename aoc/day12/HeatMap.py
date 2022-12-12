from aoc.common.Board import Board
from itertools import product


class HeatMap(Board):
    def __init__(self, width, height):
        super(HeatMap, self).__init__(width, height, "")

    def value(self, x, y):
        v = self.get_or_none(x, y)
        if v == "S":
            return 1
        if v == "E":
            return 26
        return ord(v) - 96


    @staticmethod
    def from_lines(lines):
        heatMap = HeatMap(len(lines[0]), len(lines))
        for y in range(len(lines)):
            line = lines[y]
            for x in range(len(line)):
                heatMap.set(x, y, line[x])
        return heatMap
