from aoc.Day import Day
from aoc.day12.HeatMap import HeatMap
from aoc.common.Dijkstra import *

class Day12(Day):
    day = "12"
    use_dummy = False

    def convert(self, lines):
        map = HeatMap.from_lines(lines)
        self.end = map.find("E")
        self.all_edges = {}
        for x in range(map.width):
            for y in range(map.height):
                edges = []
                val = map.value(x, y)
                for n in map.neighbors(x, y):
                    if val + 1 >= map.value(n[0], n[1]):
                        edges.append(EdgeDistance(map.index(n[0], n[1]), 1))
                self.all_edges[map.index(x, y)] = edges
        self.dijkstra = Dijkstra()
        return map

    def run1(self):
        start = self.data.find("S")
        return self.path_length(start)

    def run2(self):
        map = self.data
        distances = []
        for x in range(map.width):
            for y in range(map.height):
                if map.value(x, y) == 1:
                    distances.append(self.path_length((x, y)))
        return min(distances)

    def path_length(self, start):
        map = self.data
        edges = self.all_edges
        end = self.end
        result = self.dijkstra.shortest_path(len(edges), map.index(start[0], start[1]), map.index(end[0], end[1]), edges)
        return result.length
