import math


def solution(numer1, denom1, numer2, denom2):
    # 통분해서 더한 뒤(분자는 서로의 분모를 곱해 더하고, 분모는 분모끼리 곱함) 최대공약수로 나눠 기약분수로 만든다
    numer = numer1 * denom2 + numer2 * denom1
    denom = denom1 * denom2
    g = math.gcd(numer, denom)
    return [numer // g, denom // g]
