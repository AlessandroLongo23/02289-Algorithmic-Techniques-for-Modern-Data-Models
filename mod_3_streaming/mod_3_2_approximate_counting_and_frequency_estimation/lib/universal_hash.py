import hashlib
import random

class UniversalHashTable():
    def __init__(self, m: int, salt: int | None = None):
        if salt is None:
            self.salt = random.randint(0, 1000000)
        else:
            self.salt = salt

        self.m: int = m
        self.table = [[] for _ in range(m)]
    
    def evaluate(self, x: int) -> int:
        value: str = str(x) + str(self.salt)
        hash_value: int = int(hashlib.md5(value.encode()).hexdigest(), 16)
        return hash_value % self.m

    def insert(self, x: int) -> None:
        self.table[self.evaluate(x)].append(x)

    def insert_all(self, nums: list[int]) -> None:
        for num in nums:
            self.insert(num)

    def is_injective(self) -> bool:
        for i in range(self.m):
            if len(self.table[i]) > 1:
                return False
        return True

    def __str__(self) -> str:
        table_str = "\n".join([f"{i}: {self.table[i]}" for i in range(self.m)])
        table_str = table_str.replace("], ", "],\n")
        table_str = "{\n" + table_str + "\n}"
        return f"{{m={self.m}, salt={self.salt}, table={table_str}}}"
