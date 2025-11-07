class HashFunction:
    def __init__(self, a, b, m):
        self.a = a
        self.b = b
        self.m = m

    def evaluate(self, x: int | str):
        if isinstance(x, str):
            x = int(x, 2)

        return (self.a * x + self.b) % self.m