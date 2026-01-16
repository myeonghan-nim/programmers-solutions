def solution(n):
    answer = []
    while n > 0:
        digit = n % 10
        answer.append(digit)
        n //= 10
    return answer
