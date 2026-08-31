import math


def solution(arr):
    # 두 수의 최소공배수 = 두 수의 곱 ÷ 최대공약수(gcd). 이를 배열의 앞에서부터 하나씩 누적하면 전체 최소공배수가 된다.
    lcm = 1
    for num in arr:
        lcm *= num // math.gcd(lcm, num)
    return lcm
