def solution(my_string):
    # 숫자는 모두 한 자리이므로, 문자열에서 숫자 글자만 골라 정수로 바꿔 전부 더한다
    return sum(int(c) for c in my_string if c.isdigit())
