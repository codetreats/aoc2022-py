from aoc.Day import Day
from aoc.day18.Droplet import Droplet

class Day18(Day):
    day = "18"
    use_dummy = False

    def convert(self, lines):
        droplet_list = [Droplet.from_line(line) for line in lines]
        droplets = {}
        for d in droplet_list:
            droplets[(d.x, d.y, d.z)] = d
        return droplets

    def run1(self):
        return self.count_sides(self.data)

    def run2(self):
        droplets = self.data
        max_x = max([d.x for d in droplets.values()]) + 1
        max_y = max([d.y for d in droplets.values()]) + 1
        max_z = max([d.z for d in droplets.values()]) + 1
        for x in range(0, max_x + 1):
            for y in range(0, max_y + 1):
                for z in range(0, max_z + 1):
                    if (x, y, z) not in droplets:
                        droplets[(x,y,z)] = Droplet(x, y, z, False)
                        if x == 0 or y == 0 or z == 0 or x == max_x or y == max_y or z == max_z:
                            droplets[(x,y,z)].is_reachable = True
                        
        last_air = 0
        air = self.count_air(droplets)
        while air != last_air:
            last_air = air
            for droplet in filter(lambda d: d.is_air(), droplets.values()):
                for n in filter(lambda n: n in droplets and not droplets[n].is_lava, droplet.neighbours()):
                    droplets[n].is_reachable = True
            air = self.count_air(droplets)

        return self.count_sides(droplets)

    def count_air(self, droplets):
        return len(list(filter(lambda d: d.is_air(), droplets.values())))

    def count_sides(self, droplets):
        total = 0
        for d in droplets.values():
            if not d.is_lava:
                continue
            total = total + len(list(filter(lambda n: n not in droplets or droplets[n].is_air(), d.neighbours())))
        return total