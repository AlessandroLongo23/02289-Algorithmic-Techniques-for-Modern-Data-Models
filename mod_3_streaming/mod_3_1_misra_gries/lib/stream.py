import random

class Stream:
    def __init__(self, elements: list[int] | str | None = None, n: int = 10, u: int = 10):
        if isinstance(elements, str):
            elements = list(elements)

        if elements is None:
            elements = random.choices(population=range(1, u + 1), k=n)

        self.elements = elements
        self.n = len(elements)
        self.u = max(elements)
        self.index = 0

    def print_frequencies(self) -> None:
        frequencies = self.get_frequencies()
        print("\nFrequencies:")
        for el, freq in sorted(frequencies.items(), key=lambda x: x[1], reverse=True):
            print(f"Element: {el}, Frequency: {freq}")
    
    def get_frequencies(self) -> dict[int | str, int]:
        return {el: self.elements.count(el) for el in self.elements}

    def print_heavy_hitters(self, k: int) -> None:
        heavy_hitters = self.get_heavy_hitters(k)
        print(f"\nHeavy hitters with k={k}:")
        for el, freq in heavy_hitters.items():
            print(f"Element: {el}, Frequency: {freq}")
    
    def get_heavy_hitters(self, k: int) -> dict[int | str, int]:
        # return all elements that occur more than m/k times: don't return duplicates
        return {el: self.elements.count(el) for el in self.elements if self.elements.count(el) > self.n / k}

    def __add__(self, other: 'Stream') -> 'Stream':
        return Stream(elements=self.elements + other.elements, n=self.n + other.n, u=self.u)

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