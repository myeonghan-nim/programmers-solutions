def solution(n, edges):
    # 세 점을 잇는 경로들이 만나는 가운데 점 v를 고정하면, 세 거리의 중간값은 (v에서 뻗은 가지 중 가장 긴 것) + (세 번째로 긴 것)이 된다. 각 점에서 이웃 방향별 최장 거리를 아래(자식)/위(부모) 두 번의 순회로 모두 구해 최댓값을 찾는다.
    # 시간 복잡도: O(n)
    if n < 3:
        return 0

    adj = [[] for _ in range(n + 1)]
    for u, v in edges:
        adj[u].append(v)
        adj[v].append(u)

    # 재귀 없이: 뿌리에서부터의 방문 순서(order)를 만들어 두고 그 순서로 계산
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

    # down[v] = v에서 자식 쪽으로 내려갈 수 있는 최장 거리 (잎부터 거꾸로 계산)
    down = [0] * (n + 1)
    for v in reversed(order[1:]):
        p = parent[v]
        if down[v] + 1 > down[p]:
            down[p] = down[v] + 1

    # up[w] = w에서 부모 쪽으로 올라갈 때의 최장 거리 = 1 + max(부모의 위쪽 거리, 부모의 다른 자식 중 최장 가지)
    up = [-1] * (n + 1)
    for v in order:
        m1 = m2 = 0  # 자식 방향 가지 길이의 1등/2등 (1등인 자식에게는 2등을 물려줌)
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

    # 각 점에서 이웃 방향별 거리 중 1~3등을 뽑아 (1등 + 3등)이 답의 후보
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
