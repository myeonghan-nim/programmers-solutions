def solution(n, computers):
    answer = 0
    visited = [False] * n
    for i in range(n):
        if not visited[i]:
            answer += 1
            stack = [i]
            visited[i] = True
            while stack:
                node = stack.pop()
                for j in range(n):
                    if computers[node][j] == 1 and not visited[j]:
                        visited[j] = True
                        stack.append(j)
    return answer
