def solution(a):
    # b는 열마다 1의 개수만 a와 같으면 되므로, 열을 왼쪽부터 하나씩 채우면서 "지금까지 1을 홀수 개 가진 행의 수(odd)"만 상태로 기억하는 DP를 돌린다. 한 열에 1을 s개 놓을 때 홀수 행에 j개, 짝수 행에 s-j개 놓는 경우를 조합으로 센다.
    # 시간 복잡도: O(m * n^2)  (n = 행 수, m = 열 수)
    MOD = 10_000_019
    n = len(a)
    col_sums = [sum(col) for col in zip(*a)]  # 각 열의 1 개수(b에도 그대로 필요)

    # binom[i][j] = i개에서 j개를 고르는 경우의 수(이항계수) 표
    binom = [[0] * (n + 1) for _ in range(n + 1)]
    for i in range(n + 1):
        binom[i][0] = 1
        for j in range(1, i + 1):
            binom[i][j] = (binom[i - 1][j - 1] + binom[i - 1][j]) % MOD

    dp = [0] * (n + 1)
    dp[0] = 1
    for s in col_sums:
        ndp = [0] * (n + 1)
        for odd in range(n + 1):
            if not dp[odd]:
                continue
            for j in range(max(0, s - (n - odd)), min(odd, s) + 1):
                new_odd = odd - j + (s - j)  # 홀수 행에 놓으면 짝수로, 짝수 행에 놓으면 홀수로 바뀜
                ndp[new_odd] = (ndp[new_odd] + dp[odd] * binom[odd][j] * binom[n - odd][s - j]) % MOD
        dp = ndp
    return dp[0]  # 마지막에 홀수 행이 0개 = 모든 행의 1 개수가 짝수
