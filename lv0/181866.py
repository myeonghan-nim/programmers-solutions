def solution(my_string):
    # "x"를 기준으로 잘라 빈 문자열을 버리고 사전순으로 정렬한다
    return sorted(s for s in my_string.split("x") if s)
