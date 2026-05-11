def solution(sequence):
    answer = plus_current = minus_current = 0

    for index, number in enumerate(sequence):
        sign = 1 if index % 2 == 0 else -1
        plus_value = number * sign
        minus_value = -plus_value

        plus_current = max(plus_value, plus_current + plus_value)
        minus_current = max(minus_value, minus_current + minus_value)
        answer = max(answer, plus_current, minus_current)

    return answer