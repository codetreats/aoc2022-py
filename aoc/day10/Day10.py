from aoc.Day import Day


class Day10(Day):
    day = "10"
    use_dummy = False

    def convert(self, lines):
        ops = []
        for line in lines:
            ops.append(0)
            if line != "noop":
                ops.append(int(line.split()[1]))
        return ops

    def run1(self):
        x = 1
        strength = 0
        for i in range(220):
            cycle = i + 1
            if cycle % 40 == 20:
                strength = strength + cycle * x
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
            sprite = sprite + self.data[i]
        return screen
