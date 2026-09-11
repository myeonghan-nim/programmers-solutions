def solution(str_list):
    # 앞에서부터 살피다 처음 만나는 것이 "l"이면 그 왼쪽을, "r"이면 그 오른쪽을 돌려주고, 둘 다 없으면 빈 리스트를 돌려준다
    for i, s in enumerate(str_list):
        if s == "l":
            return str_list[:i]
        if s == "r":
            return str_list[i + 1:]
    return []
