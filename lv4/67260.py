from collections import deque


def solution(n, path, order):
    tree = [[] for _ in range(n)]
    for a, b in path:
        tree[a].append(b)
        tree[b].append(a)

    graph = [[] for _ in range(n)]
    indegree = [0] * n

    visited = [False] * n
    visited[0] = True
    queue = deque([0])
    while queue:
        node = queue.popleft()
        for next_node in tree[node]:
            if not visited[next_node]:
                visited[next_node] = True
                graph[node].append(next_node)
                indegree[next_node] += 1
                queue.append(next_node)

    for a, b in order:
        graph[a].append(b)
        indegree[b] += 1

    queue = deque(node for node in range(n) if indegree[node] == 0)
    count = 0
    while queue:
        node = queue.popleft()
        count += 1
        for next_node in graph[node]:
            indegree[next_node] -= 1
            if indegree[next_node] == 0:
                queue.append(next_node)

    return count == n
