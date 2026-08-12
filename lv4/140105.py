def solution(n, count):
    MOD = 1_000_000_007
    dp = [0] * (count + 1)
    dp[1] = 1
    for i in range(2, n + 1):
        for k in range(min(i, count), 0, -1):
            dp[k] = (dp[k - 1] + 2 * (i - 1) * dp[k]) % MOD
    return dp[count]
