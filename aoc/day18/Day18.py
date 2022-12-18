from aoc.Day import Day
from copy import deepcopy

class Day18(Day):
    day = "18"
    use_dummy = False

    def convert(self, lines):
        return set([(int(line.split(",")[0]),int(line.split(",")[1]),int(line.split(",")[2])) for line in lines])

    def run1(self):
        cubes = self.data
        total = 0
        for cube in cubes:
            for coord in range(3):
                for add in (-1, 1):
                    c = list(cube)
                    c[coord] = c[coord] + add
                    if tuple(c) not in cubes:
                        total = total + 1
        return total

    def run2(self):
        return ""
