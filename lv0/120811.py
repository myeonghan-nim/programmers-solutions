def solution(array):
    # 오름차순으로 정렬하면 한가운데 인덱스(길이의 절반 위치)에 중앙값이 온다
    return sorted(array)[len(array) // 2]
