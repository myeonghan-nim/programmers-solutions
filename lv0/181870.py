def solution(str_arr):
    # "ad"가 들어 있지 않은 문자열만 순서대로 남긴다
    return [s for s in str_arr if 'ad' not in s]
