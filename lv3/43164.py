from collections import defaultdict, deque


def solution(tickets):
    # 모든 표를 한 번씩 쓰는 한붓그리기 경로 찾기(히어홀저 방식). 각 공항의 도착지를 알파벳순으로 정렬해 두고, 갈 수 있는 한 계속 나아가다 막힌 공항부터 경로 확정 목록에 담는다. 마지막에 뒤집으면 답이 된다.
    # 시간 복잡도: O(E log E) (E = 표 수)
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
            route.append(stack.pop())  # 더 갈 곳이 없으면 경로 확정
        else:
            stack.append(graph[airport].popleft())  # 알파벳순으로 가장 빠른 도착지로 이동

    return route[::-1]
