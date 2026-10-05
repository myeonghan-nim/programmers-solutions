import math


def solution(a, b):
    # 최대공약수로 나눠 기약분수의 분모를 만든 뒤, 분모에서 2와 5를 전부 나눠 없애고 1만 남으면 유한소수다
    b //= math.gcd(a, b)
    for p in (2, 5):
        while b % p == 0:
            b //= p
    return 1 if b == 1 else 2
