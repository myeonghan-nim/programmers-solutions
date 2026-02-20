from collections import Counter


def solution(k, tangerine):
    for cnt, v in enumerate(sorted(Counter(tangerine).values(), reverse=True), 1):
        k -= v
        if k <= 0:
            return cnt
