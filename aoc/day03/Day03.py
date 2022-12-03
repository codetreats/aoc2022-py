from aoc.Day import Day


class Day03(Day):
    day = "03"
    use_dummy = False

    def convert(self, lines):
        return lines

    def run1(self):
        items = ""
        for line in self.data:
            half = int(len(line) / 2)
            first = line[:half]
            second = line [half:]
            line_items = ""
            for f in first:
                if f in second and f not in line_items:
                    line_items += f
            items += line_items    
        return sum([self.get_value(c) for c in items])

    def run2(self):
        return ""

    def get_value(self, string):
        val = ord(string)
        if val > 96:
            return val - 96
        return val - 38
