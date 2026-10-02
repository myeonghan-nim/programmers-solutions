import math


def solution(n):
    # 정수 제곱근(isqrt)을 구해 다시 제곱했을 때 n이 그대로 나오면 제곱수다
    return 1 if math.isqrt(n) ** 2 == n else 2
