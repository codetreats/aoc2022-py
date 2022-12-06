import unittest
from aoc.day06.Day06 import Day06


class testDay06(unittest.TestCase):
    def test_part1_dummy(self):
        class_under_test = Day06().init_with(True)
        self.assertEqual("7", str(class_under_test.run1()))

    def test_part1(self):
        class_under_test = Day06().init_with(False)
        self.assertEqual("1155", str(class_under_test.run1()))

    def test_part2_dummy(self):
        class_under_test = Day06().init_with(True)
        self.assertEqual("19", str(class_under_test.run2()))

    def test_part2(self):
        class_under_test = Day06().init_with(False)
        self.assertEqual("2789", str(class_under_test.run2()))


if __name__ == '__main__':
    unittest.main()
