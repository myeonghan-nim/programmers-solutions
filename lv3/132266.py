from collections import deque


def solution(n, roads, sources, destination):
    # 부대원마다 따로 찾지 않고, 도착지(부대)에서 한 번만 BFS(가까운 지역부터 차례로 퍼져 나가는 탐색)를 돌려 모든 지역까지의 최단 거리를 구한다. 길을 지나는 시간이 전부 1이라 BFS만으로 최단 거리가 보장된다.
    # 시간 복잡도: O(n + 길 수)
    graph = [[] for _ in range(n + 1)]
    for a, b in roads:
        graph[a].append(b)
        graph[b].append(a)

    dist = [-1] * (n + 1)  # -1은 도달 불가(복귀 불가능) 표시로 그대로 답이 된다
    dist[destination] = 0
    queue = deque([destination])

    while queue:
        node = queue.popleft()
        for next_node in graph[node]:
            if dist[next_node] == -1:
                dist[next_node] = dist[node] + 1
                queue.append(next_node)

    return [dist[source] for source in sources]
