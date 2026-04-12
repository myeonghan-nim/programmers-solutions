def solution(n, stations, w):
    answer = 0

    now = 1
    coverage = 2 * w + 1
    for station in stations:
        left = station - w
        if now < left:
            gap = left - now
            q, r = divmod(gap, coverage)
            answer += q + (1 if r else 0)
        now = station + w + 1

    if now <= n:
        gap = n - now + 1
        q, r = divmod(gap, coverage)
        answer += q + (1 if r else 0)

    return answer
