def solution(n, k):
    # k부터 n까지 k 간격으로 뛰면 k의 배수만 오름차순으로 나온다
    return list(range(k, n + 1, k))
