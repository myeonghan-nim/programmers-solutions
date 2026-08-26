def solution(grid):
    n, m = len(grid), len(grid[0])

    def anchors(r, c):
        if grid[r][c] == 1:
            return ((r, c), (r + 1, c + 1))
        return ((r, c + 1), (r + 1, c))

    def neighbors(t):
        r, c, i = t
        ar, ac = anchors(r, c)[i]
        out = []
        nr = r - 1 if ar == r else r + 1
        if 0 <= nr < n:
            for j, (br, _) in enumerate(anchors(nr, c)):
                if br == ar:
                    out.append((nr, c, j))
        nc = c - 1 if ac == c else c + 1
        if 0 <= nc < m:
            for j, (_, bc) in enumerate(anchors(r, nc)):
                if bc == ac:
                    out.append((r, nc, j))
        return out

    visited = set()

    def walk(start):
        seq, cur, pv = [start], start, None
        visited.add(start)
        while True:
            nxts = [x for x in neighbors(cur) if x != pv]
            if not nxts:
                return seq, False
            nxt = nxts[0]
            if nxt in visited:
                return seq, True
            visited.add(nxt)
            seq.append(nxt)
            pv, cur = cur, nxt

    def longest(cells, cyclic):
        if len(set(cells)) == len(cells):
            return len(cells)
        seq = cells + cells if cyclic else cells
        last, lo, best = {}, 0, 0
        for hi, cell in enumerate(seq):
            if cell in last and last[cell] >= lo:
                lo = last[cell] + 1
            last[cell] = hi
            best = max(best, hi - lo + 1)
        return best

    tris = [(r, c, i) for r in range(n) for c in range(m) for i in (0, 1)]
    best = 0
    for t in tris:
        if t not in visited and len(neighbors(t)) < 2:
            seq, _ = walk(t)
            best = max(best, longest([x[:2] for x in seq], False))
    for t in tris:
        if t not in visited:
            seq, _ = walk(t)
            best = max(best, longest([x[:2] for x in seq], True))
    return best
