def solution(number, n, m):
    # n과 m 둘 다로 나눈 나머지가 0이면 공배수이므로 1, 아니면 0을 돌려준다
    return int(number % n == 0 and number % m == 0)
