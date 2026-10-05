def solution(my_string):
    # dict.fromkeys는 키의 첫 등장 순서를 지키며 중복을 없애 주므로, 그 키들을 이어 붙이면 앞선 문자만 남는다
    return "".join(dict.fromkeys(my_string))
