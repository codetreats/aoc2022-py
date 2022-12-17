import re
import math
from dataclasses import dataclass

@dataclass
class Room:
    name: str
    rate: int
    tunnels: []
    def __init__(self, name, rate, tunnels):
        self.name = name
        self.rate = rate
        self.tunnels = tunnels

    @staticmethod
    def from_line(line):
        pattern = re.compile(r"Valve (.*) has flow rate=(\d*); tunnel.? lead.? to valve.? (.*)")
        match = pattern.match(line)
        name = match.group(1)
        rate = int(match.group(2))
        tunnels = match.group(3).split(", ")
        return Room(name, rate, tunnels)