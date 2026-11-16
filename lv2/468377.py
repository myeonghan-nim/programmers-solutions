def solution(cost, hint):
    # 완전 탐색: 스테이지마다 번들을 살지 말지 두 갈래로 모두 시도한다. 힌트권은 많이 쓸수록 비용이 줄고 다른 스테이지에는 못 쓰므로, 가진 만큼(최대 n - 1장) 전부 쓰는 것이 항상 최선이다
    # 시간 복잡도: O(2^n * k) (k는 번들 한 개의 힌트권 수)
    n = len(cost)
    ticket_counts = [0] * n

    def min_cost(stage):
        clear_cost = cost[stage][min(ticket_counts[stage], n - 1)]
        if stage == n - 1:
            return clear_cost
        without_bundle = min_cost(stage + 1)
        price, *ticket_numbers = hint[stage]
        for number in ticket_numbers:
            ticket_counts[number - 1] += 1
        with_bundle = price + min_cost(stage + 1)
        for number in ticket_numbers:
            ticket_counts[number - 1] -= 1
        return clear_cost + min(without_bundle, with_bundle)

    return min_cost(0)
