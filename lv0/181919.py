def solution(n):
    # 1이 될 때까지 짝수면 2로 나누고 홀수면 3배+1을 반복하며 거쳐 간 수를 모두 기록한다
    result = [n]
    while n != 1:
        n = n // 2 if n % 2 == 0 else 3 * n + 1
        result.append(n)
    return result
