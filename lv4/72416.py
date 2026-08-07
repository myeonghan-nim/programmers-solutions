def solution(sales, links):
    n = len(sales)
    children = [[] for _ in range(n + 1)]
    for leader, member in links:
        children[leader].append(member)

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
            extra = min(extra, take[child] - best)
        take[node] = base + sales[node - 1]
        skip[node] = base + (extra if children[node] else 0)

    return min(skip[1], take[1])
