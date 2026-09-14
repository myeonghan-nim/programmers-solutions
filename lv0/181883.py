def solution(arr, queries):
    # 각 쿼리 [s, e]마다 s부터 e까지 구간의 원소에 1씩 더한다
    for s, e in queries:
        for i in range(s, e + 1):
            arr[i] += 1
    return arr
