import sys

# 파이썬 정수 연산은 자릿수 제한이 없지만 문자열과 정수 사이 변환은 기본 4300자리로 막혀 있으므로 최대 10만 자리인 입력을 다루려면 제한을 풀어야 한다
sys.set_int_max_str_digits(0)


def solution(a, b):
    return str(int(a) + int(b))
