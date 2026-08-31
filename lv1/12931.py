def solution(n):
    # 10으로 나눈 나머지(맨 끝 자릿수)를 더하고, 몫으로 바꿔 자릿수를 하나씩 줄인다
    answer = 0
    while n > 0:
        answer += n % 10
        n //= 10
    return answer
