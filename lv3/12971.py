def solution(sticker):
    n = len(sticker)
    if n == 1:
        return sticker[0]

    answer = 0
    for start, end in ((0, n - 1), (1, n)):
        take_prev2 = take_prev1 = 0
        for i in range(start, end):
            take_prev2, take_prev1 = take_prev1, max(take_prev1, take_prev2 + sticker[i])
        answer = max(answer, take_prev1)
    return answer
