import unittest
from aoc.day01.Day01 import Day01


class testDay01(unittest.TestCase):
    def test_part1_dummy(self):
        class_under_test = Day01().init_with(True)
        self.assertEqual("24000", str(class_under_test.run1()))

    def test_part1(self):
        class_under_test = Day01().init_with(False)
        self.assertEqual("70613", str(class_under_test.run1()))

    def test_part2_dummy(self):
        class_under_test = Day01().init_with(True)
        self.assertEqual("45000", str(class_under_test.run2()))

    def test_part2(self):
        class_under_test = Day01().init_with(False)
        self.assertEqual("205805", str(class_under_test.run2()))


if __name__ == '__main__':
    unittest.main()
