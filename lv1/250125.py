def solution(board, h, w):
    # 상하좌우 네 칸 중 보드 안에 있으면서 board[h][w]와 색이 같은 칸의 개수를 센다
    # 시간 복잡도: O(1)
    n = len(board)
    count = 0
    for dh, dw in ((0, 1), (1, 0), (-1, 0), (0, -1)):
        h_check, w_check = h + dh, w + dw
        if 0 <= h_check < n and 0 <= w_check < n and board[h_check][w_check] == board[h][w]:
            count += 1
    return count
