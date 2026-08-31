def solution(sticker):
    # 원형이라 첫 장과 마지막 장을 동시에 뗄 수 없다. 그래서 "마지막 장 제외(0..n-2)"와 "첫 장 제외(1..n-1)" 두 직선 구간에 대해 인접한 것을 못 떼는 최대합 DP를 각각 돌리고 큰 쪽을 답으로 한다.
    # 시간 복잡도: O(n)
    n = len(sticker)
    if n == 1:
        return sticker[0]

    answer = 0
    for start, end in ((0, n - 1), (1, n)):
        take_prev2 = take_prev1 = 0
        for i in range(start, end):
            # 현재 장을 떼면 두 칸 전 최대 + 현재 값, 안 떼면 한 칸 전 최대
            take_prev2, take_prev1 = take_prev1, max(take_prev1, take_prev2 + sticker[i])
        answer = max(answer, take_prev1)
    return answer
