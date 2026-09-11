import string


def solution(my_string):
    # 대문자 A~Z, 소문자 a~z 순서로 각 글자가 문자열에 몇 번 나오는지 세어 담는다
    return [my_string.count(ch) for ch in string.ascii_uppercase + string.ascii_lowercase]
