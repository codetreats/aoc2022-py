import unittest
from aoc.day10.Day10 import Day10


class testDay10(unittest.TestCase):
    def test_part1_dummy(self):
        class_under_test = Day10().init_with(True)
        self.assertEqual("", str(class_under_test.run1()))

    def test_part1(self):
        class_under_test = Day10().init_with(False)
        self.assertEqual("", str(class_under_test.run1()))

    def test_part2_dummy(self):
        class_under_test = Day10().init_with(True)
        self.assertEqual("", str(class_under_test.run2()))

    def test_part2(self):
        class_under_test = Day10().init_with(False)
        self.assertEqual("", str(class_under_test.run2()))


if __name__ == '__main__':
    unittest.main()
