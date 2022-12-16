import re
import math
from dataclasses import dataclass

@dataclass
class Room:
    name: str
    rate: int
    tunnels: []
    is_open: bool
    opened_at_last_visit: {}

    def __init__(self, name, rate, tunnels, is_open, opened_at_last_visit):
        self.name = name
        self.rate = rate
        self.tunnels = tunnels
        self.is_open = is_open
        self.opened_at_last_visit = opened_at_last_visit

    def open(self):
        self.is_open = True

    def clone(self):
        if self.opened_at_last_visit == None:
            opened_at_last_visit = None
        else:
            opened_at_last_visit = set()
            for o in self.opened_at_last_visit:
                opened_at_last_visit.add(o)
        return Room(self.name, self.rate, self.tunnels, self.is_open, opened_at_last_visit)

    def were_same_opened_at_last_visit(self, rooms):
        if self.opened_at_last_visit == None:
            return False
        for r in rooms.values():
            if r.is_open and r.name not in self.opened_at_last_visit:
                return False
        return True

    def visit(self, rooms):
        if self.opened_at_last_visit == None:
            self.opened_at_last_visit = set()
        for r in rooms.values():
            if r.is_open:
                self.opened_at_last_visit.add(r.name)

    @staticmethod
    def from_line(line):
        pattern = re.compile(r"Valve (.*) has flow rate=(\d*); tunnel.? lead.? to valve.? (.*)")
        match = pattern.match(line)
        name = match.group(1)
        rate = int(match.group(2))
        tunnels = match.group(3).split(", ")
        return Room(name, rate, tunnels, False, None)