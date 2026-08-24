MOD = 1_000_000_007


def solution(grid, d, k):
    n, m = len(grid), len(grid[0])
    N = n * m

    adj = [[] for _ in range(N)]
    for i in range(n):
        for j in range(m):
            for ni, nj in ((i - 1, j), (i + 1, j), (i, j - 1), (i, j + 1)):
                if 0 <= ni < n and 0 <= nj < m:
                    adj[i * m + j].append((ni * m + nj, grid[ni][nj] - grid[i][j]))

    M = [[int(u == v) for v in range(N)] for u in range(N)]
    for s in d:
        for u in range(N):
            row, nxt = M[u], [0] * N
            for v in range(N):
                if row[v]:
                    for w, slope in adj[v]:
                        if slope == s:
                            nxt[w] = (nxt[w] + row[v]) % MOD
            M[u] = nxt

    def matmul(A, B):
        C = [[0] * N for _ in range(N)]
        for i in range(N):
            Ai, Ci = A[i], C[i]
            for t in range(N):
                a = Ai[t]
                if a:
                    Bt = B[t]
                    for j in range(N):
                        Ci[j] += a * Bt[j]
            C[i] = [x % MOD for x in Ci]
        return C

    R = [[int(u == v) for v in range(N)] for u in range(N)]
    p = k
    while p:
        if p & 1:
            R = matmul(R, M)
        M = matmul(M, M)
        p >>= 1

    return sum(map(sum, R)) % MOD
