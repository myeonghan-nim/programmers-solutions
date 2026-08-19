def solution(a):
    MOD = 10_000_019
    n = len(a)
    col_sums = [sum(col) for col in zip(*a)]

    C = [[0] * (n + 1) for _ in range(n + 1)]
    for i in range(n + 1):
        C[i][0] = 1
        for j in range(1, i + 1):
            C[i][j] = (C[i - 1][j - 1] + C[i - 1][j]) % MOD

    dp = [0] * (n + 1)
    dp[0] = 1
    for s in col_sums:
        ndp = [0] * (n + 1)
        for odd in range(n + 1):
            if not dp[odd]:
                continue
            for j in range(max(0, s - (n - odd)), min(odd, s) + 1):
                new_odd = odd - j + (s - j)
                ndp[new_odd] = (ndp[new_odd] + dp[odd] * C[odd][j] * C[n - odd][s - j]) % MOD
        dp = ndp
    return dp[0]
