from aoc.Day import Day


class Day02(Day):
    day = "02"
    use_dummy = False

    scoring = [["A", "A", 3], ["A", "B", 0], ["A", "C", 6], ["B", "A", 6], ["B", "B", 3], ["B", "C", 0], ["C", "A", 0], ["C", "B", 6], ["C", "C", 3]]
    shape_score = {"A": 1, "B": 2, "C": 3}

    def convert(self, lines):
        return [line.split() for line in lines]

    def run1(self):
        sum = 0
        for line in self.data:
            me = line[1].replace("X", "A").replace("Y", "B").replace("Z", "C")
            opponent = line[0]
            sum += self.shape_score[me] + self.score(me, opponent)
        return sum

    def run2(self):
        sum = 0
        for line in self.data:
            result = int(line[1].replace("X", "0").replace("Y", "3").replace("Z", "6"))
            opponent = line[0]
            sum += self.shape_score[self.move(result, opponent)] + result
        return sum

    def score(self, me, opponent):
        for score in self.scoring:
            if me == score[0] and opponent == score[1]:
                return score[2]
        raise

    def move(self, result, opponent):
        for score in self.scoring:
            if result == score[2] and opponent == score[1]:
                return score[0]
        raise