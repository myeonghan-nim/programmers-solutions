def solution(keyinput, board):
    # 키마다 이동량을 정해 두고 한 칸씩 움직이되, 움직인 좌표가 맵 절반 크기를 벗어나면 그 입력은 무시한다
    moves = {"up": (0, 1), "down": (0, -1), "left": (-1, 0), "right": (1, 0)}
    max_x, max_y = board[0] // 2, board[1] // 2
    x = y = 0
    for key in keyinput:
        dx, dy = moves[key]
        if abs(x + dx) <= max_x and abs(y + dy) <= max_y:
            x, y = x + dx, y + dy
    return [x, y]
