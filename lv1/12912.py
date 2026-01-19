def solution(a, b):
    start, end = min(a, b), max(a, b)
    return (start + end) * (end - start + 1) // 2
