import hashlib

class HashFunction:
    def __init__(self, p, q, m):
        self.p = p
        self.q = q
        self.m = m


class LinearHash(HashFunction):
    def __init__(self, p, q, m):
        super().__init__(p, q, m)

    def evaluate(self, x):
        return (self.p * x + self.q) % self.m


class HashLibFunction(HashFunction):
    def __init__(self, salt, m):
        super().__init__(0, 0, m)
        self.salt = salt
        self.m = m
    
    def evaluate(self, x):
        value = str(x) + str(self.salt)
        hash_value = int(hashlib.md5(value.encode()).hexdigest(), 16)
        return hash_value % self.m