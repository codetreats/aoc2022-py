from __future__ import annotations
import re
from dataclasses import dataclass
from aoc.day07.File import File

@dataclass
class Dir:
    parent: Dir
    name: str
    files: []
    subdirs: []

    def __init__(self, parent: Dir, name):
        self.parent = parent
        self.name = name
        self.files = []
        self.subdirs = []

    def add_dir(self, dir: Dir):
        self.subdirs.append(dir)
        
    def add_file(self, file: File):
        self.files.append(file)

    def size(self):
        size = 0
        for f in self.files:
            size = size + f.size
        for d in self.subdirs:
            size = size + d.size()
        return size

    def all_dirs(self):
        dirs = self.subdirs.copy()
        for d in self.subdirs:
            dirs = dirs + d.all_dirs()
        return dirs        

    def get_dir(self, name: str):
        for dir in self.subdirs:
            if dir.name == name:
                return dir
        raise        