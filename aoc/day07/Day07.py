from aoc.Day import Day
from aoc.day07.Dir import Dir
from aoc.day07.File import File


class Day07(Day):
    day = "07"
    use_dummy = False

    def convert(self, lines):
        root = Dir(None, "/")
        current = root
        for line in lines:
            if line.startswith("$ cd /"):
                current = root
            elif line.startswith("$ cd .."):
                current = current.parent
            elif line.startswith("$ cd"):
                current = current.get_dir(line.split()[2])
            elif line.startswith("dir"):
                current.add_dir(Dir(current, line.split()[1]))
            elif line[0].isdigit():
                current.add_file(File.from_line(line))
        return root

    def run1(self):
        return sum([d.size() for d in self.data.all_dirs() if d.size() <= 100000])

    def run2(self):
        needed = self.data.size() + 30000000 - 70000000
        return min([d.size() for d in self.data.all_dirs() if d.size() >= needed])
