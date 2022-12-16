import unittest
from aoc.day13.Day13 import Day13


class testDay13(unittest.TestCase):
    def test_part1_dummy(self):
        class_under_test = Day13().init_with(True)
        self.assertEqual("13", str(class_under_test.run1()))

    def test_part1(self):
        class_under_test = Day13().init_with(False)
        self.assertEqual("6272", str(class_under_test.run1()))

    def test_part2_dummy(self):
        class_under_test = Day13().init_with(True)
        self.assertEqual("140", str(class_under_test.run2()))

    def test_part2(self):
        class_under_test = Day13().init_with(False)
        self.assertEqual("22288", str(class_under_test.run2()))


if __name__ == '__main__':
    unittest.main()
