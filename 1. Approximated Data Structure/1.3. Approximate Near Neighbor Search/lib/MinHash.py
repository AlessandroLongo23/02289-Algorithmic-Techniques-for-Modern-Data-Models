import random

class MinHash:
    def __init__(self, universe: list[str]):
        self.random_permutation = random.sample(universe, len(universe))
        self.table = [[] for _ in range(len(universe))]

    def hash_(self, set_: list[str]):
        return min(self.random_permutation.index(x) for x in set_)

    def insert(self, set_: list[str] | list[list[str]]):
        if isinstance(set_[0], list):
            for x in set_:
                self.insert(x)
            return

        self.table[self.hash_(set_)].append(set_)

    def print_table(self):
        print(f'Table: "MinHash"')
        print(self.random_permutation)
        for i in range(len(self.table)):
            print(f"{i}: {self.table[i]}")