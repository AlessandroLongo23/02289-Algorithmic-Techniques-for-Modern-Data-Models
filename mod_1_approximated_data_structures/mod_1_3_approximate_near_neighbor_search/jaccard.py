from itertools import chain
from lib.utils import jaccard
from lib.MinHash import MinHash

if __name__ == "__main__":
    sets = [
        ['a', 'e'],
        ['b'],
        ['a', 'c', 'e'],
        ['b', 'd', 'e']
    ]

    for i in range(len(sets)):
        for j in range(i+1, len(sets)):
            print(f"Jaccard similarity between {sets[i]} and {sets[j]}: {jaccard(sets[i], sets[j])}")

    minhash = MinHash(list(set(chain.from_iterable(sets))))
    minhash.insert(sets)
    minhash.print_table()