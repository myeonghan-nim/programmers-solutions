from collections import deque


def solution(board):
    # 한 번의 이동을 간선 하나로 보는 BFS다. 칸에서 네 방향으로 각각 장애물이나 가장자리 직전까지 미끄러진 칸이 이웃이며, 처음 꺼낸 목표 칸의 이동 횟수가 최솟값이다
    # 시간 복잡도: O(행 수 * 열 수 * (행 수 + 열 수))
    row_count, col_count = len(board), len(board[0])
    start = next((row, col) for row in range(row_count) for col in range(col_count) if board[row][col] == "R")
    moves = {start: 0}
    queue = deque([start])
    while queue:
        row, col = queue.popleft()
        if board[row][col] == "G":
            return moves[(row, col)]
        for d_row, d_col in ((-1, 0), (1, 0), (0, -1), (0, 1)):
            next_row, next_col = row, col
            # 다음 칸이 판 안이고 장애물이 아닌 동안 계속 미끄러진다
            while 0 <= next_row + d_row < row_count and 0 <= next_col + d_col < col_count and board[next_row + d_row][next_col + d_col] != "D":
                next_row, next_col = next_row + d_row, next_col + d_col
            if (next_row, next_col) not in moves:
                moves[(next_row, next_col)] = moves[(row, col)] + 1
                queue.append((next_row, next_col))
    return -1
