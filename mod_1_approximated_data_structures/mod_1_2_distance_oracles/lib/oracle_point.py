from lib.vec2 import Vec2
from lib.point import Point

class OraclePoint(Point):
    def __init__(self: OraclePoint, i: int, pos: Vec2):
        super().__init__(pos)
        self.i: int = i
        self.bunch: list[list[OraclePoint]] = []

    def calculate_bunch(self: OraclePoint, Vs: list[list[OraclePoint]]):
        self.bunch: list[list[OraclePoint]] = [[] for _ in range(len(Vs))]
        for i in range(len(Vs) - 1):
            p_next_layer: OraclePoint = min(Vs[i + 1], key=lambda x: Point.distance(self, x))
            for v in Vs[i]:
                if Point.distance(self, v) <= Point.distance(self, p_next_layer):
                    self.bunch[i].append(v)
            self.bunch[i] = sorted(self.bunch[i], key=lambda x: Point.distance(self, x))

        for v in Vs[-1]:
            self.bunch[-1].append(v)
        self.bunch[-1] = sorted(self.bunch[-1], key=lambda x: Point.distance(self, x))
        
    def __str__(self: OraclePoint) -> str:
        return f"OraclePoint(index: {self.i}, position: (x: {self.pos.x:.2f}, y: {self.pos.y:.2f}))"