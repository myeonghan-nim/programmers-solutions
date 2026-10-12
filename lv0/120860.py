def solution(dots):
    # 변이 축과 평행한 직사각형이므로 가로는 x좌표의 최대-최소, 세로는 y좌표의 최대-최소이고 넓이는 둘의 곱이다
    xs = [x for x, _ in dots]
    ys = [y for _, y in dots]
    return (max(xs) - min(xs)) * (max(ys) - min(ys))
