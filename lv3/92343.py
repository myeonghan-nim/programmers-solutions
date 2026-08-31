def solution(info, edges):
    # 루트부터 시작해 "지금 갈 수 있는 노드 목록(candidates)"을 들고 다니며 그중 하나를 골라 방문하는 모든 순서를 시도하는 완전 탐색. 방문한 노드의 자식들이 새 후보로 추가되고, 늑대가 양 이상이 되는 선택은 바로 버린다.
    # 시간 복잡도: O(방문 순서의 조합 수) (노드가 최대 17개 + 가지치기로 제한 시간 내 동작)
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

            if next_wolf >= next_sheep:  # 양이 다 잡아먹히는 선택은 가지치기
                continue

            # 방문한 노드는 빼고 그 자식들을 새 후보로 넣는다
            next_candidates = candidates[:i] + candidates[i + 1:] + children[node]
            dfs(next_sheep, next_wolf, next_candidates)

    dfs(1, 0, children[0])  # 루트(0번)에는 항상 양이 있으므로 양 1마리로 시작
    return answer
