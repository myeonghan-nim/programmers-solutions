def solution(n, works):
    if sum(works) <= n:
        return 0

    works.sort(reverse=True)
    works.append(0)
    for i in range(len(works) - 1):
        cur = works[i]
        nxt = works[i + 1]
        cnt = i + 1
        need = (cur - nxt) * cnt

        if n >= need:
            n -= need
            continue

        q, r = divmod(n, cnt)
        base = cur - q

        answer = r * (base - 1) ** 2
        answer += (cnt - r) * base ** 2
        answer += sum(w * w for w in works[i + 1:-1])
        return answer

    return 0
