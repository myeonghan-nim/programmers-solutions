def solution(info, edges):
    n = len(info)
    children = [[] for _ in range(n)]

    for parent, child in edges:
        children[parent].append(child)

    answer = 0

    def dfs(sheep, wolf, candidates):
        nonlocal answer
        answer = max(answer, sheep)

        for i, node in enumerate(candidates):
            next_sheep = sheep + (info[node] == 0)
            next_wolf = wolf + (info[node] == 1)

            if next_wolf >= next_sheep:
                continue

            next_candidates = candidates[:i] + candidates[i + 1:] + children[node]
            dfs(next_sheep, next_wolf, next_candidates)

    dfs(1, 0, children[0])
    return answer
