import re
from dataclasses import dataclass

@dataclass
class Rock:
    width: int
    height: int
    pixel: []

    def __init__(self, width, height, pixel):
        self.width = width
        self.height = height
        self.pixel = pixel