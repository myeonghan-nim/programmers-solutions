def solution(elements):
    n = len(elements)
    extended = elements * 2

    prefix = [0] * (2 * n + 1)
    for i, value in enumerate(extended, 1):
        prefix[i] = prefix[i - 1] + value

    sums = set()
    for length in range(1, n + 1):
        for start in range(n):
            sums.add(prefix[start + length] - prefix[start])

    return len(sums)
