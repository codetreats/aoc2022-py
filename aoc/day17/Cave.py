from aoc.common.Board import Board

class Cave(Board):
    removed: int

    def __init__(self, width, height):
        super(Cave, self).__init__(width, height, ".")
        self.removed = 0

    def max_height(self):
        max = -1
        for c in self.content:
            if c[1] > max:
                max = c[1]
        return max + 1

    def total_height(self):
        return self.max_height() + self.removed

    def add(self, start, rock):        
        for r in rock.pixel:
            self.set(start[0] + r[0], start[1] + r[1], "#")

    def fits(self, start, rock):
        for r in rock.pixel:
            val = self.get_or_none(start[0] + r[0], start[1] + r[1]) 
            if val == "#" or val == None:
                return False
        return True

    def cleanup(self):
        content = {}
        if self.max_height() < 200:
            return
        for c in self.content:
            if c[1] > 100:
                content[c[0], c[1] - 100] = self.content[c]
        self.content = content
        self.removed = self.removed + 100

    def __str__(self):
        lines = []
        lines.append("")
        for y in range(self.max_height() + 3):
            line = ""
            for x in range(self.width):
                line = line + str(self.get_or_none(x, y))
            lines.append(line)
        lines.append("")
        lines.reverse()
        return "\n".join(lines)