from heapq import heappop, heappush


def solution(n, start, end, roads, traps):
    # 함정은 최대 10개이므로 "각 함정을 홀수 번 밟았는지"를 비트마스크로 묶어 (방, 마스크) 상태에서 다익스트라(가장 싼 상태부터 확정하는 최단 경로)를 돌린다. 간선의 실제 방향은 양 끝 방의 뒤집힘 여부가 서로 같은지/다른지로 정해진다.
    # 시간 복잡도: O(2^t * (n + e) log(n * 2^t))  (t = 함정 수, e = 길 수)
    adj = [[] for _ in range(n + 1)]
    for u, v, c in roads:
        adj[u].append((v, c, 0))  # 원래 방향
        adj[v].append((u, c, 1))  # 뒤집혔을 때만 쓸 수 있는 방향

    bit = [0] * (n + 1)
    for i, trap in enumerate(traps):
        bit[trap] = 1 << i
    size = 1 << len(traps)

    dist = [float('inf')] * ((n + 1) * size)
    dist[start * size] = 0
    heap = [(0, start, 0)]
    while heap:
        d, u, mask = heappop(heap)
        if u == end:
            return d
        if d > dist[u * size + mask]:
            continue
        flipped = 1 if mask & bit[u] else 0
        for v, c, reverse in adj[u]:
            # 두 끝의 뒤집힘이 같으면 원래 방향, 다르면 반대 방향으로만 이동 가능
            if (flipped ^ (1 if mask & bit[v] else 0)) != reverse:
                continue
            nmask = mask ^ bit[v]  # 도착한 방이 함정이면 그 함정 상태를 뒤집음
            nd = d + c
            if nd < dist[v * size + nmask]:
                dist[v * size + nmask] = nd
                heappush(heap, (nd, v, nmask))
    return -1
