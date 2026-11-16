def solution(info, n, m):
    # 배낭 DP: min_a_trace[b] = B의 흔적 합이 정확히 b일 때 A 흔적 합의 최솟값. 물건마다 A가 훔치면 A 흔적이 늘고, B가 훔치면 b 칸이 옮겨 간다. B는 m 미만만 허용하므로 칸은 m개면 충분하다
    # 시간 복잡도: O(len(info) * m)
    unreachable = float("inf")
    min_a_trace = [0] + [unreachable] * (m - 1)
    for a_trace, b_trace in info:
        # 같은 물건을 두 번 반영하지 않도록 뒤에서부터 갱신한다 (b - b_trace 칸은 아직 이전 물건까지의 값이다)
        for b in range(m - 1, -1, -1):
            stolen_by_b = min_a_trace[b - b_trace] if b >= b_trace else unreachable
            min_a_trace[b] = min(min_a_trace[b] + a_trace, stolen_by_b)
    answer = min(min_a_trace)
    return answer if answer < n else -1
