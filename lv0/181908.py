def solution(my_string, is_suffix):
    # endswith는 문자열이 주어진 문자열로 끝나는지(접미사인지) 알려주므로 그 결과를 1/0으로 바꾼다
    return int(my_string.endswith(is_suffix))
