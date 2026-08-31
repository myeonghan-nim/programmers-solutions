def solution(n, money):
    # 화폐 종류를 하나씩 추가해 가며 dp[i] = "지금까지의 화폐로 i원을 만드는 방법의 수"를 누적한다. 화폐 순서대로 채우므로 조합이 중복 계산되지 않는다.
    # 시간 복잡도: O(n * len(money))
    MOD = 1000000007

    dp = [0] * (n + 1)
    dp[0] = 1  # 0원을 만드는 방법은 아무것도 안 쓰는 1가지

    for coin in money:
        for i in range(coin, n + 1):
            # i원을 만들 때 coin을 하나 더 쓰는 경우를 더한다
            dp[i] = (dp[i] + dp[i - coin]) % MOD

    return dp[n]
