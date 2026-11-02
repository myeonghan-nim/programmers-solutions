from itertools import combinations


def solution(number):
    # 학생이 최대 13명이므로 세 명을 뽑는 모든 조합(최대 286개)의 합이 0인지 직접 세어도 충분하다
    # 시간 복잡도: O(n^3)
    return sum(a + b + c == 0 for a, b, c in combinations(number, 3))
