def solution(brown, yellow):
    for h in range(1, int(yellow ** 0.5) + 1):
        if not(yellow % h):
            w = yellow // h
            if 2 * (w + h + 2) == brown:
                return [w + 2, h + 2]
