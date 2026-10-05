def solution(sides):
    # 정렬하면 마지막 원소가 가장 긴 변이므로, 그 변이 나머지 두 변의 합보다 작은지만 확인하면 된다
    sides.sort()
    return 1 if sides[2] < sides[0] + sides[1] else 2
