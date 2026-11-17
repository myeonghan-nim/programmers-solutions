from collections import Counter


def solution(points, routes):
    # 로봇마다 실제로 한 칸씩 움직여 보면서 (시각, r, c)에 몇 대가 있었는지 센다. 같은 시각 같은 좌표에 2대 이상이면 몇 대가 모였든 위험 상황 1번이다
    # 시간 복잡도: O(x * m * L), L은 포인트 사이 최대 이동 거리(좌표가 100 이하라 최대 198)
    visits = Counter()
    for route in routes:
        row, column = points[route[0] - 1]
        time = 0
        visits[time, row, column] += 1
        for point_number in route[1:]:
            target_row, target_column = points[point_number - 1]
            # r 좌표를 먼저 다 맞춘 뒤 c 좌표를 맞춘다
            while (row, column) != (target_row, target_column):
                if row != target_row:
                    row += 1 if row < target_row else -1
                else:
                    column += 1 if column < target_column else -1
                time += 1
                visits[time, row, column] += 1
    return sum(robot_count >= 2 for robot_count in visits.values())
