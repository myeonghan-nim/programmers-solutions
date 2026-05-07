def solution(n, costs):
    parent = list(range(n))

    def find(x):
        if parent[x] != x:
            parent[x] = find(parent[x])
        return parent[x]

    answer = count = 0
    for a, b, cost in sorted(costs, key=lambda x: x[2]):
        a, b = find(a), find(b)
        if a != b:
            parent[b] = a
            answer += cost
            count += 1
            if count == n - 1:
                break

    return answer
