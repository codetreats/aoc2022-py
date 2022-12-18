from aoc.Day import Day
from aoc.day17.Cave import Cave
from aoc.day17.Rock import Rock
import sys
import math

class Day17(Day):
    day = "17"
    use_dummy = False
    rate_check_start = 1

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
        return self.calculate_cave_height(2022)

    def run2(self):
        total_rounds = 1000000000000
        check_rate, diff, round = self.detect_constant_growth_rate()
        # print("After " + str(round) + " rounds, the cave grows every " + str(check_rate) + " rounds/rocks with " + str(diff) + " pixels")
        calculated_rounds = math.floor((total_rounds - round) / check_rate)
        height_of_calculated_rounds = calculated_rounds * diff
        rounds_to_simulate = total_rounds - calculated_rounds * check_rate
        return self.calculate_cave_height(rounds_to_simulate) + height_of_calculated_rounds

    def calculate_cave_height(self, rounds):
        cave = Cave(7, 300)
        move_index = 0
        for round in range(rounds):
            move_index = self.simulate_rock(cave, round, move_index)
            cave.cleanup()
        return cave.total_height()

    def detect_constant_growth_rate(self):
        cave = Cave(7, 300)
        for check_rate in (range(self.rate_check_start, 50000)):
            move_index = 0
            last = 0
            lastdiffs = {}
            lindex = 0
            for round in range(check_rate * 20):
                move_index = self.simulate_rock(cave, round, move_index)
                cave.cleanup()
                if (round + 1) % check_rate == 0:
                    h = cave.total_height()
                    diff = h - last
                    # print("Round " + str(tmp) + " - Height: " + str(h) + " - Diff: " + str(diff))
                    lastdiffs[lindex % 10] = diff
                    lindex = lindex + 1
                    if self.check_diffs_in_a_row(lastdiffs, 10):
                        # print("Found constant diff: " + str(diff) + " @ " + str(check_rate))
                        return (check_rate, diff, round)
                    last = h                   
        raise
    
    def check_diffs_in_a_row(self, lastdiffs, count):
        if len(lastdiffs) < count:
            return False
        diff = lastdiffs[0]
        for d in lastdiffs:
            if lastdiffs[d] != diff:
                return False
        return True

    def simulate_rock(self, cave, round, move_index):
        rock = self.rocks[round % 5]
        pos = (2, cave.max_height() + rock.height + 2)
        while True:
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