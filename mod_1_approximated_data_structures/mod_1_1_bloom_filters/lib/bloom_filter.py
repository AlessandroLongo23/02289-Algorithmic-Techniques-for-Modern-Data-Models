from lib.linear_hash import LinearHash, HashFunction

class BloomFilter:
    def __init__(self, m, h):
        self.m: int = m
        self.h: list[HashFunction] = h
        self.bit_array: list[bool] = [False] * m
        self.nums: list[int] = []

    def add(self, x: int) -> None:
        for hash_function in self.h:
            self.bit_array[hash_function.evaluate(x)] = True

        self.nums.append(x)

    def __and__(self, other: BloomFilter) -> BloomFilter:
        result: BloomFilter = BloomFilter(self.m, self.h)
        
        for i in range(self.m):
            result.bit_array[i] = self.bit_array[i] and other.bit_array[i]
        
        return result

    def __or__(self, other: BloomFilter) -> BloomFilter:
        result: BloomFilter = BloomFilter(self.m, self.h)
        
        for i in range(self.m):
            result.bit_array[i] = self.bit_array[i] or other.bit_array[i]
        
        return result

    def __sub__(self, other: BloomFilter) -> BloomFilter:
        result: BloomFilter = BloomFilter(self.m, self.h)

        for i in range(self.m):
            result.bit_array[i] = self.bit_array[i] and not other.bit_array[i]
        
        return result

    def add_all(self, X: list[int]) -> None:
        for x in X:
            self.add(x)

    def query(self, x: int) -> tuple[bool, bool]:
        for hash_function in self.h:
            if not self.bit_array[hash_function.evaluate(x)]:
                return False, x in self.nums
        
        return True, x in self.nums

    def print_bit_array(self) -> None:
        print("Bit array: ", end="[")
        for i in range(self.m):
            print(1 if self.bit_array[i] else 0, end=" ")
        print("]")

    def calculate_false_positive_rate(self, n: int) -> None:
        expected_specific_bit_zero: float = (1 - 1 / self.m) ** (len(self.nums) * len(self.h))
        expected_num_zero: float = self.m * expected_specific_bit_zero

        actual_num_zero: int = self.m - sum(self.bit_array)
        print(f"Expected num zero: {expected_num_zero}, Actual num zero: {actual_num_zero}")