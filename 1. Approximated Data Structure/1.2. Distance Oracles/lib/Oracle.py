import random
from lib.Point import Point
from lib.Vec2 import Vec2

class Oracle:
    def __init__(self, num_points, k, p):
        self.points = [Point(i, Vec2.random()) for i in range(num_points)]

        self.Vs = [[] for _ in range(k)]

        self.Vs[0] = self.points
        for i in range(1, len(self.Vs)):
            for point in self.Vs[i - 1]:
                if random.random() < p:
                    self.Vs[i].append(point)

        for point in self.points:
            point.calculate_bunch(self.Vs)

    def dist(self: Oracle, u: Point, v: Point) -> float:
        w = u
        i = 0
        while w not in v.bunch[i]:
            i += 1
            u, v = v, u
            w = u.bunch[i][0]

        distance = u.distance(w) + v.distance(w)

        return distance / u.distance(v)