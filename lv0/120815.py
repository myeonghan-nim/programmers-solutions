import math


def solution(n):
    # 6조각 x 판 수가 n으로 나누어떨어지는 최소 판 수는 6과 n의 최소공배수를 6으로 나눈 값, 즉 n을 최대공약수로 나눈 값이다
    return n // math.gcd(n, 6)
