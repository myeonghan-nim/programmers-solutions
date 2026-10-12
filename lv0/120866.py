def solution(board):
    # 지뢰마다 자기 칸과 둘레 8칸을 위험지역 집합에 넣고, 전체 칸 수에서 위험지역 수를 빼면 안전한 칸 수다
    n = len(board)
    danger = set()
    for r in range(n):
        for c in range(n):
            if board[r][c]:
                for dr in (-1, 0, 1):
                    for dc in (-1, 0, 1):
                        if 0 <= r + dr < n and 0 <= c + dc < n:
                            danger.add((r + dr, c + dc))
    return n * n - len(danger)
