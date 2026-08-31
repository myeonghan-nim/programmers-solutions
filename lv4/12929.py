def solution(n):
    # dp[i] = 괄호 i쌍으로 만들 수 있는 올바른 문자열 수 (카탈란 수). 문자열을 "(안쪽)나머지" 꼴로 보면, 안쪽 left쌍 × 나머지 right쌍의 곱을 전부 더하면 된다.
    # 시간 복잡도: O(n^2)
    dp = [0] * (n + 1)
    dp[0] = 1

    for i in range(1, n + 1):
        for left in range(i):
            right = i - 1 - left  # 맨 앞 괄호 1쌍 + 안쪽 left쌍을 뺀 나머지
            dp[i] += dp[left] * dp[right]

    return dp[n]
