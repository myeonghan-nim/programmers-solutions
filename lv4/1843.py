def solution(arr):
    numbers = list(map(int, arr[::2]))
    operators = arr[1::2]

    n = len(numbers)
    max_dp = [[0] * n for _ in range(n)]
    min_dp = [[0] * n for _ in range(n)]
    for i in range(n):
        max_dp[i][i] = numbers[i]
        min_dp[i][i] = numbers[i]

    for length in range(2, n + 1):
        for i in range(n - length + 1):
            j = i + length - 1

            current_max = float('-inf')
            current_min = float('inf')

            for k in range(i, j):
                operator = operators[k]

                if operator == '+':
                    candidate_max = max_dp[i][k] + max_dp[k + 1][j]
                    candidate_min = min_dp[i][k] + min_dp[k + 1][j]
                else:
                    candidate_max = max_dp[i][k] - min_dp[k + 1][j]
                    candidate_min = min_dp[i][k] - max_dp[k + 1][j]

                current_max = max(current_max, candidate_max)
                current_min = min(current_min, candidate_min)

            max_dp[i][j] = current_max
            min_dp[i][j] = current_min

    return max_dp[0][n - 1]
