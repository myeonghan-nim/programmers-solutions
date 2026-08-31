def solution(n):
    # 숫자를 문자열로 바꿔 각 자릿수를 큰 순서로 정렬한 뒤 다시 정수로 만든다
    str_n = str(n)
    sorted_str = sorted(str_n, reverse=True)
    return int("".join(sorted_str))
