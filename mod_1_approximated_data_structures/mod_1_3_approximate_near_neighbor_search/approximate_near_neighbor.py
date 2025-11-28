from lib.ALSH import ALSH
from lib.LSH import LSH
from lib.HashFunction import HashFunction
from lib.Filter import Filter

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