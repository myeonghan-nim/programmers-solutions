from collections import defaultdict, deque


def solution(tickets):
    graph = defaultdict(deque)
    for start, end in tickets:
        graph[start].append(end)

    for start in graph:
        graph[start] = deque(sorted(graph[start]))

    route = []
    stack = ['ICN']
    while stack:
        airport = stack[-1]
        if airport not in graph or not graph[airport]:
            route.append(stack.pop())
        else:
            stack.append(graph[airport].popleft())

    return route[::-1]
