def solution(n, w, num):
    box_map = {k: [] for k in range(w)}
    for i in range(n):
        if (i // w) % 2:
            box_map[w - 1 - (i % w)].append(i)
        else:
            box_map[i % w].append(i)

    for k in box_map:
        idx = 1
        for v in box_map[k][::-1]:
            if v == num - 1:
                return idx
            idx += 1
    return -1
