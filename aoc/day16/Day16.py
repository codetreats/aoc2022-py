from aoc.Day import Day
from aoc.day16.Room import Room
from aoc.common.Dijkstra import *


class Day16(Day):
    day = "16"
    use_dummy = True

    def convert(self, lines):
        # all rooms as HashMap Roomname -> Room
        rooms = {}
        # maps e.g. AA to 0, BB to 1
        indices = {}
        index = 0
        # Parse input
        for room in [Room.from_line(line) for line in lines]:
            rooms[room.name] = room
            indices[room.name] = index
            index=index + 1

        # calculate all shortest pathes from each room to each other room
        dijkstra = Dijkstra()
        edges = {}
        for r in rooms.values():
            e = []
            for t in r.tunnels:
                e.append(EdgeDistance(indices[t], 1))
            edges[indices[r.name]] = e
        self.shortest_pathes = {}
        for r in rooms:
            for t in rooms:
               path = dijkstra.shortest_path(len(edges), indices[r], indices[t], edges) 
               self.shortest_pathes[(r, t)] = path.length

        # Collect all rooms which have working valves (rate > 0)
        self.valves = []
        for r in rooms.values():
            if r.rate > 0:
                self.valves.append(r.name)
        return rooms

    def run1(self):
        return self.most_pressure(30, "AA", self.valves, 0, 0, 0)

    def run2(self):
        valves = self.valves
        options = []
        # iterate all possibilites how to split up the valves between me and the elephant
        for i in range(2 ** len(valves)):
            # convert to bin, 0 means me, 1 means elephant
            bin = "{0:b}".format(i).rjust(len(valves))
            me = []
            elephant = []
            for i in range(len(valves)):
                if bin[i] == "0":
                    me.append(valves[i])
                else:
                    elephant.append(valves[i])
            # run me and the elephant independently
            options.append(self.most_pressure(26, "AA", me, 0, 0, 0) + self.most_pressure(26, "AA", elephant, 0, 0, 0))
        return max(options)

    def most_pressure(self, max_time, pos, valves, time, total_p, current_p):
        options = []
        for v in valves:
            distance = self.shortest_pathes[(pos, v)] + 1 # + 1 for opening the valve
            tp = total_p + current_p * distance
            cp = current_p + self.data[v].rate
            if time + distance <= max_time:
                options.append(self.most_pressure(max_time, v, self.clone_without(valves, v), time + distance, tp, cp))
        if len(options) == 0:
            return total_p + current_p * (max_time - time)
        return max(options)

    def clone_without(self, valves, valve):
        clone = []
        for v in valves:
            if valve != v:
                clone.append(v)
        return clone
        
        
    
