import sys
from aoc.util.util import get_day
from aoc.day01.Day01 import Day01
from aoc.day02.Day02 import Day02
from aoc.day03.Day03 import Day03
from aoc.day04.Day04 import Day04
from aoc.day05.Day05 import Day05
from aoc.day06.Day06 import Day06
from aoc.day07.Day07 import Day07
from aoc.day08.Day08 import Day08
from aoc.day09.Day09 import Day09
from aoc.day10.Day10 import Day10
from aoc.day11.Day11 import Day11
from aoc.day12.Day12 import Day12
from aoc.day13.Day13 import Day13
from aoc.day14.Day14 import Day14
from aoc.day15.Day15 import Day15
from aoc.day16.Day16 import Day16
from aoc.day17.Day17 import Day17
from aoc.day18.Day18 import Day18
from aoc.day19.Day19 import Day19
from aoc.day20.Day20 import Day20
from aoc.day21.Day21 import Day21
from aoc.day22.Day22 import Day22
from aoc.day23.Day23 import Day23
from aoc.day24.Day24 import Day24
from aoc.day25.Day25 import Day25

if len(sys.argv) > 1:
    overrideDay = sys.argv[1]
else:
    overrideDay = 25

day = get_day(overrideDay)

days = {
    "01": Day01(),
    "02": Day02(),
    "03": Day03(),
    "04": Day04(),
    "05": Day05(),
    "06": Day06(),
    "07": Day07(),
    "08": Day08(),
    "09": Day09(),
    "10": Day10(),
    "11": Day11(),
    "12": Day12(),
    "13": Day13(),
    "14": Day14(),
    "15": Day15(),
    "16": Day16(),
    "17": Day17(),
    "18": Day18(),
    "19": Day19(),
    "20": Day20(),
    "21": Day21(),
    "22": Day22(),
    "23": Day23(),
    "24": Day24(),
    "25": Day25()
}

days[day].run()
