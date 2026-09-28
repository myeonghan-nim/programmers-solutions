def solution(arr):
    # 배열 길이보다 크거나 같아질 때까지 2를 거듭 곱해 목표 길이를 찾고, 모자란 만큼 뒤에 0을 붙인다
    n = 1
    while n < len(arr):
        n *= 2
    return arr + [0] * (n - len(arr))
