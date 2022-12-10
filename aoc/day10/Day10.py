from aoc.Day import Day


class Day10(Day):
    day = "10"
    use_dummy = True

    def convert(self, lines):
        ops = []
        for line in lines:
            ops.append(None)
            if line != "noop":
                ops.append(int(line.split()[1]))
        return ops

    def run1(self):
        x = 1
        strength = 0
        for i in range(220):
            cycle = i + 1
            if cycle == 20 or cycle == 60 or cycle == 100  or cycle == 140  or cycle == 180  or cycle == 220:
                strength = strength + cycle * x
            if self.data[i] != None:
                x = x + self.data[i]
        return strength

    def run2(self):
        sprite = 1
        screen = ""
        for i in range(240):
            crt = i % 40
            if crt == 0:
                screen = screen + "\n"
            if abs(sprite - crt) <= 1:
                screen = screen + "#"
            else:
                screen = screen + "."
            if self.data[i] != None:
                sprite = sprite + self.data[i]
        return screen
