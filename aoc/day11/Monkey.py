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

    def throw_next(self, all_divisions):
        if len(self.items) == 0:
            return None
        self.inspections = self.inspections + 1   
        item = self.items.pop(0)
        item = self.operation(item)
        if all_divisions == None:
            item = math.floor(item / 3)
        else:
            item = item % all_divisions
        if item % self.test == 0:
            return (self.if_true, item)
        else:
            return (self.if_false, item)
    
    def receive(self, item):
        self.items.append(item)

    @staticmethod
    def from_lines(lines):
        pattern = re.compile(r"Monkey (\d*):\n.*Starting items: (.*)\n.*Operation: new = old (.) (.*)\n.*Test: divisible by (\d*)\n.*If true: throw to monkey (\d*)\n.*If false: throw to monkey (\d*)")
        match = pattern.match("\n".join(lines))
        
        id = int(match.group(1))
        item_list = match.group(2)
        operator = match.group(3)
        operand = match.group(4)
        test = int(match.group(5))
        if_true = int(match.group(6))
        if_false = int(match.group(7))

        items = [int(x) for x in item_list.split(", ")]
        
        if operator == "*":
            if operand == "old":
                operation = lambda x: x * x
            else:
                op = int(operand)
                operation = lambda x: x * op
        else:
            if operand == "old":
                operation = lambda x: x + x
            else:
                op = int(operand)
                operation = lambda x: x + op
        
        return Monkey(id, items, operation, test, if_true, if_false)