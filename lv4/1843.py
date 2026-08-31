def solution(arr):
    # 구간을 둘로 쪼개는 DP: 구간 [i..j]에서 나올 수 있는 최댓값과 최솟값을 함께 기억한다. 빼기(-)는 뒤 구간의 "최솟값"을 빼야 결과가 커지므로 최솟값도 같이 관리해야 한다.
    # 시간 복잡도: O(n^3) (n은 숫자 개수, 최대 101)
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

            for k in range(i, j):  # k번째 연산자를 마지막에 계산한다고 가정하고 쪼갠다
                operator = operators[k]

                if operator == '+':
                    candidate_max = max_dp[i][k] + max_dp[k + 1][j]
                    candidate_min = min_dp[i][k] + min_dp[k + 1][j]
                else:
                    # 빼기: 최대가 되려면 뒤쪽의 최솟값을, 최소가 되려면 뒤쪽의 최댓값을 뺀다
                    candidate_max = max_dp[i][k] - min_dp[k + 1][j]
                    candidate_min = min_dp[i][k] - max_dp[k + 1][j]

                current_max = max(current_max, candidate_max)
                current_min = min(current_min, candidate_min)

            max_dp[i][j] = current_max
            min_dp[i][j] = current_min

    return max_dp[0][n - 1]
