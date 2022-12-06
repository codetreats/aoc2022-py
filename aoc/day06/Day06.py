from aoc.Day import Day


class Day06(Day):
    day = "06"
    use_dummy = False

    def convert(self, lines):
        return lines

    def run1(self):
        return self.index_of_distinct_chars(4)

    def run2(self):
        return self.index_of_distinct_chars(14)

    def index_of_distinct_chars(self, count):
        stream = self.data[0]
        for i in range(count, len(stream) + 1):
            window = stream[i-count:i]
            if len(set(window)) == count:
                return i           
        raise
