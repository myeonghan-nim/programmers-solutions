def solution(angle):
    # 90도와 180도를 경계로 위에서부터 차례로 비교해 예각(1), 직각(2), 둔각(3), 평각(4)을 판별한다
    if angle < 90:
        return 1
    if angle == 90:
        return 2
    if angle < 180:
        return 3
    return 4
