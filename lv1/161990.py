def solution(wallpaper):
    # 파일 칸들의 좌표를 모은 뒤, 가장 작은 행·열을 시작점으로, 가장 큰 행·열 + 1을 끝점으로 삼는다
    # 시간 복잡도: O(H × W)
    files = [(i, j) for i, row in enumerate(wallpaper) for j, cell in enumerate(row) if cell == "#"]
    rows, cols = zip(*files)
    return [min(rows), min(cols), max(rows) + 1, max(cols) + 1]
