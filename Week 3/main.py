def hamming_distance(x: str, y: str):
    return sum(1 for i in range(len(x)) if x[i] != y[i])

class HashFunction:
    def __init__(self, a, b, m):
        self.a = a
        self.b = b
        self.m = m

    def evaluate(self, x: int | str):
        if isinstance(x, str):
            x = int(x, 2)

        return (self.a * x + self.b) % self.m

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

class Filter:
    def __init__(self, g: list[int]):
        self.g = g

    def filter(self, x: dict) -> str:
        filtered = ''.join([x['value'][i - 1] for i in self.g])
        return filtered


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


if __name__ == "__main__":
    X = [
        {
            'name': "x",
            'value': '10110011'
        },
        {
            'name': "y",
            'value': '10001101'
        },
        {
            'name': "z",
            'value': '00110010'
        },
        {
            'name': "u",
            'value': '01001010'
        },
        {
            'name': "v",
            'value': '01001000'
        }
    ]

    alsh = ALSH([
        LSH(5, HashFunction(3, 4, 5), Filter([1, 4, 8]), "Table 1"),
        LSH(5, HashFunction(7, 2, 5), Filter([1, 7, 7]), "Table 2")
    ])

    alsh.insert(X)
    alsh.print_tables()

    w = {
        'name': 'w',
        'value': '10111010'
    }

    closest, distance = alsh.apxNearNeighbor(w)
    print(f"Closest: {closest}, Distance: {distance}")