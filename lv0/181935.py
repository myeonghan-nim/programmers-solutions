def solution(n):
    # n이 홀수면 n 이하의 홀수를 모두 더하고, 짝수면 n 이하의 짝수를 제곱해서 더한다
    if n % 2 == 1:
        return sum(range(1, n + 1, 2))
    return sum(i * i for i in range(2, n + 1, 2))
