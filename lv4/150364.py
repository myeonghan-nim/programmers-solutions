def solution(edges, target):
    n = len(target)
    children = [[] for _ in range(n + 1)]
    for parent, child in edges:
        children[parent].append(child)
    for group in children:
        group.sort()

    leaves = [v for v in range(1, n + 1) if not children[v]]

    def visits(drops):
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
    if any(count[v] * 3 < target[v - 1] or count[v] > target[v - 1] for v in leaves):
        return [-1]

    plan = {}
    for v in leaves:
        times = count[v]
        threes, twos = divmod(target[v - 1] - times, 2)
        plan[v] = iter([1] * (times - threes - twos) + [2] * twos + [3] * threes)

    answer = []
    for drop in range(low):
        v, i = 1, drop
        while children[v]:
            width = len(children[v])
            v, i = children[v][i % width], i // width
        answer.append(next(plan[v]))
    return answer
