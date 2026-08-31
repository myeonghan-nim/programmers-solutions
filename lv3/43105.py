def solution(triangle):
    # 위에서 아래로 내려오며 dp[i][j] = (i행 j번 칸)까지 오는 경로 합의 최댓값을 채운다. 각 칸은 바로 위 왼쪽/오른쪽 두 칸 중 큰 쪽에서 내려온다.
    # 시간 복잡도: O(n^2)
    n = len(triangle)

    dp = [[0] * n for _ in range(n)]
    dp[0][0] = triangle[0][0]
    for i in range(1, n):
        dp[i][0] = dp[i - 1][0] + triangle[i][0]  # 양 끝 칸은 올 수 있는 곳이 하나뿐
        for j in range(1, i):
            dp[i][j] = max(dp[i - 1][j - 1], dp[i - 1][j]) + triangle[i][j]
        dp[i][i] = dp[i - 1][i - 1] + triangle[i][i]

    return max(dp[n - 1])  # 바닥 행에서 가장 큰 값
