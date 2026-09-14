import math


def solution(num_list):
    # 길이가 11 이상이면 모든 원소의 합, 10 이하면 모든 원소의 곱(math.prod)을 구한다
    return sum(num_list) if len(num_list) >= 11 else math.prod(num_list)
