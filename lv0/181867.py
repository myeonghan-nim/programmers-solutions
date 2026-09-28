def solution(my_string):
    # "x"를 기준으로 자른 각 조각의 길이를 순서대로 담는다 (빈 조각의 길이 0도 포함)
    return [len(s) for s in my_string.split("x")]
