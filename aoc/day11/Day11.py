import sys
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
        return self.simulate(20, None)

    def run2(self):
        # the idea is, that if a division y by x is 0, than (y - x) / x = 0, too
        # so if you remove the product of all divisors of the worry level, the divison will still work
        # the monkey which multiplies old * old has no items and can be ignored
        all_divisions = 1
        for m in self.data:
            all_divisions = all_divisions * m.test
        return self.simulate(10000, all_divisions)

    def simulate(self, rounds, all_divisions):
        monkeys = self.data
        reduces = 1
        for m in monkeys:
            reduces = reduces * m.test
        for round in range(1,rounds + 1):
            sys.stdout.flush()
            for monkey in monkeys:
                next = monkey.throw_next(all_divisions)            
                while next != None:
                    monkeys[next[0]].receive(next[1])
                    next = monkey.throw_next(all_divisions)
        inspections = [m.inspections for m in monkeys]
        inspections.sort()     
        return inspections[-1] * inspections[-2]
