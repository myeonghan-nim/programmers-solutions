def solution(grid):
    # 각 칸의 두 삼각형은 가로 변 하나, 세로 변 하나로만 다른 칸의 삼각형과 닿는다.
    # 즉 삼각형마다 이웃이 최대 2개라, 전체 이웃 관계는 갈림길 없는 "사슬(경로)"과 "고리(사이클)"로 나뉜다.
    # 한 칸에서는 삼각형을 하나만 칠할 수 있으므로, 답 = 사슬/고리 위에서 같은 칸이 두 번 나오지 않는 가장 긴 연속 구간의 길이.
    # 시간 복잡도: O(N * M)
    n, m = len(grid), len(grid[0])

    def anchors(r, c):
        # 칸 (r, c)의 삼각형 0/1에 대해 (가로 변이 놓인 행 경계, 세로 변이 놓인 열 경계)를 돌려줌
        if grid[r][c] == 1:
            return ((r, c), (r + 1, c + 1))
        return ((r, c + 1), (r + 1, c))

    def neighbors(t):
        # 가로 변 건너편 칸, 세로 변 건너편 칸에서 같은 변을 공유하는 삼각형을 찾는다 (최대 2개)
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
        # start에서 한 방향으로 사슬을 따라간다. 이미 본 삼각형과 다시 만나면 고리라는 뜻
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
        # 같은 칸이 두 번 나오지 않는 가장 긴 연속 구간(투 포인터), 고리는 두 배로 이어 붙여 처리
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
    for t in tris:  # 끝점(이웃 1개 이하)에서 시작하는 사슬부터 처리
        if t not in visited and len(neighbors(t)) < 2:
            seq, _ = walk(t)
            best = max(best, longest([x[:2] for x in seq], False))
    for t in tris:  # 남은 삼각형은 전부 고리 위에 있음
        if t not in visited:
            seq, _ = walk(t)
            best = max(best, longest([x[:2] for x in seq], True))
    return best
