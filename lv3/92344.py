def solution(board, skill):
    n, m = len(board), len(board[0])
    damage = [[0] * (m + 1) for _ in range(n + 1)]

    for type_, r1, c1, r2, c2, degree in skill:
        if type_ == 1:
            degree = -degree

        damage[r1][c1] += degree
        damage[r1][c2 + 1] -= degree
        damage[r2 + 1][c1] -= degree
        damage[r2 + 1][c2 + 1] += degree

    for r in range(n + 1):
        for c in range(1, m + 1):
            damage[r][c] += damage[r][c - 1]

    for c in range(m + 1):
        for r in range(1, n + 1):
            damage[r][c] += damage[r - 1][c]

    answer = 0
    for r in range(n):
        for c in range(m):
            if board[r][c] + damage[r][c] > 0:
                answer += 1

    return answer
