def solution(land, height):
    # 모든 칸을 가장 싸게 잇는 최소 신장 트리(MST) 문제. 이웃 칸 사이 높이차가 height 이하면 비용 0, 넘으면 높이차를 비용으로 하는 간선을 만들고, 싼 간선부터 서로소 집합(같은 묶음인지 빠르게 확인하는 구조)으로 사이클 없이 연결한다(크루스칼).
    # 시간 복잡도: O(N^2 log N)
    n = len(land)
    vertex_count = n * n
    edges = []

    for row in range(n):
        for col in range(n):
            cell = row * n + col

            if row + 1 < n:
                diff = abs(land[row][col] - land[row + 1][col])
                edges.append((0 if diff <= height else diff, cell, cell + n))

            if col + 1 < n:
                diff = abs(land[row][col] - land[row][col + 1])
                edges.append((0 if diff <= height else diff, cell, cell + 1))

    edges.sort()

    parent = list(range(vertex_count))
    size = [1] * vertex_count

    def find(x):
        while parent[x] != x:
            parent[x] = parent[parent[x]]  # 경로를 절반씩 줄여 다음 찾기를 빠르게
            x = parent[x]
        return x

    answer = 0
    selected_count = 0

    for cost, cell_a, cell_b in edges:
        root_a = find(cell_a)
        root_b = find(cell_b)

        if root_a == root_b:
            continue

        if size[root_a] < size[root_b]:  # 작은 묶음을 큰 묶음 밑에 붙인다
            root_a, root_b = root_b, root_a

        parent[root_b] = root_a
        size[root_a] += size[root_b]
        answer += cost
        selected_count += 1

        if selected_count == vertex_count - 1:
            break

    return answer
