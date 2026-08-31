def solution(brown, yellow):
    # 노란 격자는 (가로-2) x (세로-2) 크기의 직사각형이므로, yellow를 두 수의 곱 w x h로 쪼개 보며 테두리 갈색 격자 수가 2 * (w + h + 2) 와 맞아떨어지는 쌍을 찾는다.
    # 시간 복잡도: O(√yellow)
    for h in range(1, int(yellow**0.5) + 1):
        if not (yellow % h):
            w = yellow // h  # h를 제곱근까지만 돌리므로 항상 w >= h (가로 >= 세로 조건 만족)
            if 2 * (w + h + 2) == brown:
                return [w + 2, h + 2]
