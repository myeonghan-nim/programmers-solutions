from collections import deque


def solution(m, n, h, w, drops):
    # 칸마다 비가 떨어지는 순번을 적어 두면(안 떨어지는 칸은 가장 큰 값) 구역이 처음 비를 맞는 시점 = 구역 안 순번의 최솟값이다. 가로 w칸 최솟값을 먼저 구하고, 그 결과에 세로 h칸 최솟값을 한 번 더 구하면 모든 구역의 값이 나온다
    # 시간 복잡도: O(m * n)
    never = len(drops) + 1
    rain_order = [[never] * n for _ in range(m)]
    for order, (row, column) in enumerate(drops, 1):
        rain_order[row][column] = order

    def sliding_min(values, size):
        # 단조 덱: 뒤에 더 작은 값이 들어오면 앞선 큰 값은 다시는 최솟값이 될 수 없으므로 버린다. 덱 맨 앞이 항상 현재 구간의 최솟값 위치다
        candidates = deque()
        minimums = []
        for index, value in enumerate(values):
            while candidates and values[candidates[-1]] >= value:
                candidates.pop()
            candidates.append(index)
            if candidates[0] <= index - size:
                candidates.popleft()
            if index >= size - 1:
                minimums.append(values[candidates[0]])
        return minimums

    row_minimums = [sliding_min(row_values, w) for row_values in rain_order]
    area_minimums_by_column = [sliding_min(column_values, h) for column_values in zip(*row_minimums)]

    answer = [0, 0]
    latest = 0
    # 위쪽 행부터 보면서 더 늦을 때만 바꾸고, 행 안에서는 index가 가장 왼쪽 위치를 주므로 동률 규칙이 저절로 지켜진다
    for row, area_minimums in enumerate(zip(*area_minimums_by_column)):
        row_latest = max(area_minimums)
        if row_latest > latest:
            latest = row_latest
            answer = [row, area_minimums.index(row_latest)]
    return answer
