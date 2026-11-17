def solution(storage, requests):
    # 창고 둘레에 빈칸을 한 겹 두르면 "외부와 연결"은 (0, 0)에서 빈칸만 밟아 닿을 수 있다는 뜻이 된다. 지게차 요청마다 바깥에서 빈칸을 따라 퍼져 나가며 맞닿은 요청 종류 컨테이너를 모은다
    # 시간 복잡도: O(len(requests) * n * m)
    row_count, column_count = len(storage) + 2, len(storage[0]) + 2
    grid = [[""] * column_count] + [[""] + list(line) + [""] for line in storage] + [[""] * column_count]

    for request in requests:
        kind = request[0]
        if len(request) == 2:
            removable = [(row, column) for row in range(row_count) for column in range(column_count) if grid[row][column] == kind]
        else:
            removable = []
            visited = [[False] * column_count for _ in range(row_count)]
            visited[0][0] = True
            stack = [(0, 0)]
            while stack:
                row, column = stack.pop()
                for next_row, next_column in ((row + 1, column), (row - 1, column), (row, column + 1), (row, column - 1)):
                    if not (0 <= next_row < row_count and 0 <= next_column < column_count) or visited[next_row][next_column]:
                        continue
                    visited[next_row][next_column] = True  # 컨테이너 칸도 방문 표시를 해 두어 같은 컨테이너를 두 번 모으지 않는다
                    if grid[next_row][next_column] == "":
                        stack.append((next_row, next_column))
                    elif grid[next_row][next_column] == kind:
                        removable.append((next_row, next_column))
        # 탐색이 끝난 뒤 한꺼번에 꺼내야 한다. 탐색 도중에 꺼내면 그 뒤에 숨어 있던 컨테이너까지 같은 요청에서 꺼내진다
        for row, column in removable:
            grid[row][column] = ""

    return sum(cell != "" for line in grid for cell in line)
