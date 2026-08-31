def solution(strs, t):
    # dp[i] = t의 앞 i글자를 만드는 데 필요한 조각의 최소 개수. 만들 수 있는 위치 i마다 이어붙일 수 있는 조각을 모두 시도해 다음 위치를 갱신한다.
    # 시간 복잡도: O(len(t) * len(strs)) (조각 길이가 5 이하라 비교는 짧다)
    n = len(t)
    words = set(strs)

    INF = float('inf')
    dp = [INF] * (n + 1)
    dp[0] = 0

    for i in range(n):
        if dp[i] == INF:  # 앞 i글자를 만들 수 없으면 건너뛴다
            continue

        for word in words:
            if t.startswith(word, i):  # i번째 위치부터 word가 그대로 이어지는지 확인
                next_index = i + len(word)
                dp[next_index] = min(dp[next_index], dp[i] + 1)

    return dp[n] if dp[n] != INF else -1
