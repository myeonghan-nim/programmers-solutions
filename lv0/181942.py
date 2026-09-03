def solution(str1, str2):
    # zip으로 두 문자열에서 같은 위치의 문자를 한 쌍씩 꺼내 번갈아 이어 붙인다
    return ''.join(a + b for a, b in zip(str1, str2))
