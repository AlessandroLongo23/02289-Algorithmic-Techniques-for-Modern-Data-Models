from lib.utils import hamming_distance
from lib.lsh import LSH

class ALSH:
    def __init__(self, tables: list[LSH]):
        self.tables = tables

    def insert(self, x: dict | list[dict]):
        if isinstance(x, list):
            for y in x:
                self.insert(y)
            return

        for table in self.tables:
            table.insert(x)

    def apxNearNeighbor(self, x: dict) -> dict:
        min_distance = float('inf')
        min_neighbor = None
        for table in self.tables:
            for y in table.extractNeighbors(x):
                if hamming_distance(x['value'], y['value']) < min_distance:
                    min_distance = hamming_distance(x['value'], y['value'])
                    min_neighbor = y
        return min_neighbor, min_distance

    def print_tables(self) -> None:
        for table in self.tables:
            table.print_table()
            print()