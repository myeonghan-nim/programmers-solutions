def solution(n):
    if n < 3:
        return n
    else:
        a, b = 1, 2
        for _ in range(3, n + 1):
            a, b = b, (a + b) % 1234567
        return b
