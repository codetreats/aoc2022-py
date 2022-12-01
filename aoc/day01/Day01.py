from aoc.Day import Day
from aoc.day01.Elf import Elf


class Day01(Day):
    day = "01"
    use_dummy = False

    def convert(self, lines):
        elves = []
        elves.append(Elf())
        for line in lines:
            if line == "":                
                elves.append(Elf())
            else: 
                elves[-1].add_calory_line(line)
        return elves

    def run1(self):
        return max([elf.sum() for elf in self.data])

    def run2(self):
        sorted = [elf.sum() for elf in self.data]
        sorted.sort(reverse=True)
        return sorted[0] + sorted[1] + sorted[2]