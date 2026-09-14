def solution(str_arr):
    # 홀수 인덱스 문자열은 대문자로, 짝수 인덱스 문자열은 소문자로 바꾼다
    return [s.upper() if i % 2 else s.lower() for i, s in enumerate(str_arr)]
