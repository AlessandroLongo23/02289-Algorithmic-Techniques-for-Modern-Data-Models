from lib.stream import Stream

def misra_gries(stream: Stream, k: int) -> dict[int | str, int]:
    A: dict[int | str, int] = {}
    for el in stream:
        if el in A:
            A[el] += 1
        elif len(A) < k - 1:
            A[el] = 1
        else:
            for key in A:
                A[key] -= 1
            A = {key: value for key, value in A.items() if value > 0}
    return A


def merge_streams(a: dict[int | str, int], b: dict[int | str, int], k: int) -> dict[int | str, int]:
    merged_counters = a.copy()
    for el in b:
        if el in a:
            merged_counters[el] += b[el]
        else:
            merged_counters[el] = b[el]

    if len(merged_counters) > k - 1:
        c = sorted(merged_counters.values(), reverse=True)[k - 1]
        for el in merged_counters:
            merged_counters[el] -= c
        merged_counters = {key: value for key, value in merged_counters.items() if value > 0}
    return merged_counters