import math


def solution(n):
    # isqrt는 정수 제곱근을 정확히 구하므로(큰 수도 오차 없음), 그 값을 다시 제곱해 n이 되면 n은 제곱수다
    root = math.isqrt(n)
    if root * root == n:
        return (root + 1) * (root + 1)
    return -1
