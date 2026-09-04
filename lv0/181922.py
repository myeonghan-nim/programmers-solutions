def solution(arr, queries):
    # 각 쿼리마다 구간 [s, e]를 돌며 k의 배수인 인덱스 위치의 값에 1을 더한다
    for s, e, k in queries:
        for i in range(s, e + 1):
            if k and i % k == 0:
                arr[i] += 1
    return arr
