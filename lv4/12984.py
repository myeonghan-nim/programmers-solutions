def solution(land, P, Q):
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
        add = P * (h * below_cells - below_blocks)
        remove = Q * (above_blocks - h * above_cells)
        cost = min(cost, add + remove)
        below_cells += c
        below_blocks += h * c

    return cost
