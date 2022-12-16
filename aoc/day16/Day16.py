from aoc.Day import Day
from aoc.day16.Room import Room
from aoc.common.Dijkstra import *


class Day16(Day):
    day = "16"
    use_dummy = True

    def convert(self, lines):
        rooms = {}
        indices = {}
        index = 0
        self.shortest_pathes = {}
        for room in [Room.from_line(line) for line in lines]:
            rooms[room.name] = room
            indices[room.name] = index
            index=index+1
        dijkstra = Dijkstra()
        edges = {}
        for r in rooms.values():
            e = []
            for t in r.tunnels:
                e.append(EdgeDistance(indices[t], 1))
            edges[indices[r.name]] = e
        for r in rooms:
            for t in rooms:
               path = dijkstra.shortest_path(len(edges), indices[r], indices[t], edges) 
               self.shortest_pathes[(r, t)] = path.length
        return rooms

    def run1(self):
        valves = []
        for r in self.data.values():
            if r.rate > 0:
                valves.append(r.name)
        return self.most_pressure(30, "AA", valves, 0, 0, 0)

    def run2(self):
        valves = []
        for r in self.data.values():
            if r.rate > 0:
                valves.append(r.name)
        options = []
        for i in range(2 ** len(valves)):
            bin = "{0:b}".format(i).rjust(len(valves))
            me = []
            elephant = []
            for i in range(len(valves)):
                if bin[i] == "0":
                    me.append(valves[i])
                else:
                    elephant.append(valves[i])
            options.append(self.most_pressure(26, "AA", me, 0, 0, 0) + self.most_pressure(26, "AA", elephant, 0, 0, 0))
        return max(options)

    def most_pressure(self, max_time, pos, valves, time, total_p, current_p):
        space = "".rjust(time)
        #print(space + " Minute " + str(time) + ", remaining " + str(valves) + ", total=" + str(total_p) + ": current= " + str(current_p))
        if len(valves) == 0:
            return total_p + current_p * (max_time - time)
        options = []
        for v in valves:
            distance = self.distance(pos, v) + 1 # + 1 for opening the valve
            tp = total_p + current_p * distance
            cp = current_p + self.data[v].rate
            if time + distance <= max_time:
                options.append(self.most_pressure(max_time, v, self.clone_without(valves, v), time + distance, tp, cp))
        if len(options) == 0:
            return total_p + current_p * (max_time - time)
        return max(options)
            


    def distance(self, start, end):
        return self.shortest_pathes[(start, end)]

    def clone_without(self, l, w):
        clone = []
        for e in l:
            if w != e:
                clone.append(e)
        return clone
        
        
    
