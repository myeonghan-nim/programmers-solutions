import re


def solution(my_string):
    # 정규식 \d+ 로 연속된 숫자 덩어리를 통째로 찾아 각각 정수로 바꿔 더한다
    return sum(int(num) for num in re.findall(r"\d+", my_string))
