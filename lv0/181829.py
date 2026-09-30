def solution(board, k):
    # 모든 칸을 훑으며 행 번호 i와 열 번호 j의 합이 k 이하인 칸의 값만 더한다
    return sum(value for i, row in enumerate(board) for j, value in enumerate(row) if i + j <= k)
