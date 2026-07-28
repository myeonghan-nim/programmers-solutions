def solution(board):
    n = len(board)

    blocks = {}
    for r in range(n):
        for c in range(n):
            if board[r][c]:
                blocks.setdefault(board[r][c], []).append((r, c))

    def column_top(c):
        return next((r for r in range(n) if board[r][c]), n)

    top = [column_top(c) for c in range(n)]

    def removable(bid, cells):
        rows = [r for r, _ in cells]
        cols = [c for _, c in cells]
        for r in range(min(rows), max(rows) + 1):
            for c in range(min(cols), max(cols) + 1):
                if board[r][c] == bid:
                    continue
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
