def solution(box, n):
    # 가로·세로·높이 각 방향에 주사위가 몇 개씩 들어가는지(길이 // n)를 구해 모두 곱하면 상자에 들어가는 전체 개수가 된다
    width, depth, height = box
    return (width // n) * (depth // n) * (height // n)
