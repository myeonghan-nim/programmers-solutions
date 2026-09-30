def solution(n):
    # 행 번호 i와 열 번호 j가 같은 대각선 칸만 1이므로, i == j 비교 결과(True/False)를 int로 바꿔 1과 0을 채운다
    return [[int(i == j) for j in range(n)] for i in range(n)]
