from collections import deque


def solution(begin, target, words):
    if target not in words:
        return 0

    def can_change(a, b):
        return sum(x != y for x, y in zip(a, b)) == 1

    q = deque([(begin, 0)])
    visited = {begin}
    while q:
        cur, dist = q.popleft()
        if cur == target:
            return dist

        for nxt in words:
            if nxt not in visited and can_change(cur, nxt):
                visited.add(nxt)
                q.append((nxt, dist + 1))

    return 0
