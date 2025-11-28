def jaccard(X: list[str], Y: list[str]):
    return len(set(X) & set(Y)) / len(set(X) | set(Y))

def hamming_distance(x: str, y: str):
    return sum(1 for i in range(len(x)) if x[i] != y[i])