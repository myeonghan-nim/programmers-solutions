def solution(n, computers):
    # 방문 안 한 컴퓨터에서 출발해 연결된 컴퓨터를 전부 방문(깊이 우선 탐색)하는 일을 반복한다. 새로 출발한 횟수가 곧 네트워크(연결된 덩어리) 개수다.
    # 시간 복잡도: O(n^2)
    answer = 0
    visited = [False] * n
    for i in range(n):
        if not visited[i]:
            answer += 1  # 새 덩어리 발견
            stack = [i]
            visited[i] = True
            while stack:
                node = stack.pop()
                for j in range(n):
                    if computers[node][j] == 1 and not visited[j]:
                        visited[j] = True
                        stack.append(j)
    return answer
