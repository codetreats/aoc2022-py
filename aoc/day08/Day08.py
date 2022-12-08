from aoc.Day import Day
from aoc.common.Board import Board

class Day08(Day):
    day = "08"
    use_dummy = False

    def convert(self, lines):
        board = Board(len(lines[0]), len(lines), 0)
        for y in range(len(lines)):
            line = lines[y]
            for x in range(len(line)):
                board.set(x, y, int(line[x]))
        return board

    def run1(self):
        trees = self.data
        visible = Board(trees.width, trees.height, 0)
        for y in range(trees.height):
            max = -1
            max_rev = -1
            for x in range(trees.width):
                x_rev = trees.width - x - 1
                if (trees.get_or_none(x, y) > max):
                    visible.set(x, y, 1)
                    max = trees.get_or_none(x, y)
                if (trees.get_or_none(x_rev, y) > max_rev):
                    visible.set(x_rev, y, 1)
                    max_rev = trees.get_or_none(x_rev, y)
        for x in range(trees.width):
            max = -1
            max_rev = -1
            for y in range(trees.height):
                y_rev = trees.height - y - 1
                if (trees.get_or_none(x, y) > max):
                    visible.set(x, y, 1)
                    max = trees.get_or_none(x, y)
                if (trees.get_or_none(x, y_rev) > max_rev):
                    visible.set(x, y_rev, 1)
                    max_rev = trees.get_or_none(x, y_rev)
        return sum(visible.content.values())

    def run2(self):
        trees = self.data
        scenic = Board(trees.width, trees.height, 0)
        for x in range(trees.width):
            for y in range(trees.height):
                scenic.set(x, y, self.scenic_score(x, y))
        return max(scenic.content.values())

    def scenic_score(self, sx, sy):
        trees = self.data
        height = trees.get_or_none(sx, sy)
        left = right = up = down = 0
        for x in range(sx + 1, trees.width):
            right = right + 1
            if trees.get_or_none(x, sy) >= height:
                break
        for x in reversed(range(0, sx)):
            left = left + 1
            if trees.get_or_none(x, sy) >= height:
                break
        for y in range(sy + 1, trees.height):
            down = down + 1
            if trees.get_or_none(sx, y) >= height:
                break
        for y in reversed(range(0, sy)):
            up = up + 1
            if trees.get_or_none(sx, y) >= height:
                break
        return right * left * up * down
  
