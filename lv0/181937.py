def solution(num, n):
    # num을 n으로 나눈 나머지가 0이면 배수이므로 1, 아니면 0을 돌려준다
    return int(num % n == 0)
