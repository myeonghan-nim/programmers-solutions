def solution(A, B):
    a = len(A)
    A.sort()
    B.sort()
    return sum([A[i] * B[a - 1 - i] for i in range(a)])
