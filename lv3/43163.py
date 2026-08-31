from collections import deque


def solution(begin, target, words):
    # 한 글자만 다른 단어끼리 이동할 수 있다고 보고, begin에서 target까지 너비 우선 탐색(가까운 단어부터 층층이 확인)으로 최소 변환 횟수를 찾는다.
    # 시간 복잡도: O(V^2 * L) (V = 단어 수, L = 단어 길이)
    if target not in words:
        return 0  # 목표 단어가 목록에 없으면 변환 불가

    def can_change(a, b):
        # 서로 다른 글자가 정확히 1개인지 확인
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
