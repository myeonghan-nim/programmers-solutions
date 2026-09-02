def solution(storage, num):
    # 같은 물건의 개수를 딕셔너리에 모아 더한 뒤, 개수가 가장 많은 물건의 이름을 찾는다
    counts = {}
    for name, n in zip(storage, num):
        counts[name] = counts.get(name, 0) + n
    return max(counts, key=lambda x: counts[x])
