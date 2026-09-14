def solution(my_string):
    # 먼저 전부 소문자로 만든 뒤 'a'만 'A'로 바꾸면 조건을 한 번에 만족한다
    return my_string.lower().replace("a", "A")
