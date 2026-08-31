def solution(sales, links):
    # 트리 DP: take[v] = v가 참석할 때, skip[v] = v가 불참할 때의 최소 매출 합. v가 불참하면 v가 팀장인 팀을 위해 자식 중 최소 한 명은 참석해야 하므로, 자식마다 최적을 고른 뒤 "자식 하나를 참석으로 바꾸는 추가 비용"의 최솟값(extra)을 더한다.
    # 시간 복잡도: O(n)
    n = len(sales)
    children = [[] for _ in range(n + 1)]
    for leader, member in links:
        children[leader].append(member)

    # 재귀 대신 스택으로 방문 순서를 만들고, 거꾸로(잎부터) 계산한다
    order, stack = [], [1]
    while stack:
        node = stack.pop()
        order.append(node)
        stack.extend(children[node])

    skip = [0] * (n + 1)
    take = [0] * (n + 1)
    for node in reversed(order):
        base, extra = 0, float('inf')
        for child in children[node]:
            best = min(skip[child], take[child])
            base += best
            extra = min(extra, take[child] - best)  # 이 자식을 억지로 참석시킬 때 늘어나는 비용(이미 참석이 최적이면 0)
        take[node] = base + sales[node - 1]
        skip[node] = base + (extra if children[node] else 0)  # 잎은 팀장이 아니므로 추가 비용 없음

    return min(skip[1], take[1])
