def solution(visible, hidden, k):
    n, m = len(visible), len(visible[0])
    if n > m:
        visible = [list(r) for r in zip(*visible)]
        hidden = [list(r) for r in zip(*hidden)]
        n, m = m, n

    both_even = n % 2 == 0 and m % 2 == 0
    best = None

    for mask in range(1 << n):
        base = k * bin(mask).count("1")
        S = 0
        cols = []
        for j in range(m):
            v0 = [hidden[i][j] if (mask >> i) & 1 else visible[i][j] for i in range(n)]
            v1 = [visible[i][j] if (mask >> i) & 1 else hidden[i][j] for i in range(n)]
            net0, net1 = sum(v0), sum(v1) - k
            S += max(net0, net1)
            cols.append((net0, net1, v0, v1))

        if not both_even:
            cand = S - base
        else:
            cand = None
            for j, (net0, net1, v0, v1) in enumerate(cols):
                rest = S - max(net0, net1)
                for net, vals in ((net0, v0), (net1, v1)):
                    for i in range(n):
                        if (i + j) % 2 == 1:
                            c = rest + net - vals[i] - base
                            if cand is None or c > cand:
                                cand = c

        if best is None or cand > best:
            best = cand
    return best
