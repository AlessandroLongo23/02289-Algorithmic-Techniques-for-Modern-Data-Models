from lib.LinearHash import LinearHash, HashFunction

class BloomFilter:
    def __init__(self, m, h):
        self.m = m
        self.h = h
        self.bit_array = [False] * m
        self.nums = []

    def add(self, x):
        for hash_function in self.h:
            self.bit_array[hash_function.evaluate(x)] = True

        self.nums.append(x)

    def __and__(self, other):
        result = BloomFilter(self.m, self.h)
        
        for i in range(self.m):
            result.bit_array[i] = self.bit_array[i] and other.bit_array[i]
        
        return result

    def __or__(self, other):
        result = BloomFilter(self.m, self.h)
        
        for i in range(self.m):
            result.bit_array[i] = self.bit_array[i] or other.bit_array[i]
        
        return result

    def __sub__(self, other):
        result = BloomFilter(self.m, self.h)

        for i in range(self.m):
            result.bit_array[i] = self.bit_array[i] and not other.bit_array[i]
        
        return result

    def add_all(self, X):
        for x in X:
            self.add(x)

    def query(self, x):
        for hash_function in self.h:
            if not self.bit_array[hash_function.evaluate(x)]:
                return False, x in self.nums
        
        return True, x in self.nums

    def print_bit_array(self):
        print("Bit array: ", end="[")
        for i in range(self.m):
            print(1 if self.bit_array[i] else 0, end=" ")
        print("]")

    def calculate_false_positive_rate(self, n):
        expected_specific_bit_zero = (1 - 1 / self.m) ** (len(self.nums) * len(self.h))
        expected_num_zero = self.m * expected_specific_bit_zero

        actual_num_zero = self.m - sum(self.bit_array)
        print(f"Expected num zero: {expected_num_zero}, Actual num zero: {actual_num_zero}")