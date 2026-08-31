from collections import deque


def solution(stones, k):
    # 모두 건너려면 연속한 k개의 디딤돌마다 최소 하나는 밟아야 하므로, 각 길이 k 구간에서는 "가장 큰 수"만큼만 사람이 지나갈 수 있다. 답은 모든 구간 최댓값 중 가장 작은 값이며, 구간 최댓값은 앞뒤로 넣고 뺄 수 있는 덱에 큰 값 후보의 위치만 남겨 O(1)씩 갱신한다.
    # 시간 복잡도: O(n)
    candidates = deque()
    answer = float('inf')

    for i, stone in enumerate(stones):
        while candidates and candidates[0] <= i - k:  # 구간 밖으로 벗어난 후보 제거
            candidates.popleft()

        while candidates and stones[candidates[-1]] <= stone:  # 현재 값 이하인 후보는 필요 없음
            candidates.pop()

        candidates.append(i)

        if i >= k - 1:  # 구간이 처음으로 꽉 찬 뒤부터, 맨 앞 후보가 구간 최댓값
            answer = min(answer, stones[candidates[0]])

    return answer
