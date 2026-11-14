from itertools import groupby


def solution(arr):
    # groupby는 연속으로 같은 값을 한 묶음으로 만들어 주므로, 묶음마다 대표 값 하나씩만 모으면 순서를 유지한 채 연속 중복이 사라진다
    # 시간 복잡도: O(n), n은 arr의 길이
    return [number for number, _ in groupby(arr)]
