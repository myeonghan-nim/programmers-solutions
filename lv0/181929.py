import math


def solution(num_list):
    # math.prod로 모든 원소의 곱을 구해 모든 원소의 합의 제곱과 비교한 결과를 1 또는 0으로 돌려준다
    return int(math.prod(num_list) < sum(num_list) ** 2)
