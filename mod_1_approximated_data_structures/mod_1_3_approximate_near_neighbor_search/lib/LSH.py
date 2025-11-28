from lib.hash_function import HashFunction
from lib.utils import hamming_distance

class LSH:
    def __init__(self, m: int, h: HashFunction, filter_, name: str = "Table"):
        self.name = name
        self.m = m
        self.table = [{} for _ in range(m)]
        self.h = h
        self.filter = filter_

    def insert(self, x: dict):
        if isinstance(x, list):
            for y in x:
                self.insert(y)
            return

        filtered = self.filter.filter(x)
        evaluated = self.h.evaluate(filtered)
        if filtered not in self.table[evaluated]:
            self.table[evaluated][filtered] = []
        self.table[evaluated][filtered].append(x)

    def extractNeighbors(self, x: dict):
        filtered = self.filter.filter(x)
        evaluated = self.h.evaluate(filtered)
        if filtered not in self.table[evaluated]:
            return []
        return self.table[evaluated][filtered]

    def query(self, x: dict):
        neighbors = self.extractNeighbors(x)
        min_distance = float('inf')
        min_neighbor = None
        for neighbor in neighbors:
            if hamming_distance(x['value'], neighbor['value']) < min_distance:
                min_distance = hamming_distance(x['value'], neighbor['value'])
                min_neighbor = neighbor
        return min_neighbor

    def print_table(self) -> None:
        print(f'Table: "{self.name}"')
        for i in range(self.m):
            print(f"{i}: {self.table[i]}")