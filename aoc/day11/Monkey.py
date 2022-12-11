import re
import math
from dataclasses import dataclass

@dataclass
class Monkey:
    id: int
    items: []
    operation: any
    test: int
    if_true: int
    if_false: int
    inspections: int

    def __init__(self, id, items, operation, test, if_true, if_false):
        self.id = id
        self.items = items
        self.operation = operation
        self.test = test
        self.if_true = if_true
        self.if_false = if_false
        self.inspections = 0

    def throw_next(self):
        if len(self.items) == 0:
            return None
        self.inspections = self.inspections + 1   
        item = self.items.pop(0)
        item = self.operation(item)
        item = math.floor(item / 3)
        if item % self.test == 0:
            return (self.if_true, item)
        else:
            return (self.if_false, item)
    
    def receive(self, item):
        self.items.append(item)

    @staticmethod
    def from_lines(lines):
        pattern = re.compile(r"Monkey (\d*):")
        line = lines.pop(0)
        match = pattern.match(line)
        id = int(match.group(1))
        pattern = re.compile(r".*Starting items: (.*)")
        match = pattern.match(lines.pop(0))
        items = [int(x) for x in match.group(1).split(", ")]
        pattern = re.compile(r".*Operation: new = old (.) (.*)")
        match = pattern.match(lines.pop(0))
        if match.group(1) == "*":
            if match.group(2) == "old":
                operation = lambda x: x * x
            else:
                op = int(match.group(2))
                operation = lambda x: x * op
        else:
            if match.group(2) == "old":
                operation = lambda x: x + x
            else:
                op = int(match.group(2))
                operation = lambda x: x + op
        pattern = re.compile(r".*Test: divisible by (\d*)")
        match = pattern.match(lines.pop(0))
        test = int(match.group(1))
        pattern = re.compile(r".*If true: throw to monkey (\d*)")
        match = pattern.match(lines.pop(0))
        if_true = int(match.group(1))
        pattern = re.compile(r".*If false: throw to monkey (\d*)")
        match = pattern.match(lines.pop(0))
        if_false = int(match.group(1))
        return Monkey(id, items, operation, test, if_true, if_false)