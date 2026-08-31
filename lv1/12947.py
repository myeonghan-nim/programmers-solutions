def solution(x):
    # 각 자릿수의 합을 구한 뒤, x가 그 합으로 나누어 떨어지면 하샤드 수
    original, digit_sum = x, 0
    while x > 0:
        digit_sum += x % 10
        x //= 10
    return not (original % digit_sum)  # 나머지가 0이면 True
