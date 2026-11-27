def solution(picks, minerals):
    # 곡괭이 하나가 연속한 광물 5개 묶음 하나를 맡으므로, 캘 수 있는 만큼만 남겨 5개씩 묶고 다이아몬드·철이 많은 묶음부터 좋은 곡괭이를 배정한다. 묶음 순서는 고정이어도 곡괭이를 꺼내는 순서는 자유라서 어느 묶음에 어느 곡괭이든 맞출 수 있다
    # 시간 복잡도: O(광물 수)
    fatigue_by_pick = (
        {"diamond": 1, "iron": 1, "stone": 1},
        {"diamond": 5, "iron": 1, "stone": 1},
        {"diamond": 25, "iron": 5, "stone": 1},
    )
    minerals = minerals[: 5 * sum(picks)]  # 곡괭이가 모자라 끝내 캐지 못하는 광물은 묶음 후보에서 뺀다
    groups = [minerals[index : index + 5] for index in range(0, len(minerals), 5)]
    groups.sort(key=lambda group: (group.count("diamond"), group.count("iron")), reverse=True)
    pick_order = [pick for pick, count in enumerate(picks) for _ in range(count)]  # 다이아몬드, 철, 돌 순서로 좋은 곡괭이가 앞에 온다
    return sum(fatigue_by_pick[pick][mineral] for pick, group in zip(pick_order, groups) for mineral in group)
