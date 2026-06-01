def solution(a):
    answer = 0

    min_value = float('inf')
    for x in a:
        if x < min_value:
            answer += 1
            min_value = x

    min_value = float('inf')
    for x in reversed(a):
        if x < min_value:
            answer += 1
            min_value = x

    return answer - 1
