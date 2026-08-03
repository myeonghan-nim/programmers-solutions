def solution(land, height):
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
            parent[x] = parent[parent[x]]
            x = parent[x]
        return x

    answer = 0
    selected_count = 0

    for cost, cell_a, cell_b in edges:
        root_a = find(cell_a)
        root_b = find(cell_b)

        if root_a == root_b:
            continue

        if size[root_a] < size[root_b]:
            root_a, root_b = root_b, root_a

        parent[root_b] = root_a
        size[root_a] += size[root_b]
        answer += cost
        selected_count += 1

        if selected_count == vertex_count - 1:
            break

    return answer
