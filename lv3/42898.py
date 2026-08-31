def solution(m, n, puddles):
    # 각 칸까지의 최단경로 수 = 위 칸 경로 수 + 왼쪽 칸 경로 수, 물웅덩이는 0. 한 줄짜리 배열을 행마다 덮어써서 갱신 전 값(mat[x])을 위 칸 값으로 재활용한다.
    # 시간 복잡도: O(m * n)
    blocked = {tuple(puddle) for puddle in puddles}  # 웅덩이 좌표는 (x, y) 형식
    mat = [0] * (m + 1)
    mat[1] = 1  # 시작 칸 (1, 1)에 도달하는 방법 1가지
    for y in range(1, n + 1):
        for x in range(1, m + 1):
            if (x, y) in blocked:
                mat[x] = 0
            elif x > 1:
                mat[x] = (mat[x] + mat[x - 1]) % 1_000_000_007  # 위 칸 + 왼쪽 칸
    return mat[m]
