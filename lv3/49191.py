def solution(n, results):
    # A가 B를 이겼으면 A→B로 표시하고, "A가 k를 이기고 k가 B를 이기면 A는 B를 이긴다"는 식으로 모든 중간 선수 k를 거쳐 이기는 관계를 전부 채운다(플로이드-워셜 방식). 자신과 나머지 전원(n-1명)의 승패가 정해진 선수만 순위를 확정할 수 있다.
    # 시간 복잡도: O(n^3)
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
            if graph[i][j] or graph[j][i]:  # i가 이기든 지든 관계가 정해진 상대
                known += 1
        if known == n - 1:
            answer += 1

    return answer
