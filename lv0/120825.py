def solution(my_string, n):
    # 각 문자를 n번 곱해 늘린 뒤 join으로 이어 붙인다
    return "".join(c * n for c in my_string)
