def solution(edges, target):
    # 떨어트리는 횟수 D를 정하면 숫자들이 지나는 길은 완전히 정해진다(각 노드가 자식을 번호순으로 순환).
    # 리프가 t번 받으면 만들 수 있는 합은 t 이상 3t 이하이므로, 모든 리프가 3t >= target을 만족하는 최소 D를 이분 탐색으로 찾고, 각 리프에서 1을 앞에 몰고 남는 양을 뒤에 2, 3으로 채운다.
    # 시간 복잡도: O(n log ΣT + D * 트리 높이)  (D = 떨어트린 횟수)
    n = len(target)
    children = [[] for _ in range(n + 1)]
    for parent, child in edges:
        children[parent].append(child)
    for group in children:
        group.sort()  # 길은 번호가 작은 자식부터 차례로 돈다

    leaves = [v for v in range(1, n + 1) if not children[v]]

    def visits(drops):
        # count[v] = drops번 떨어트렸을 때 v를 지나는 숫자의 개수. 부모를 c번 지나면 i번째(0부터) 자식은 ceil((c - i) / 자식 수)번 받는다.
        count = [0] * (n + 1)
        count[1] = drops
        stack = [1]
        while stack:
            v = stack.pop()
            width = len(children[v])
            for i, child in enumerate(children[v]):
                count[child] = (count[v] - i + width - 1) // width
                stack.append(child)
        return count

    total = sum(target)
    low, high = 1, total
    while low < high:
        mid = (low + high) // 2
        count = visits(mid)
        if all(count[v] * 3 >= target[v - 1] for v in leaves):
            high = mid
        else:
            low = mid + 1

    count = visits(low)
    # 최소 D에서도 어떤 리프가 합을 못 만들면(방문이 모자라거나 넘치면) 불가능
    if any(count[v] * 3 < target[v - 1] or count[v] > target[v - 1] for v in leaves):
        return [-1]

    # 남는 양(target - t)을 2씩 묶어 3으로, 나머지 하나는 2로 만들고 1을 앞에 두면 사전순 최소
    plan = {}
    for v in leaves:
        times = count[v]
        threes, twos = divmod(target[v - 1] - times, 2)
        plan[v] = iter([1] * (times - threes - twos) + [2] * twos + [3] * threes)

    answer = []
    for drop in range(low):
        v, i = 1, drop  # drop번째 숫자가 도착하는 리프를 순환 규칙으로 계산
        while children[v]:
            width = len(children[v])
            v, i = children[v][i % width], i // width
        answer.append(next(plan[v]))
    return answer
