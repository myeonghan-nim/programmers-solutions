def solution(land, p, q):
    # 목표 높이별 비용은 꺾은선(볼록) 모양이라 최솟값은 실제 존재하는 높이에서 나온다. 높이를 정렬해 낮은 쪽 누적 개수/블록 수를 유지하면 각 후보의 비용을 O(1)에 계산할 수 있다.
    # 시간 복잡도: O(N^2 + H log H) (H는 서로 다른 높이 개수)
    height = {}
    for row in land:
        for h in row:
            height[h] = height.get(h, 0) + 1

    heights = sorted(height.keys())
    counts = [height[h] for h in heights]

    total_cells = sum(counts)
    total_blocks = sum(h * c for h, c in zip(heights, counts))

    below_cells = 0
    below_blocks = 0
    cost = float('inf')
    for h, c in zip(heights, counts):
        above_cells = total_cells - below_cells - c
        above_blocks = total_blocks - below_blocks - h * c
        add = p * (h * below_cells - below_blocks)  # h보다 낮은 칸들을 h까지 채우는 비용
        remove = q * (above_blocks - h * above_cells)  # h보다 높은 칸들을 h까지 깎는 비용
        cost = min(cost, add + remove)
        below_cells += c
        below_blocks += h * c

    return cost
