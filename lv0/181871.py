def solution(my_string, pat):
    # 겹치는 등장도 세야 하므로 모든 시작 위치마다 pat으로 시작하는지 확인해 개수를 더한다
    return sum(my_string.startswith(pat, i) for i in range(len(my_string)))
