def solution(arr, query):
    # 짝수 번째 쿼리는 해당 인덱스까지만 남기고(뒷부분 버림), 홀수 번째 쿼리는 해당 인덱스부터만 남긴다(앞부분 버림)
    for i, q in enumerate(query):
        arr = arr[:q + 1] if i % 2 == 0 else arr[q:]
    return arr
