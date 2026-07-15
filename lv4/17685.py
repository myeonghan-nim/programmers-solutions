def solution_trie(words):
    root = {}
    for w in words:
        node = root
        for ch in w:
            entry = node.setdefault(ch, [0, {}])
            entry[0] += 1
            node = entry[1]

    total = 0
    for w in words:
        node = root
        for i, ch in enumerate(w, 1):
            cnt, child = node[ch]
            if cnt == 1:
                total += i
                break
            node = child
        else:
            total += len(w)
    return total


def solution_sort(words):
    ws = sorted(words)

    def lcp(a, b):
        n = 0
        for x, y in zip(a, b):
            if x != y:
                break
            n += 1
        return n

    total = 0
    for i, w in enumerate(ws):
        left = lcp(w, ws[i - 1]) if i > 0 else 0
        right = lcp(w, ws[i + 1]) if i + 1 < len(ws) else 0
        total += min(len(w), max(left, right) + 1)
    return total
