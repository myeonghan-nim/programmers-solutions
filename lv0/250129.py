def solution(route):
    # 동쪽 좌표는 E 개수에서 W 개수를 뺀 값, 북쪽 좌표는 N 개수에서 S 개수를 뺀 값이다
    return [route.count("E") - route.count("W"), route.count("N") - route.count("S")]
