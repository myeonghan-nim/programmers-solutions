import math


def solution(n):
    # 약수는 (i, n÷i) 짝으로 나오므로 제곱근까지만 확인하며 짝을 함께 더한다
    # 시간 복잡도: O(√n)
    if n < 2:
        return n
    answer = 1 + n  # 1과 n 자신은 항상 약수
    for i in range(2, int(math.sqrt(n)) + 1):
        if n % i == 0:
            answer += i + (n // i if i != n // i else 0)  # i == n//i(제곱수)면 한 번만 더한다
    return answer
