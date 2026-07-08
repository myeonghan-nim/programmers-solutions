def solution(n):
    dp = [0] * (n + 1)
    dp[0] = 1

    for i in range(1, n + 1):
        for left in range(i):
            right = i - 1 - left
            dp[i] += dp[left] * dp[right]

    return dp[n]
