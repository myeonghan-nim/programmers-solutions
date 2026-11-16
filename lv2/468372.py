def solution(dist_limit, split_limit):
    # 리프 수 = 1 + (분배 노드 수) + (3갈래 분배 노드 수)이므로 3갈래 노드를 최대한 많이 놓아야 한다. 층 순서는 "2갈래 a층 → 3갈래 b층"만 보면 된다 (노드가 적은 위쪽에 2갈래를 둬야 손해가 작다)
    # 3갈래 첫 층의 노드 수 width를 정하면 위쪽 2갈래 층은 그 조상만 최소로 두고, 남은 분배 노드를 3갈래 층에 위에서부터 채운다. width가 작으면 3갈래 자리가 모자라고 크면 조상 비용이 늘어나므로 경계를 이분 탐색한다
    # 시간 복잡도: O(log⁴(split_limit))
    def count_ancestors(two_depth, width):
        # width개의 노드를 받치려면 한 층 올라갈 때마다 절반(올림)씩 필요하다
        return sum((width + (1 << depth) - 1) >> depth for depth in range(1, two_depth + 1))

    answer = 1
    for two_depth in range(split_limit.bit_length()):
        full_two_way = (1 << two_depth) - 1  # 2갈래 층을 꽉 채웠을 때의 노드 수: 1 + 2 + 4 + ...
        three_product = 1
        while (three_product << two_depth) <= split_limit:
            three_capacity = (three_product - 1) // 2  # 3갈래 첫 층 노드 하나가 자신을 포함해 아래로 거느릴 수 있는 3갈래 노드 수: 1 + 3 + 9 + ...
            # 분배 노드를 남김없이 쓸 수 있는 가장 작은 width를 찾는다
            low, high = 1, 1 << two_depth
            while low < high:
                width = (low + high) // 2
                if count_ancestors(two_depth, width) + width * three_capacity >= dist_limit:
                    high = width
                else:
                    low = width + 1
            # 경계 바로 앞은 3갈래 자리가 모자라 노드가 남지만 조상 비용이 적어 더 나을 수 있으므로 둘 다 확인한다
            for width in (low - 1, low):
                ancestors = count_ancestors(two_depth, width)
                if width >= 1 and ancestors <= dist_limit:
                    three_way = min(dist_limit - ancestors, width * three_capacity)
                    spare_two_way = min(dist_limit - ancestors - three_way, full_two_way - ancestors)  # 3갈래 자리가 다 차면 남는 노드는 2갈래 빈자리에 둔다
                    answer = max(answer, 1 + ancestors + spare_two_way + 2 * three_way)
            three_product *= 3
    return answer
