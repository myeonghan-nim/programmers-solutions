def solution(land):
    # 덩어리마다 한 번만 탐색해 크기와 걸쳐 있는 열 범위를 구하고, 그 범위의 모든 열에 크기를 더한다. 덩어리는 상하좌우로 이어져 있어 가장 왼쪽 열과 가장 오른쪽 열 사이의 열을 빠짐없이 지나므로 범위만 기억하면 된다
    # 시간 복잡도: O(n * m)
    rows, columns = len(land), len(land[0])
    visited = [[False] * columns for _ in range(rows)]
    oil_by_column = [0] * columns
    for start_row in range(rows):
        for start_column in range(columns):
            if not land[start_row][start_column] or visited[start_row][start_column]:
                continue
            visited[start_row][start_column] = True
            # 덩어리가 최대 25만 칸이라 재귀는 깊이 제한에 걸리므로 스택으로 탐색한다
            stack = [(start_row, start_column)]
            size = 0
            left = right = start_column
            while stack:
                row, column = stack.pop()
                size += 1
                left = min(left, column)
                right = max(right, column)
                for next_row, next_column in ((row - 1, column), (row + 1, column), (row, column - 1), (row, column + 1)):
                    if 0 <= next_row < rows and 0 <= next_column < columns and land[next_row][next_column] and not visited[next_row][next_column]:
                        visited[next_row][next_column] = True
                        stack.append((next_row, next_column))
            for column in range(left, right + 1):
                oil_by_column[column] += size
    return max(oil_by_column)
