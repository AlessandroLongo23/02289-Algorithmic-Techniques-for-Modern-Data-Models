import numpy as np
import random

class Vec2: 
    def __init__(self, x, y):
        self.x = x
        self.y = y

    @staticmethod
    def random() -> Vec2:
        return Vec2(random.random(), random.random())

    def dist(self: Vec2, other: Vec2) -> float:
        return np.sqrt((self.x - other.x) ** 2 + (self.y - other.y) ** 2)