from heapq import heappop, heappush


def solution(n, start, end, roads, traps):
    adj = [[] for _ in range(n + 1)]
    for u, v, c in roads:
        adj[u].append((v, c, 0))
        adj[v].append((u, c, 1))

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
            if (flipped ^ (1 if mask & bit[v] else 0)) != reverse:
                continue
            nmask = mask ^ bit[v]
            nd = d + c
            if nd < dist[v * size + nmask]:
                dist[v * size + nmask] = nd
                heappush(heap, (nd, v, nmask))
    return -1
