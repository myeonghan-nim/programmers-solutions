MOD = 1_000_000_007


def solution(grid, d, k):
    # 칸(최대 64개)을 정점으로 보고, 경사 수열 d를 한 번 통과하는 이동을 행렬 mat(mat[u][v] = u에서 출발해 v에 도착하는 경우의 수)으로 만든 뒤, mat을 k번 곱한 결과(mat^k)를 거듭제곱 반복(이진법 분할)으로 구해 전체 합을 낸다.
    # 시간 복잡도: O(|d| * N^2 + N^3 log k)  (N = 칸 수)
    n, m = len(grid), len(grid[0])
    size = n * m

    adj = [[] for _ in range(size)]  # 각 칸에서 상하좌우 칸으로의 (이웃, 경사) 목록
    for i in range(n):
        for j in range(m):
            for ni, nj in ((i - 1, j), (i + 1, j), (i, j - 1), (i, j + 1)):
                if 0 <= ni < n and 0 <= nj < m:
                    adj[i * m + j].append((ni * m + nj, grid[ni][nj] - grid[i][j]))

    # 단위 행렬에서 시작해, d의 경사 s와 일치하는 이동만 한 단계씩 반영해 mat을 만든다
    mat = [[int(u == v) for v in range(size)] for u in range(size)]
    for s in d:
        for u in range(size):
            row, nxt = mat[u], [0] * size
            for v in range(size):
                if row[v]:
                    for w, slope in adj[v]:
                        if slope == s:
                            nxt[w] = (nxt[w] + row[v]) % MOD
            mat[u] = nxt

    def matmul(a, b):
        # 0인 원소를 건너뛰고, 나머지는 마지막에 한 번만 나눠(%) 빠르게 곱한다
        c = [[0] * size for _ in range(size)]
        for i in range(size):
            ai, ci = a[i], c[i]
            for t in range(size):
                val = ai[t]
                if val:
                    bt = b[t]
                    for j in range(size):
                        ci[j] += val * bt[j]
            c[i] = [x % MOD for x in ci]
        return c

    result = [[int(u == v) for v in range(size)] for u in range(size)]
    p = k
    while p:  # k를 이진법으로 쪼개 log k번의 곱으로 mat^k 계산
        if p & 1:
            result = matmul(result, mat)
        mat = matmul(mat, mat)
        p >>= 1

    return sum(map(sum, result)) % MOD  # 모든 (시작 칸, 끝 칸) 쌍의 경로 수 합
