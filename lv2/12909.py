def solution(s):
    left = 0
    for char in s:
        if char == '(':
            left += 1
        else:
            if left < 1:
                return False
            else:
                left -= 1
    return not bool(left)
