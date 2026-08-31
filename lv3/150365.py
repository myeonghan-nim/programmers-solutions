def solution(n, m, x, y, r, c, k):
    # 매 걸음마다 사전 순으로 빠른 d < l < r < u 순서로 시도해서, "남은 걸음 수로 도착지에 갈 수 있는" 첫 방향을 고르는 그리디 방식. 갈 수 있다는 조건: 도착지까지 거리 <= 남은 걸음 수이고, 남는 걸음이 짝수(왕복으로 소모 가능).
    # 시간 복잡도: O(k)
    if abs(x - r) + abs(y - c) > k or (k - abs(x - r) - abs(y - c)) % 2 != 0:  # 시작부터 불가능한 경우
        return 'impossible'

    directions = [('d', 1, 0), ('l', 0, -1), ('r', 0, 1), ('u', -1, 0)]
    path = []
    current_x, current_y = x, y
    for _ in range(k):
        for direction, dx, dy in directions:
            next_x, next_y = current_x + dx, current_y + dy
            if 1 <= next_x <= n and 1 <= next_y <= m:
                remaining_distance = abs(next_x - r) + abs(next_y - c)
                # 이 칸으로 간 뒤에도 남은 걸음으로 도착지에 정확히 도달할 수 있어야 한다
                if remaining_distance <= k - len(path) - 1 and (k - len(path) - 1 - remaining_distance) % 2 == 0:
                    path.append(direction)
                    current_x, current_y = next_x, next_y
                    break
    return ''.join(path)
