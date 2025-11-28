from lib.vec2 import Vec2

class Point:
    def __init__(self, pos: Vec2):
        self.pos: Vec2 = pos

    @staticmethod
    def distance(p1: Point, p2: Point) -> float:
        return p1.pos.dist(p2.pos)
        
    def __str__(self):
        return f"Point({self.pos.x:.2f}, {self.pos.y:.2f})"