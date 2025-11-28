class Filter:
    def __init__(self, g: list[int]):
        self.g = g

    def filter(self, x: dict) -> str:
        filtered = ''.join([x['value'][i - 1] for i in self.g])
        return filtered