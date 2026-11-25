from math import isqrt


def solution(r1, r2):
    # x > 0, y >= 0인 영역(1사분면 + 양의 x축)만 세고 4를 곱한다. 이 영역을 90도씩 돌리면 원점을 뺀 모든 점을 겹치지 않게 덮기 때문이다. x마다 가능한 y는 작은 원 밖 최소 정수부터 큰 원 안 최대 정수까지다
    # 시간 복잡도: O(r2)
    count = 0
    for x in range(1, r2 + 1):
        y_max = isqrt(r2 * r2 - x * x)
        # 작은 원 위의 점도 포함이므로 sqrt(r1^2 - x^2)의 올림이 필요하다. 실수 오차를 피하려고 isqrt(n - 1) + 1로 올림을 구한다
        y_min = isqrt(r1 * r1 - x * x - 1) + 1 if x < r1 else 0
        count += y_max - y_min + 1
    return count * 4
