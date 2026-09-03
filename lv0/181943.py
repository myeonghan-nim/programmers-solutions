def solution(my_string, overwrite_string, s):
    # 인덱스 s 앞부분 + 덮어쓸 문자열 + 덮인 구간 뒷부분을 이어 붙여 새 문자열을 만든다
    return my_string[:s] + overwrite_string + my_string[s + len(overwrite_string):]
