def solution(m, n, puddles):
    blocked = {tuple(puddle) for puddle in puddles}
    mat = [0] * (m + 1)
    mat[1] = 1
    for y in range(1, n + 1):
        for x in range(1, m + 1):
            if (x, y) in blocked:
                mat[x] = 0
            elif x > 1:
                mat[x] = (mat[x] + mat[x - 1]) % 1_000_000_007
    return mat[m]
