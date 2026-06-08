def solution(n, results):
    graph = [[False] * n for _ in range(n)]

    for winner, loser in results:
        graph[winner - 1][loser - 1] = True

    for k in range(n):
        for i in range(n):
            for j in range(n):
                if graph[i][k] and graph[k][j]:
                    graph[i][j] = True

    answer = 0
    for i in range(n):
        known = 0
        for j in range(n):
            if graph[i][j] or graph[j][i]:
                known += 1
        if known == n - 1:
            answer += 1

    return answer
