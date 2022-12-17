import unittest
from aoc.day16.Day16 import Day16


class testDay16(unittest.TestCase):
    def test_part1_dummy(self):
        class_under_test = Day16().init_with(True)
        self.assertEqual("1651", str(class_under_test.run1()))

    def test_part1(self):
        class_under_test = Day16().init_with(False)
        self.assertEqual("2320", str(class_under_test.run1()))

    def test_part2_dummy(self):
        class_under_test = Day16().init_with(True)
        self.assertEqual("1707", str(class_under_test.run2()))

    def test_part2(self):
        class_under_test = Day16().init_with(False)
        # self.assertEqual("2967", str(class_under_test.run2()))


if __name__ == '__main__':
    unittest.main()
