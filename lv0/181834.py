def solution(my_string):
    # 문자끼리는 알파벳 순서로 크기 비교가 되므로("a" < "l"), "l"보다 앞서는 글자만 "l"로 바꿔 이어 붙인다
    return "".join(c if c >= "l" else "l" for c in my_string)
