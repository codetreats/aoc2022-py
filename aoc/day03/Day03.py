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
            for f in first:
                if f in second:
                    items += f
                    break
        return sum([self.get_value(c) for c in items])

    def run2(self):
        badges = ""
        for index in range(0, len(self.data), 3):
            for f in self.data[index]:
                if f in self.data[index + 1] and f in self.data[index + 2]:
                    badges += f
                    break
        return sum([self.get_value(c) for c in badges])

    def get_value(self, string):
        val = ord(string)
        if val > 96:
            return val - 96
        return val - 38

