def solution(my_string):
    # 문자열에서 숫자 글자만 골라 정수로 바꾼 뒤 오름차순으로 정렬한다
    return sorted(int(c) for c in my_string if c.isdigit())
