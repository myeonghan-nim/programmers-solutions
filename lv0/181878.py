def solution(my_string, pat):
    # 대소문자를 구분하지 않으므로 둘 다 소문자로 맞춘 뒤 포함 여부를 확인한다
    return int(pat.lower() in my_string.lower())
