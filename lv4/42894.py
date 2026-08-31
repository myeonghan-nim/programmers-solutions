def solution(board):
    # 블록을 지울 수 있는 조건: 블록을 감싸는 가장 작은 직사각형에서 블록이 아닌 칸이 전부 비어 있고, 그 빈칸 위로 검은 블록이 막힘없이 떨어질 수 있어야 한다.
    # 하나를 지우면 위가 뚫려 새로 지울 수 있게 되므로, 더 못 지울 때까지 반복한다.
    # 시간 복잡도: O(B^2 + B*N) (B는 블록 수, N은 보드 한 변 길이)
    n = len(board)

    blocks = {}
    for r in range(n):
        for c in range(n):
            if board[r][c]:
                blocks.setdefault(board[r][c], []).append((r, c))

    def column_top(c):
        return next((r for r in range(n) if board[r][c]), n)

    top = [column_top(c) for c in range(n)]  # 각 열에서 가장 위에 있는 블록의 행 번호

    def removable(bid, cells):
        rows = [r for r, _ in cells]
        cols = [c for _, c in cells]
        for r in range(min(rows), max(rows) + 1):
            for c in range(min(cols), max(cols) + 1):
                if board[r][c] == bid:
                    continue
                # 다른 블록이 차지했거나(top[c] < r) 위가 막혀 검은 블록이 못 닿으면 불가
                if board[r][c] or top[c] < r:
                    return False
        return True

    answer, changed = 0, True
    while changed:
        changed = False
        for bid in list(blocks):
            if removable(bid, blocks[bid]):
                for r, c in blocks[bid]:
                    board[r][c] = 0
                for _, c in blocks[bid]:
                    top[c] = column_top(c)
                del blocks[bid]
                answer += 1
                changed = True
    return answer
