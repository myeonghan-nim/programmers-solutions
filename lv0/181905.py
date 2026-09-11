def solution(my_string, s, e):
    # s 앞부분은 그대로 두고, s~e 구간만 뒤집은 뒤, e 뒷부분을 그대로 이어 붙인다
    return my_string[:s] + my_string[s:e + 1][::-1] + my_string[e + 1:]
