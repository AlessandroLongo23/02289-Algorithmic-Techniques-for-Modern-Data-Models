class HashFunction:
    def __init__(self, p: int, q: int, m: int):
        self.p: int = p
        self.q: int = q
        self.m: int = m

class LinearHash(HashFunction):
    def __init__(self, p: int, q: int, m: int):
        super().__init__(p, q, m)

    def evaluate(self, x: int) -> int:
        return (self.p * x + self.q) % self.m