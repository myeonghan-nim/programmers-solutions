def solution(n):
    if n < 3:
        return 1

    cnt = 0
    start = end = total = 1
    while start <= n:
        if total == n:
            cnt += 1
            total -= start
            start += 1
        elif total < n:
            end += 1
            if end > n:
                break
            total += end
        else:
            total -= start
            start += 1

    return cnt
