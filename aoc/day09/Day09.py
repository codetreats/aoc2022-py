from aoc.Day import Day
from aoc.common.Point import Point
from aoc.day09.Tail import Tail


class Day09(Day):
    day = "09"
    use_dummy = True
    directions = { "R" : Point(1, 0), "L" : Point(-1, 0), "U" : Point(0, 1), "D" : Point(0, -1)}        

    def convert(self, lines):        
        return lines

    def run1(self):
        return self.run(2)

    def run2(self):
        return self.run(10)

    def run(self, knots):
        tails = [Tail() for i in range(knots)]
        for line in self.data:
            direction = self.directions[line.split()[0]]
            for i in range(int(line.split()[1])):                
                tails[0].set(tails[0].x + direction.x, tails[0].y + direction.y)
                for i in range(knots - 1):
                    tails[i + 1].follow(tails[i])
        return len(tails[-1].visited)
