from collections import deque


def solution(n, path, order):
    # 동굴은 트리라서 어떤 방에 가려면 반드시 트리상의 부모 방을 먼저 지나야(방문해야) 한다. "부모 -> 자식" 화살표와 order의 "먼저 -> 나중" 화살표를 한 그래프에 모은 뒤, 화살표 순서를 지켜 n개 방을 전부 나열할 수 있는지(위상 정렬) 확인한다.
    # 시간 복잡도: O(n)
    tree = [[] for _ in range(n)]
    for a, b in path:
        tree[a].append(b)
        tree[b].append(a)

    graph = [[] for _ in range(n)]
    indegree = [0] * n

    # 입구(0번 방)에서 퍼져 나가며 각 방의 부모 -> 자식 화살표를 만든다
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

    # 받는 화살표가 없는 방부터 하나씩 지워 나간다(위상 정렬)
    queue = deque(node for node in range(n) if indegree[node] == 0)
    count = 0
    while queue:
        node = queue.popleft()
        count += 1
        for next_node in graph[node]:
            indegree[next_node] -= 1
            if indegree[next_node] == 0:
                queue.append(next_node)

    return count == n  # 전부 지워졌으면 순서 조건에 모순(순환)이 없다는 뜻
