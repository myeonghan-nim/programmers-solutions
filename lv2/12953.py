import math


def solution(arr):
    lcm = 1
    for num in arr:
        lcm *= num // math.gcd(lcm, num)
    return lcm
