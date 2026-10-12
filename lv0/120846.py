def solution(n):
    # 합성수는 2 이상 자기 자신 미만의 수로 나누어떨어지는 수가 하나라도 있는 수이므로, 4부터 n까지 그런 수를 센다
    return sum(any(i % d == 0 for d in range(2, i)) for i in range(4, n + 1))
