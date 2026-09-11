def solution(arr, intervals):
    # 닫힌 구간 [a, b]는 슬라이스 arr[a:b+1]에 해당하므로 두 구간을 각각 잘라 이어 붙인다
    (a, b), (c, d) = intervals
    return arr[a:b + 1] + arr[c:d + 1]
