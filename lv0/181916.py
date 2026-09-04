from collections import Counter


def solution(a, b, c, d):
    # 숫자별 등장 횟수를 세어 몇 종류가 나왔는지에 따라 문제의 점수 규칙에 그대로 대입한다
    counts = Counter([a, b, c, d])
    if len(counts) == 1:
        return 1111 * a
    if len(counts) == 2:
        p, q = sorted(counts, key=lambda x: counts[x], reverse=True)
        if counts[p] == 3:
            return (10 * p + q) ** 2
        return (p + q) * abs(p - q)
    if len(counts) == 3:
        q, r = (num for num in counts if counts[num] == 1)
        return q * r
    return min(a, b, c, d)
