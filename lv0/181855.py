from collections import Counter


def solution(str_arr):
    # 문자열들을 길이별로 세어 가장 개수가 많은 그룹의 크기를 구한다
    return max(Counter(len(s) for s in str_arr).values())
