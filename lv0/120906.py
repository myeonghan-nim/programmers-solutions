def solution(n):
    # 숫자를 문자열로 바꿔 한 글자씩 다시 정수로 만든 뒤 모두 더한다
    return sum(int(digit) for digit in str(n))
