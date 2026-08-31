def solution(board, skill):
    # 스킬마다 직사각형 안의 칸을 일일이 고치지 않고, 네 모서리에만 변화량을 찍어 두는 2차원 차이 배열을 쓴다. 마지막에 가로/세로로 한 번씩 누적하면 각 칸이 받은 총 변화량이 나오므로, 원래 내구도와 더해 1 이상인 건물을 센다.
    # 시간 복잡도: O(N*M + 스킬 수)
    n, m = len(board), len(board[0])
    damage = [[0] * (m + 1) for _ in range(n + 1)]

    for type_, r1, c1, r2, c2, degree in skill:
        if type_ == 1:  # 공격은 내구도를 깎으므로 음수로
            degree = -degree

        # 직사각형 시작에 +, 벗어나는 경계에 -를 찍어 두면 누적 시 내부만 값이 남는다
        damage[r1][c1] += degree
        damage[r1][c2 + 1] -= degree
        damage[r2 + 1][c1] -= degree
        damage[r2 + 1][c2 + 1] += degree

    for r in range(n + 1):  # 가로 방향 누적
        for c in range(1, m + 1):
            damage[r][c] += damage[r][c - 1]

    for c in range(m + 1):  # 세로 방향 누적
        for r in range(1, n + 1):
            damage[r][c] += damage[r - 1][c]

    answer = 0
    for r in range(n):
        for c in range(m):
            if board[r][c] + damage[r][c] > 0:
                answer += 1

    return answer
