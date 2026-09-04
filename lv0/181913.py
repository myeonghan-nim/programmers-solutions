def solution(my_string, queries):
    # 문자열은 바꿀 수 없으므로 글자 리스트로 바꾼 뒤, 각 쿼리 구간 [s, e]를 차례로 뒤집고 다시 합친다
    chars = list(my_string)
    for s, e in queries:
        chars[s:e + 1] = chars[s:e + 1][::-1]
    return "".join(chars)
