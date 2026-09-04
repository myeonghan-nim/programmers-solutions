def solution(int_strs, k, s, l):
    # 각 문자열에서 s부터 l글자를 잘라 정수로 바꾼 뒤, k보다 큰 값만 순서대로 모은다
    return [n for x in int_strs if (n := int(x[s:s + l])) > k]
