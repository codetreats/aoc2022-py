import unittest
from aoc.day10.Day10 import Day10


class testDay10(unittest.TestCase):
    def test_part1_dummy(self):
        class_under_test = Day10().init_with(True)
        self.assertEqual("13140", str(class_under_test.run1()))

    def test_part1(self):
        class_under_test = Day10().init_with(False)
        self.assertEqual("12520", str(class_under_test.run1()))

    def test_part2_dummy(self):
        expected = "\n##..##..##..##..##..##..##..##..##..##..\n###...###...###...###...###...###...###.\n####....####....####....####....####....\n#####.....#####.....#####.....#####.....\n######......######......######......####\n#######.......#######.......#######....."
        class_under_test = Day10().init_with(True)
        self.assertEqual(expected, str(class_under_test.run2()))

    def test_part2(self):
        expected = "\n####.#..#.###..####.###....##..##..#....\n#....#..#.#..#....#.#..#....#.#..#.#....\n###..####.#..#...#..#..#....#.#....#....\n#....#..#.###...#...###.....#.#.##.#....\n#....#..#.#....#....#....#..#.#..#.#....\n####.#..#.#....####.#.....##...###.####."
        class_under_test = Day10().init_with(False)
        self.assertEqual(expected, str(class_under_test.run2()))


if __name__ == '__main__':
    unittest.main()
