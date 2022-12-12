import unittest
from aoc.day12.Day12 import Day12


class testDay12(unittest.TestCase):
    def test_part1_dummy(self):
        class_under_test = Day12().init_with(True)
        self.assertEqual("31", str(class_under_test.run1()))

    def test_part1(self):
        class_under_test = Day12().init_with(False)
        self.assertEqual("408", str(class_under_test.run1()))

    def test_part2_dummy(self):
        class_under_test = Day12().init_with(True)
        self.assertEqual("29", str(class_under_test.run2()))

    def test_part2(self):
        class_under_test = Day12().init_with(False)
        self.assertEqual("399", str(class_under_test.run2()))


if __name__ == '__main__':
    unittest.main()
