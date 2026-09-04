def solution(arr, queries):
    # 각 쿼리 [i, j]마다 두 위치의 값을 서로 맞바꾼다
    for i, j in queries:
        arr[i], arr[j] = arr[j], arr[i]
    return arr
