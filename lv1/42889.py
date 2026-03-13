from collections import Counter


def solution(N, stages):
    n, counter = len(stages), Counter(stages)
    failure_rate = {}
    for stage in range(1, N + 1):
        count = counter.get(stage, 0)
        if not n:
            failure_rate[stage] = 0
        else:
            failure_rate[stage] = count / n
        n -= count
    return list(k for k, _ in sorted(failure_rate.items(), key=lambda item: item[1], reverse=True))
