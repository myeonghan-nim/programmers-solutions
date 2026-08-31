def solution(s):
    # 아직 짝을 못 찾은 여는 괄호 '('의 개수를 세면서 문자열을 한 번 훑는다. ')'가 나왔는데 짝이 될 '('가 없으면 그 즉시 올바르지 않은 괄호이다.
    # 시간 복잡도: O(n)
    left = 0
    for char in s:
        if char == "(":
            left += 1
        else:
            if left < 1:  # 짝이 될 '('가 없는데 ')'가 나온 경우
                return False
            else:
                left -= 1
    return not bool(left)  # 끝까지 봤을 때 '('가 남지 않아야 올바른 괄호
