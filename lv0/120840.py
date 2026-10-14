import math


def solution(balls, share):
    # 순서 없이 고르는 경우의 수는 조합이므로 math.comb로 balls개 중 share개를 뽑는 조합 수를 구한다
    return math.comb(balls, share)
