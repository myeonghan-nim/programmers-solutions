def solution(n):
    # 오른쪽→아래→왼쪽→위 순서로 나아가며 1부터 n*n까지 차례로 채우고, 다음 칸이 범위 밖이거나 이미 채워져 있으면 시계방향으로 방향을 튼다
    grid = [[0] * n for _ in range(n)]
    row = col = 0
    dr, dc = 0, 1
    for value in range(1, n * n + 1):
        grid[row][col] = value
        if not (0 <= row + dr < n and 0 <= col + dc < n) or grid[row + dr][col + dc]:
            dr, dc = dc, -dr
        row, col = row + dr, col + dc
    return grid
