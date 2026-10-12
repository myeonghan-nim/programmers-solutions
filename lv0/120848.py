def solution(n):
    # 1!부터 시작해 다음 팩토리얼이 n을 넘지 않는 동안 i를 하나씩 키워 가면, 멈춘 순간의 i가 i! ≤ n 을 만족하는 가장 큰 수다
    i = fact = 1
    while fact * (i + 1) <= n:
        i += 1
        fact *= i
    return i
