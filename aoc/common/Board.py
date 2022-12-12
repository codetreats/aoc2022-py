class Board:
    def __init__(self, width, height, default):
        self.width = width
        self.height = height
        self.default = default
        self.content = {}
        self.rotated = 0
        self.flipped = False

    def fill(self, lines):
        for y in range(len(lines)):
            line = lines[y]
            for x in range(len(line)):
                if line[x] != self.default:
                    self.set(x, y, line[x])
        return self

    def get_or_none(self, x, y):
        if 0 <= x < self.width and 0 <= y < self.height:
            if (x, y) in self.content:
                return self.content[(x, y)]
            return self.default
        return None

    def set(self, x, y, value):
        self.content[(x, y)] = value
    
    def find(self, value):
        for x in range(self.width):
            for y in range(self.height):
                if self.get_or_none(x, y) == value:
                    return (x, y)
        return None

    def index(self, x, y):
        return y * self.width + x

    def neighbors(self, x, y, with_diag=False, with_self=False):
        neighbors = {}
        neighbors[(x - 1, y)] = self.get_or_none(x - 1, y)
        neighbors[(x + 1, y)] = self.get_or_none(x + 1, y)
        neighbors[(x, y - 1)] = self.get_or_none(x, y - 1)
        neighbors[(x, y + 1)] = self.get_or_none(x, y + 1)
        if with_diag:
            neighbors[(x - 1, y - 1)] = self.get_or_none(x - 1, y - 1)
            neighbors[(x + 1, y + 1)] = self.get_or_none(x + 1, y + 1)
            neighbors[(x - 1, y + 1)] = self.get_or_none(x - 1, y + 1)
            neighbors[(x + 1, y - 1)] = self.get_or_none(x + 1, y - 1)
        if with_self:
            neighbors[(x, y)] = self.get_or_none(x, y)
        return {k: v for k, v in neighbors.items() if v is not None}

    def rotate_by(self, times):
        for _ in range(times):
            self.rotate()
        return self

    def rotate(self):
        rotated = {}
        if self.width != self.height:
            raise
        for (x, y), value in self.content.items():
            rotated[(self.width - 1 - y, x)] = value
        self.rotated += 1
        self.content = rotated
        return self

    def flip(self):
        flipped = {}
        if self.rotated != 0:
            raise
        for (x, y), value in self.content.items():
            flipped[(self.width - 1 - x, y)] = value
        self.flipped = not self.flipped
        self.content = flipped
        return self

    def count(self, value):
        count = 0
        for x in range(self.width):
            for y in range(self.height):
                if self.get_or_none(x, y) == value:
                    count += 1
        return count

    def __str__(self):
        board = "\n"
        for y in range(self.height):
            for x in range(self.width):
                board = board + str(self.get_or_none(x, y))
            board = board + "\n"
        board = board + "\n"
        return board

    def __repr__(self):
        return self.__str__()

    def __eq__(self, obj):
        if not isinstance(obj, Board):
            return False
        return self.width == obj.width and self.height == obj.height and self.content == obj.content

    def copy(self):
        board = Board(self.width, self.height, self.default)
        board.content = self.content.copy()
        return board
