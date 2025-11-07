class Point:
    def __init__(self, i, pos):
        self.i = i
        self.pos = pos
        self.bunch = None

    def distance(self: Point, other: Point) -> float:
        return self.pos.dist(other.pos)

    def calculate_bunch(self: Point, Vs: list[list[Point]]):
        self.bunch = [[] for _ in range(len(Vs))]
        for i in range(len(Vs) - 1):
            p_next_layer = min(Vs[i + 1], key=lambda x: self.distance(x))
            for v in Vs[i]:
                if self.distance(v) <= self.distance(p_next_layer):
                    self.bunch[i].append(v)
            self.bunch[i] = sorted(self.bunch[i], key=lambda x: self.distance(x))

        for v in Vs[-1]:
            self.bunch[-1].append(v)
        self.bunch[-1] = sorted(self.bunch[-1], key=lambda x: self.distance(x))
        
    def __str__(self):
        return f"{self.i}"