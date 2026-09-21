def solution(k, num, links):
    n = len(num)

    is_child = [False] * n
    for left, right in links:
        if left != -1:
            is_child[left] = True
        if right != -1:
            is_child[right] = True

    root = is_child.index(False)

    order = []
    stack = [root]
    while stack:
        node = stack.pop()
        order.append(node)

        left, right = links[node]
        if left != -1:
            stack.append(left)
        if right != -1:
            stack.append(right)

    order.reverse()

    def feasible(limit):
        remain = [0] * n
        cuts = 0

        for node in order:
            left, right = links[node]
            a = remain[left] if left != -1 else 0
            b = remain[right] if right != -1 else 0
            w = num[node]

            if w + a + b <= limit:
                remain[node] = w + a + b
            elif w + min(a, b) <= limit:
                cuts += 1
                remain[node] = w + min(a, b)
            else:
                cuts += 2
                remain[node] = w

            if cuts >= k:
                return False

        return True

    total = sum(num)
    low = max(max(num), (total + k - 1) // k)
    high = total
    while low < high:
        mid = (low + high) // 2

        if feasible(mid):
            high = mid
        else:
            low = mid + 1

    return low
