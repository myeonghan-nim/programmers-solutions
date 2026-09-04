def solution(my_strings, parts):
    # 각 문자열에서 구간 [s, e]에 해당하는 부분(슬라이스 [s:e+1])을 잘라 순서대로 이어 붙인다
    return "".join(s[a:b + 1] for s, (a, b) in zip(my_strings, parts))
