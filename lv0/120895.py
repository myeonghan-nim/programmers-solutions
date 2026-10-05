def solution(my_string, num1, num2):
    # 문자열은 직접 못 바꾸므로 리스트로 만들어 두 위치의 글자를 서로 바꾼 뒤 다시 이어 붙인다
    chars = list(my_string)
    chars[num1], chars[num2] = chars[num2], chars[num1]
    return "".join(chars)
