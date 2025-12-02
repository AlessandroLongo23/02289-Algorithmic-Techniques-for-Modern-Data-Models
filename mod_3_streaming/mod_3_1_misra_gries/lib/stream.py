import random

class Stream:
    def __init__(self, elements: list[int] | None = None, n: int = 10, u: int = 10):
        if elements is None:
            elements = random.choices(population=range(1, u + 1), k=n)

        self.elements = elements
        self.n = len(elements)
        self.u = max(elements)
        self.index = 0

    def __str__(self) -> str:
        return f"Stream(elements={self.elements}, n={self.n}, u={self.u})"

    def __next__(self) -> int | None:
        if self.index >= len(self.elements):
            raise StopIteration
        element = self.elements[self.index]
        self.index += 1
        return element
    
    def __len__(self) -> int:
        return len(self.elements)
    
    def __getitem__(self, index: int) -> int | None:
        return self.elements[index]