def solution(dot):
    # x와 y의 부호 조합으로 사분면이 정해진다: 둘 다 양수면 1, x만 음수면 2, 둘 다 음수면 3, y만 음수면 4
    x, y = dot
    if x > 0:
        return 1 if y > 0 else 4
    return 2 if y > 0 else 3
