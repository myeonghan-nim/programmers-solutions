def solution(A, B):
    A.sort()
    B.sort()

    n = len(A)
    a, b = 0, 0
    count = 0
    while a < n and b < n:
        if A[a] < B[b]:
            count += 1
            a += 1
            b += 1
        else:
            b += 1
    return count
