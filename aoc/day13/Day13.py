from aoc.Day import Day
from aoc.util.util import *
import json
import functools

class Day13(Day):
    day = "13"
    use_dummy = True

    def convert(self, lines):
        result = []
        for p in split_list(lines, ""):
            result.append((json.loads(p[0]), json.loads(p[1])))
        return result

    def run1(self):
        indices = []
        for i in range(len(self.data)):
            if self.order(self.data[i][0], self.data[i][1]) <= 0:
                indices.append(i + 1)
        return sum(indices)

    def run2(self):
        key = 1
        all = [[[2]], [[6]]]
        for tuple in self.data:
            all.append(tuple[0])
            all.append(tuple[1])
        sorted_pkg = sorted(all, key=functools.cmp_to_key(self.order))
        for i in range(len(sorted_pkg)):
            if sorted_pkg[i] == [[2]] or sorted_pkg[i] == [[6]]:
                key = key * (i + 1)
        return key

    def order(self, left, right):        
        if type(left) is int and type(right) is int:
            return left - right
        if type(left) is int:
            left = [ left ]
        if type(right) is int:
            right = [ right ]
        for i in range(max([len(left), len(right)])):
            if len(left) < i + 1:
                return -1
            if len(right) < i + 1:
                return 1
            order = self.order(left[i], right[i])
            if order != 0:
                return order
        return 0
