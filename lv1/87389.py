def solution(n):
    answer = n - 1

    if not (answer % 2):
        return 2
    if not (answer % 3):
        return 3

    i = 5
    while i * i <= answer:
        if not(answer % i):
            return i
        j = i + 2
        if not(answer % j):
            return j
        i += 6

    return answer
