from itertools import combinations


def solution(n, q, ans):
    # n이 최대 30이라 가능한 비밀 코드는 많아야 30개 중 5개를 고르는 142,506가지다. 전부 만들어 보고 모든 시도의 응답과 겹치는 개수가 맞는 것만 센다
    # 시간 복잡도: O(C(n, 5) * m)
    attempts = [set(numbers) for numbers in q]
    return sum(
        all(len(attempt.intersection(code)) == matched for attempt, matched in zip(attempts, ans))
        for code in combinations(range(1, n + 1), 5)
    )
