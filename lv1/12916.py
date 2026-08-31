def solution(s):
    # 대소문자를 구별하지 않으므로 모두 소문자로 바꾼 뒤 p와 y의 개수를 비교한다
    s = s.lower()
    return s.count("p") == s.count("y")
