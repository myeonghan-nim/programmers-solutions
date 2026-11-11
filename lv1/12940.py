from math import gcd, lcm


def solution(n, m):
    # 표준 라이브러리의 gcd(유클리드 호제법)와 lcm(n * m // gcd)을 그대로 쓴다
    # 시간 복잡도: O(log(min(n, m)))
    return [gcd(n, m), lcm(n, m)]
