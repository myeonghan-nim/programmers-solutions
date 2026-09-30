def solution(str_list, ex):
    # ex가 들어 있지 않은 문자열만 골라 순서대로 이어 붙인다
    return "".join(s for s in str_list if ex not in s)
