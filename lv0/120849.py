def solution(my_string):
    # 문자열을 한 글자씩 보면서 모음(aeiou)이 아닌 글자만 골라 다시 이어 붙인다
    return "".join(c for c in my_string if c not in "aeiou")
