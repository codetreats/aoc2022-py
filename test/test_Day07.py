import unittest
from aoc.day07.Day07 import Day07


class testDay07(unittest.TestCase):
    def test_part1_dummy(self):
        class_under_test = Day07().init_with(True)
        self.assertEqual("95437", str(class_under_test.run1()))

    def test_part1(self):
        class_under_test = Day07().init_with(False)
        self.assertEqual("1086293", str(class_under_test.run1()))

    def test_part2_dummy(self):
        class_under_test = Day07().init_with(True)
        self.assertEqual("24933642", str(class_under_test.run2()))

    def test_part2(self):
        class_under_test = Day07().init_with(False)
        self.assertEqual("366028", str(class_under_test.run2()))


if __name__ == '__main__':
    unittest.main()
