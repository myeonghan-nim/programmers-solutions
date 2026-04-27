from collections import deque


def solution(stones, k):
    candidates = deque()
    answer = float('inf')

    for i, stone in enumerate(stones):
        while candidates and candidates[0] <= i - k:
            candidates.popleft()

        while candidates and stones[candidates[-1]] <= stone:
            candidates.pop()

        candidates.append(i)

        if i >= k - 1:
            answer = min(answer, stones[candidates[0]])

    return answer
