def solution(a, b):
    # 두 수를 문자열로 이어 붙여 만든 수와 2 * a * b 중 큰 값을 고른다. 둘이 같아도 값이 같으므로 max로 충분하다
    return max(int(str(a) + str(b)), 2 * a * b)
