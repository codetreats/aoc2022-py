import time
import os


class Day:
    day = None
    data = []
    lines = []
    use_dummy = True
    reset = True

    def run(self):
        self.init()
        self.run_part(1)
        if self.reset:
            self.init()
        self.run_part(2)
        
    def run_part(self, nr):
        print(30 * "#")
        print("Starting Day" + self.day + " part " + str(nr))
        print(30 * "#")
        print()
        start = time.time_ns()
        if nr == 1:
            print("Result: " + str(self.run1()))
        else:
            print("Result: " + str(self.run2()))
        end = time.time_ns()
        print()
        duration = round((end - start) / 1000000)
        unit = "millis"
        if duration <= 1:
            duration = end - start
            unit = "nanos"
        print(f"Part {nr} took {duration} {unit}")

    def init(self):
        self.init_with(self.use_dummy)

    def init_with(self, use_dummy):
        self.use_dummy = use_dummy
        res_dir = self.res_dir()
        if use_dummy:
            filename = res_dir + "/day" + self.day + "/dummy.txt"
        else:
            filename = res_dir + "/day" + self.day + "/input.txt"
        with open(filename) as f:
            tmp = f.readlines()
            self.lines = [line.rstrip("\n") for line in tmp]
            self.data = self.convert(self.lines)

        return self

    def run1(self):
        raise NotImplementedError("Please Implement this method")

    def run2(self):
        raise NotImplementedError("Please Implement this method")

    def convert(self, lines):
        raise NotImplementedError("Please Implement this method")

    def read_resource(self, filename):
        res_dir = self.res_dir()
        filename = res_dir + "/day" + self.day + "/" + filename
        with open(filename) as f:
            tmp = f.readlines()
            return [line.rstrip("\n") for line in tmp]

    def res_dir(self):
        return os.path.dirname(os.path.realpath(__file__)) + "/../res"

