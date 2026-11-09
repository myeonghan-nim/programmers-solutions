from collections import Counter


def solution(participant, completion):
    # 동명이인이 있을 수 있어 집합 차집합은 쓸 수 없다. Counter끼리 빼면 횟수 차이가 남는 이름만 남고, 완주하지 못한 선수는 한 명이므로 그 이름이 유일한 키다
    # 시간 복잡도: O(n)
    return next(iter(Counter(participant) - Counter(completion)))
