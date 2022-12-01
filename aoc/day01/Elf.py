import re
from dataclasses import dataclass


@dataclass
class Elf:
    calories: []

    def __init__(self):
        self.calories = []

    def add_calory_line(self, line):
        self.calories.append(int(line))

    def sum(self):
        sum = 0
        for cal in self.calories:
            sum += cal
        return sum