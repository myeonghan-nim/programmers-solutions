def solution(mats, park):
    # 각 칸을 오른쪽 아래 모서리로 하는 가장 큰 빈 정사각형의 한 변을 dp로 구하고(위, 왼쪽, 왼쪽 위 칸 값의 최솟값 + 1), 그 최댓값 이하인 가장 큰 돗자리를 고른다
    # 시간 복잡도: O(h * w + len(mats))
    height, width = len(park), len(park[0])
    dp = [[0] * (width + 1) for _ in range(height + 1)]  # 맨 위 행과 맨 왼쪽 열을 0으로 두어 경계 검사를 없앤다
    best = 0
    for i in range(height):
        for j in range(width):
            if park[i][j] == "-1":
                dp[i + 1][j + 1] = min(dp[i][j + 1], dp[i + 1][j], dp[i][j]) + 1
                best = max(best, dp[i + 1][j + 1])
    return max((mat for mat in mats if mat <= best), default=-1)
