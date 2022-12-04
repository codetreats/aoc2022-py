import unittest
from aoc.day04.Day04 import Day04


class testDay04(unittest.TestCase):
    def test_part1_dummy(self):
        class_under_test = Day04().init_with(True)
        self.assertEqual("2", str(class_under_test.run1()))

    def test_part1(self):
        class_under_test = Day04().init_with(False)
        self.assertEqual("450", str(class_under_test.run1()))

    def test_part2_dummy(self):
        class_under_test = Day04().init_with(True)
        self.assertEqual("4", str(class_under_test.run2()))

    def test_part2(self):
        class_under_test = Day04().init_with(False)
        self.assertEqual("837", str(class_under_test.run2()))


if __name__ == '__main__':
    unittest.main()
