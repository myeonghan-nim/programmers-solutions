def solution(n, w, num):
    # 상자를 쌓는 규칙 그대로 각 열(세로줄)에 상자를 쌓아 보고, num 상자가 있는 열의 맨 위에서부터 num까지 세면 꺼내야 하는 개수다
    box_map = {k: [] for k in range(w)}  # 열 번호 -> 아래부터 쌓인 상자 번호(0부터 셈)
    for i in range(n):
        if (i // w) % 2:  # i // w 는 층 번호. 홀수 층은 오른쪽에서 왼쪽으로 놓는다
            box_map[w - 1 - (i % w)].append(i)
        else:
            box_map[i % w].append(i)

    for k in box_map:
        idx = 1
        for v in box_map[k][::-1]:  # 맨 위 상자부터 아래로 확인
            if v == num - 1:
                return idx
            idx += 1
    return -1
