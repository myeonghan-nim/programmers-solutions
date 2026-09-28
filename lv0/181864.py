def solution(my_string, pat):
    # translate로 A는 B로, B는 A로 한 번에 맞바꾼 뒤 pat이 부분 문자열로 들어 있는지 확인한다
    return int(pat in my_string.translate(str.maketrans("AB", "BA")))
