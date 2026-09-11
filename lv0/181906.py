def solution(my_string, is_prefix):
    # startswith는 문자열이 주어진 문자열로 시작하는지(접두사인지) 알려주므로 그 결과를 1/0으로 바꾼다
    return int(my_string.startswith(is_prefix))
