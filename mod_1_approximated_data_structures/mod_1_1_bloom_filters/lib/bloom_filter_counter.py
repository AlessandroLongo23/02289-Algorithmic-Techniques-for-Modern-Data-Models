from lib.linear_hash import HashFunction
from lib.bloom_filter import BloomFilter

class BloomFilterCounter(BloomFilter):
    def __init__(self, m, h):
        super().__init__(m, h)
        self.bit_array: list[int] = [0] * m

    def clear(self) -> None:
        self.bit_array = [0] * self.m
        self.nums = []

    def add(self, x: int) -> None:
        for hash_function in self.h:
            self.bit_array[hash_function.evaluate(x) % self.m] += 1

        self.nums.append(x)

    def delete(self, x: int) -> None:
        for hash_function in self.h:
            self.bit_array[hash_function.evaluate(x) % self.m] -= 1
            if self.bit_array[hash_function.evaluate(x) % self.m] < 0:
                self.bit_array[hash_function.evaluate(x) % self.m] = 0
        
        self.nums.remove(x)

    def __and__(self, other: BloomFilter) -> BloomFilter:
        result: BloomFilter = BloomFilter(self.m, self.h)
        
        for i in range(self.m):
            result.bit_array[i] = min(self.bit_array[i], other.bit_array[i])
        
        return result

    def __or__(self, other: BloomFilter) -> BloomFilter:
        result: BloomFilter = BloomFilter(self.m, self.h)
        
        for i in range(self.m):
            result.bit_array[i] = max(self.bit_array[i], other.bit_array[i])
        
        return result

    def __sub__(self, other: BloomFilter) -> BloomFilter:
        result: BloomFilter = BloomFilter(self.m, self.h)

        for i in range(self.m):
            result.bit_array[i] = self.bit_array[i] - other.bit_array[i]
            if result.bit_array[i] < 0:
                result.bit_array[i] = 0
        
        return result

    def add_all(self, X: list[int]) -> None:
        for x in X:
            self.add(x)

    def query(self, x: int) -> tuple[bool, bool]:
        for hash_function in self.h:
            if self.bit_array[hash_function.evaluate(x) % self.m] == 0:
                return False, x in self.nums
        
        return True, x in self.nums

    def print_bit_array(self) -> None:
        print("Bit array: ", end="[")
        for i in range(self.m):
            print(self.bit_array[i], end=" ")
        print("]")

    def halve(self) -> None:
        if self.m % 2 != 0:
            raise ValueError("Size of Bloom filter must be divisible by 2")
        
        self.bit_array = self.bit_array[:self.m//2] + self.bit_array[self.m//2:]
        self.m = self.m // 2

    def double(self) -> None:
        new_bit_array = [0] * (self.m * 2)
        new_bit_array[:self.m] = self.bit_array
        self.bit_array = new_bit_array
        self.m = self.m * 2