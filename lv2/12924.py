def solution(n):
    # 연속한 자연수 구간 [start, end]의 합(total)을 유지하며 구간을 조금씩 옮긴다. 합이 n보다 작으면 끝(end)을 늘리고, 크면 앞(start)을 줄이고, 같으면 하나 센다.
    # 시간 복잡도: O(n)
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
