def solution(m, n, start_x, start_y, balls):
    # 벽에 한 번 튕긴 경로는 목표 공을 그 벽 너머로 대칭 이동한 점까지의 직선과 길이가 같다. 네 벽에 대해 각각 구해 최솟값을 고르되, 벽으로 가는 길에 목표 공이 먼저 놓인 벽은 뺀다
    # 시간 복잡도: O(공의 수)
    answer = []
    for x, y in balls:
        dx_squared, dy_squared = (start_x - x) ** 2, (start_y - y) ** 2
        distances = []
        # 벽에 수직으로 쳐야 하는 같은 줄에서 목표 공이 벽 쪽에 있으면 벽보다 공에 먼저 맞으므로 그 벽은 쓸 수 없다
        if not (start_y == y and x < start_x):
            distances.append((start_x + x) ** 2 + dy_squared)  # 왼쪽 벽
        if not (start_y == y and x > start_x):
            distances.append((2 * m - start_x - x) ** 2 + dy_squared)  # 오른쪽 벽
        if not (start_x == x and y < start_y):
            distances.append(dx_squared + (start_y + y) ** 2)  # 아래쪽 벽
        if not (start_x == x and y > start_y):
            distances.append(dx_squared + (2 * n - start_y - y) ** 2)  # 위쪽 벽
        answer.append(min(distances))
    return answer
