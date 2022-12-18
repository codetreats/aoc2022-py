import unittest
from aoc.day17.Day17 import Day17


class testDay17(unittest.TestCase):
    def test_part1_dummy(self):
        class_under_test = Day17().init_with(True)
        self.assertEqual("3068", str(class_under_test.run1()))

    def test_part1(self):
        class_under_test = Day17().init_with(False)
        self.assertEqual("3130", str(class_under_test.run1()))

    def test_part2_dummy(self):
        class_under_test = Day17().init_with(True)
        self.assertEqual("1514285714288", str(class_under_test.run2()))

    def test_part2(self):
        class_under_test = Day17().init_with(False)
        class_under_test.rate_check_start = 1725 # Speedup test, test should succeed also without this, but will take much longer
        self.assertEqual("1556521739139", str(class_under_test.run2()))


if __name__ == '__main__':
    unittest.main()
