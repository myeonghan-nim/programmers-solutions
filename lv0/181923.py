def solution(arr, queries):
    # 각 쿼리마다 구간 [s, e]에서 k보다 큰 값들만 골라 그중 최솟값을 답으로 하고, 없으면 -1로 한다
    return [min((num for num in arr[s:e + 1] if num > k), default=-1) for s, e, k in queries]
