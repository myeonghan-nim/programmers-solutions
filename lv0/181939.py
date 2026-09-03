def solution(a, b):
    # a 뒤에 b를 붙인 수와 b 뒤에 a를 붙인 수를 만들어 더 큰 값을 고른다
    return max(int(str(a) + str(b)), int(str(b) + str(a)))
