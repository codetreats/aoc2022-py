from aoc.Day import Day


class Day10(Day):
    day = "10"
    use_dummy = True

    def convert(self, lines):
        ops = [ None ]
        for line in lines:
            ops.append(None)
            if line != "noop":
                ops.append(int(line.split()[1]))
        return ops

    def run1(self):
        x = 1
        strength = 0
        for i in range(1, 221):
            if i == 20 or i == 60 or i == 100  or i == 140  or i == 180  or i == 220:
                print(str(i) + ": " + str(x))
                strength = strength + i * x
            if self.data[i] != None:
                x = x + self.data[i]
            

        return strength

    def run2(self):
        return ""
