def solution(n, infection, edges, k):
    # 완전 탐색: 여는 종류의 순서를 전부 시도하며, 한 번 열 때마다 감염된 배양체들에서 그 종류의 파이프만 타고 퍼뜨린다. 같은 종류를 연달아 열면 새로 감염되는 곳이 없으므로 직전과 다른 종류만 고른다
    # 시간 복잡도: O(2^k * n)
    neighbors = {pipe_type: [[] for _ in range(n + 1)] for pipe_type in (1, 2, 3)}
    for x, y, pipe_type in edges:
        neighbors[pipe_type][x].append(y)
        neighbors[pipe_type][y].append(x)

    def max_infected(infected, last_type, remaining):
        if remaining == 0:
            return len(infected)
        best = len(infected)
        for pipe_type in (1, 2, 3):
            if pipe_type == last_type:
                continue
            spread = set(infected)
            stack = list(infected)
            while stack:
                node = stack.pop()
                for neighbor in neighbors[pipe_type][node]:
                    if neighbor not in spread:
                        spread.add(neighbor)
                        stack.append(neighbor)
            best = max(best, max_infected(spread, pipe_type, remaining - 1))
        return best

    return max_infected({infection}, 0, k)
