def solution(n, s, a, b, fares):
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
                graph[i][j] = min(graph[i][j], graph[i][k] + graph[k][j])

    for i in range(1, n + 1):
        answer = min(answer, graph[s][i] + graph[i][a] + graph[i][b])

    return answer
