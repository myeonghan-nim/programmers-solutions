def solution(n):
    # 2부터 차례로 나눠 보며 나누어떨어지는 수(소인수)를 기록하고, 같은 소인수는 더 나눠지지 않을 때까지 전부 나눠 없애 중복 없이 오름차순으로 모은다
    factors = []
    d = 2
    while n > 1:
        if n % d == 0:
            factors.append(d)
            while n % d == 0:
                n //= d
        d += 1
    return factors
