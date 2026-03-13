def solution(n):
    str_n = str(n)
    sorted_str = sorted(str_n, reverse=True)
    return int("".join(sorted_str))
