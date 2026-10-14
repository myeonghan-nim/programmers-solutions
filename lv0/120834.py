def solution(age):
    # 나이를 문자열로 바꿔 각 자리 숫자를 "abcdefghij"에서 그 숫자 번째 알파벳(0은 a, 9는 j)으로 바꾼다
    return "".join("abcdefghij"[int(d)] for d in str(age))
