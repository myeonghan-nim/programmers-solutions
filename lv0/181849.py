def solution(num_str):
    # 문자열의 각 글자를 정수로 바꿔 모두 더한다
    return sum(int(digit) for digit in num_str)
