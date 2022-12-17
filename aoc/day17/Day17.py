from aoc.Day import Day
from aoc.day17.Cave import Cave
from aoc.day17.Rock import Rock


class Day17(Day):
    day = "17"
    use_dummy = False

    def convert(self, lines):        
        movements = []
        for s in lines[0]:
            if s == "<":
                movements.append(-1)
            else:
                movements.append(1)
        rocks = []
        rocks.append(Rock(4, 1, [(0,0), (1,0), (2,0), (3,0)]))
        rocks.append(Rock(3, 3, [(1,0), (0,-1), (1,-1), (2,-1), (1,-2)]))
        rocks.append(Rock(3, 3, [(2,0), (2,-1), (0,-2), (1,-2), (2,-2)]))
        rocks.append(Rock(1, 4, [(0,0), (0,-1), (0,-2), (0,-3)]))
        rocks.append(Rock(2, 2, [(0,0), (0,-1), (1,0), (1,-1)]))
        self.rocks = rocks
        return movements

    def run1(self):
        cave = Cave(7, 10000)
        move_index = 0
        for round in range(2022):
            move_index = self.simulate_rock(cave, round, move_index)
        return cave.max_height()

    def run2(self):
        return ""
    
    def simulate_rock(self, cave, round, move_index):
        rock = self.rocks[round % 5]
        pos = (2, cave.max_height() + rock.height + 2)
        while True:
            cave.add_temp(pos, rock)
            stream = self.data[move_index % len(self.data)]
            move_index = move_index + 1
            next_pos = (pos[0] + stream, pos[1])
            if cave.fits(next_pos, rock):
                pos = next_pos                
            next_pos = (pos[0], pos[1] - 1)
            if not cave.fits(next_pos, rock):
                cave.add(pos, rock)
                return move_index
            pos = next_pos