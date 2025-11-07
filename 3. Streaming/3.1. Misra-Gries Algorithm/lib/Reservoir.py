import random

class Reservoir:
    def __init__(self, n: int, k: int):
        self.n = n
        self.k = k
        self.count = 0
        self.reservoir = []
    
    def add(self, x: int) -> bool:
        self.count += 1
        if len(self.reservoir) < self.k:
            self.reservoir.append(x)
            return True
        else:
            if random.random() < self.k / self.count:
                self.reservoir[random.randint(0, len(self.reservoir) - 1)] = x
                return True

        return False
    
    def get_reservoir(self) -> list[int]:
        return self.reservoir
    
    def get_count(self) -> int:
        return self.count