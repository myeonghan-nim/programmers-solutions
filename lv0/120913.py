def solution(my_str, n):
    # 0, n, 2n, ... 위치에서 시작해 n글자씩 잘라 담는다. 마지막 조각은 n글자보다 짧아도 그대로 들어간다
    return [my_str[i:i + n] for i in range(0, len(my_str), n)]
