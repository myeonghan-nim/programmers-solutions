from collections import deque


def solution(n, edge):
    # 1번 노드에서 가까운 노드부터 차례로 퍼져 나가는 탐색(BFS)으로 각 노드까지의 최단 거리를 구한 뒤, 가장 먼 거리에 있는 노드 수를 센다.
    # 시간 복잡도: O(n + 간선 수)
    graph = [[] for _ in range(n + 1)]
    for a, b in edge:
        graph[a].append(b)
        graph[b].append(a)

    distance = [-1] * (n + 1)  # -1은 아직 방문하지 않았다는 표시
    distance[1] = 0

    queue = deque([1])
    while queue:
        node = queue.popleft()
        for nxt in graph[node]:
            if distance[nxt] == -1:
                distance[nxt] = distance[node] + 1
                queue.append(nxt)

    max_distance = max(distance)
    return distance.count(max_distance)
