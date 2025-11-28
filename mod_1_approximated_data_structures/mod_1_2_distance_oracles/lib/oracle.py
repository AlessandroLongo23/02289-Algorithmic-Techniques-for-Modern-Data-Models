import random
from lib.oracle_point import OraclePoint
from lib.vec2 import Vec2
from lib.point import Point

class Oracle:
    def __init__(self: Oracle, num_points: int, k: int, p: float):
        self.points: list[OraclePoint] = [OraclePoint(i, Vec2.random()) for i in range(num_points)]

        self.Vs: list[list[OraclePoint]] = [[] for _ in range(k)]

        self.Vs[0] = self.points
        for i in range(1, len(self.Vs)):
            for point in self.Vs[i - 1]:
                if random.random() < p:
                    self.Vs[i].append(point)

        for point in self.points:
            point.calculate_bunch(self.Vs)

    def distance(self: Oracle, u: OraclePoint, v: OraclePoint) -> float:
        w: OraclePoint = u
        i: int = 0
        while w not in v.bunch[i]:
            i += 1
            u, v = v, u
            w: OraclePoint = u.bunch[i][0]

        distance: float = Point.distance(u, w) + Point.distance(v, w)

        return distance