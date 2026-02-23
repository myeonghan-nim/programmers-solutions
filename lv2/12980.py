def solution(n):
    cnt = 0
    while n > 0:
        if n % 2:
            n -= 1
            cnt += 1
        else:
            n //= 2
    return cnt
