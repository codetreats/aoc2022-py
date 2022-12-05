import unittest
from aoc.day05.Day05 import Day05


class testDay05(unittest.TestCase):
    def test_part1_dummy(self):
        class_under_test = Day05().init_with(True)
        self.assertEqual("CMZ", str(class_under_test.run1()))

    def test_part1(self):
        class_under_test = Day05().init_with(False)
        self.assertEqual("VRWBSFZWM", str(class_under_test.run1()))

    def test_part2_dummy(self):
        class_under_test = Day05().init_with(True)
        self.assertEqual("MCD", str(class_under_test.run2()))

    def test_part2(self):
        class_under_test = Day05().init_with(False)
        self.assertEqual("RBTWJWMCF", str(class_under_test.run2()))


if __name__ == '__main__':
    unittest.main()
