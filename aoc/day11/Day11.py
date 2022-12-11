from aoc.Day import Day
from aoc.day11.Monkey import Monkey
from aoc.util.util import *

class Day11(Day):
    day = "11"
    use_dummy = False

    def convert(self, lines):
        parts = split_list(lines, "")
        return [Monkey.from_lines(p) for p in parts]

    def run1(self):
        monkeys = self.data
        for round in range(1,21):
            for monkey in monkeys:
                next = monkey.throw_next()            
                while next != None:
                    monkeys[next[0]].receive(next[1])
                    next = monkey.throw_next()
        inspections = [m.inspections for m in monkeys]
        inspections.sort()        
        return inspections[-1] * inspections[-2]

    def run2(self):
        return ""
