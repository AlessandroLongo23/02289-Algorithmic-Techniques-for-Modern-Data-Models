import random
from itertools import chain


def jaccard(X: list[str], Y: list[str]):
    return len(set(X) & set(Y)) / len(set(X) | set(Y))

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

if __name__ == "__main__":
    sets = [
        ['a', 'e'],
        ['b'],
        ['a', 'c', 'e'],
        ['b', 'd', 'e']
    ]

    for i in range(len(sets)):
        for j in range(i+1, len(sets)):
            print(f"Jaccard similarity between {sets[i]} and {sets[j]}: {jaccard(sets[i], sets[j])}")

    minhash = MinHash(list(set(chain.from_iterable(sets))))
    minhash.insert(sets)
    minhash.print_table()

