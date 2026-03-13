import math


def solution(n):
    if n < 2:
        return n
    answer = 1 + n
    for i in range(2, int(math.sqrt(n)) + 1):
        if n % i == 0:
            answer += i + (n // i if i != n // i else 0)
    return answer
