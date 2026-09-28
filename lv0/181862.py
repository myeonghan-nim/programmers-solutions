import re


def solution(my_str):
    # a, b, c 중 아무 글자나 만나면 그 자리에서 문자열을 자르고, 빈 조각은 버린다; 남는 조각이 없으면 ["EMPTY"]
    return [s for s in re.split("[abc]", my_str) if s] or ["EMPTY"]
