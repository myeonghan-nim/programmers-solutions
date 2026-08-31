from heapq import heappop, heappush


def solution(board):
    # 같은 칸이라도 어느 방향으로 들어왔는지에 따라 이후 코너 비용이 달라지므로, (칸, 진입 방향)을 하나의 상태로 두고 비용이 작은 상태부터 확정하는 다익스트라 탐색을 한다. 직선은 100원, 방향이 바뀌면 코너 500원을 더한다.
    # 시간 복잡도: O(N^2 * 4 * log(N^2 * 4))
    n = len(board)
    directions = [(-1, 0), (0, 1), (1, 0), (0, -1)]
    costs = [[[float('inf')] * 4 for _ in range(n)] for _ in range(n)]
    costs[0][0] = [0] * 4
    heap = [(0, 0, 0, -1)]  # -1은 출발 직후라 진입 방향이 없다는 뜻

    while heap:
        cost, row, col, prev_direction = heappop(heap)

        if prev_direction != -1 and cost > costs[row][col][prev_direction]:
            continue  # 이미 더 싼 비용으로 처리된 낡은 기록은 건너뜀

        for direction, (dr, dc) in enumerate(directions):
            nr, nc = row + dr, col + dc

            if not (0 <= nr < n and 0 <= nc < n):
                continue
            if board[nr][nc] == 1:
                continue

            next_cost = cost + 100
            if prev_direction != -1 and prev_direction != direction:  # 방향이 꺾이면 코너 발생
                next_cost += 500

            if next_cost < costs[nr][nc][direction]:
                costs[nr][nc][direction] = next_cost
                heappush(heap, (next_cost, nr, nc, direction))

    return min(costs[n - 1][n - 1])
