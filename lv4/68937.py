def solution(n, edges):
    if n < 3:
        return 0

    adj = [[] for _ in range(n + 1)]
    for u, v in edges:
        adj[u].append(v)
        adj[v].append(u)

    root = edges[0][0]
    parent = [root] * (n + 1)
    seen = bytearray(n + 1)
    seen[root] = 1
    order = [root]
    for v in order:
        for w in adj[v]:
            if not seen[w]:
                seen[w] = 1
                parent[w] = v
                order.append(w)

    down = [0] * (n + 1)
    for v in reversed(order[1:]):
        p = parent[v]
        if down[v] + 1 > down[p]:
            down[p] = down[v] + 1

    up = [-1] * (n + 1)
    for v in order:
        m1 = m2 = 0
        arg1 = -1
        for w in adj[v]:
            if w == parent[v]:
                continue
            d = down[w] + 1
            if d > m1:
                m1, m2, arg1 = d, m1, w
            elif d > m2:
                m2 = d
        base = up[v] if up[v] > 0 else 0
        for w in adj[v]:
            if w == parent[v]:
                continue
            sib = m2 if w == arg1 else m1
            up[w] = 1 + (base if base > sib else sib)

    ans = 0
    for v in order:
        b1 = b2 = b3 = 0
        deg = 0
        for w in adj[v]:
            d = up[v] if w == parent[v] else down[w] + 1
            deg += 1
            if d > b1:
                b1, b2, b3 = d, b1, b2
            elif d > b2:
                b2, b3 = d, b2
            elif d > b3:
                b3 = d
        if deg >= 2 and b1 + b3 > ans:
            ans = b1 + b3
    return ans
