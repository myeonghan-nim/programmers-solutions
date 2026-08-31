def solution(n, s, a, b, fares):
    # 모든 지점 쌍 사이의 최저 요금을 한 번에 구하는 플로이드-워셜을 돌린 뒤, 합승을 끝내고 헤어지는 지점 i를 전부 시도해 (s→i 합승) + (i→a) + (i→b)의 최솟값을 찾는다. i가 s이면 처음부터 따로 가는 경우도 자동으로 포함된다.
    # 시간 복잡도: O(n^3)
    answer = float('inf')
    graph = [[float('inf')] * (n + 1) for _ in range(n + 1)]

    for i in range(1, n + 1):
        graph[i][i] = 0

    for fare in fares:
        c, d, f = fare
        graph[c][d] = f
        graph[d][c] = f

    for k in range(1, n + 1):
        for i in range(1, n + 1):
            for j in range(1, n + 1):
                # k를 거쳐 가는 길이 더 싸면 갱신
                graph[i][j] = min(graph[i][j], graph[i][k] + graph[k][j])

    for i in range(1, n + 1):
        answer = min(answer, graph[s][i] + graph[i][a] + graph[i][b])

    return answer
