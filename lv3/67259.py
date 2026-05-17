from heapq import heappop, heappush


def solution(board):
    n = len(board)
    directions = [(-1, 0), (0, 1), (1, 0), (0, -1)]
    costs = [[[float('inf')] * 4 for _ in range(n)] for _ in range(n)]
    costs[0][0] = [0] * 4
    heap = [(0, 0, 0, -1)]

    while heap:
        cost, row, col, prev_direction = heappop(heap)

        if prev_direction != -1 and cost > costs[row][col][prev_direction]:
            continue

        for direction, (dr, dc) in enumerate(directions):
            nr, nc = row + dr, col + dc

            if not (0 <= nr < n and 0 <= nc < n):
                continue
            if board[nr][nc] == 1:
                continue

            next_cost = cost + 100
            if prev_direction != -1 and prev_direction != direction:
                next_cost += 500

            if next_cost < costs[nr][nc][direction]:
                costs[nr][nc][direction] = next_cost
                heappush(heap, (next_cost, nr, nc, direction))

    return min(costs[n - 1][n - 1])
