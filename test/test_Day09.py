import unittest
from aoc.day09.Day09 import Day09


class testDay09(unittest.TestCase):
    def test_part1_dummy(self):
        class_under_test = Day09().init_with(True)
        self.assertEqual("88", str(class_under_test.run1()))

    def test_part1(self):
        class_under_test = Day09().init_with(False)
        self.assertEqual("6314", str(class_under_test.run1()))

    def test_part2_dummy(self):
        class_under_test = Day09().init_with(True)
        self.assertEqual("36", str(class_under_test.run2()))

    def test_part2(self):
        class_under_test = Day09().init_with(False)
        self.assertEqual("2504", str(class_under_test.run2()))


if __name__ == '__main__':
    unittest.main()
