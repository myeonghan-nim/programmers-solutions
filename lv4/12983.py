def solution(strs, t):
    n = len(t)
    words = set(strs)

    INF = float('inf')
    dp = [INF] * (n + 1)
    dp[0] = 0

    for i in range(n):
        if dp[i] == INF:
            continue

        for word in words:
            if t.startswith(word, i):
                next_index = i + len(word)
                dp[next_index] = min(dp[next_index], dp[i] + 1)

    return dp[n] if dp[n] != INF else -1
