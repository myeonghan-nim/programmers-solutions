def solution(emergency):
    # 내림차순으로 정렬한 리스트에서 각 응급도가 몇 번째(1부터)에 있는지가 진료 순서다
    order = sorted(emergency, reverse=True)
    return [order.index(e) + 1 for e in emergency]
