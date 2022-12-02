import unittest
from aoc.day02.Day02 import Day02


class testDay02(unittest.TestCase):
    def test_part1_dummy(self):
        class_under_test = Day02().init_with(True)
        self.assertEqual("15", str(class_under_test.run1()))

    def test_part1(self):
        class_under_test = Day02().init_with(False)
        self.assertEqual("12458", str(class_under_test.run1()))

    def test_part2_dummy(self):
        class_under_test = Day02().init_with(True)
        self.assertEqual("12", str(class_under_test.run2()))

    def test_part2(self):
        class_under_test = Day02().init_with(False)
        self.assertEqual("12683", str(class_under_test.run2()))


if __name__ == '__main__':
    unittest.main()
