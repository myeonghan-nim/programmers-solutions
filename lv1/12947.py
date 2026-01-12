def solution(x):
    orginal_x, sum = x, 0
    while x > 0:
        sum += x % 10
        x //= 10
    return not (orginal_x % sum)
