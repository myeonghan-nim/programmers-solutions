def solution(dots):
    # 네 점을 두 쌍으로 나누는 방법은 3가지뿐이고, 두 직선의 기울기가 같은지는 나눗셈 대신 (dy1*dx2 == dy2*dx1) 곱셈 비교로 확인한다
    def parallel(p, q, r, s):
        return (q[1] - p[1]) * (s[0] - r[0]) == (s[1] - r[1]) * (q[0] - p[0])

    a, b, c, d = dots
    return 1 if parallel(a, b, c, d) or parallel(a, c, b, d) or parallel(a, d, b, c) else 0
