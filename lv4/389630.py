def solution(visible, hidden, k):
    # 칸에 적힌 수가 모두 양수라 말은 최대한 많은 칸을 지나는 것이 이득이다.
    # 행 뒤집기 조합(2^n가지)을 전부 시도하고, 행이 정해지면 각 열은 뒤집을지 말지를 따로따로 고르면 된다.
    # 단, n과 m이 모두 짝수면 모든 칸을 지나는 경로가 없어서 (행+열) 번호 합이 홀수인 칸 하나를 빼야 한다.
    # 행을 짝수/홀수 번째 두 묶음으로 나눠 묶음별 합을 미리 표로 만들어 조합마다 열당 O(1)에 계산한다.
    # 시간 복잡도: O(2^n * m)
    n, m = len(visible), len(visible[0])
    if n > m:  # 행 수가 적은 쪽을 n으로 두어 시도할 조합 수를 줄임
        visible = [list(r) for r in zip(*visible)]
        hidden = [list(r) for r in zip(*hidden)]
        n, m = m, n

    both_even = n % 2 == 0 and m % 2 == 0
    even_rows = range(0, n, 2)
    odd_rows = range(1, n, 2)
    even_mask_count, odd_mask_count = 1 << len(even_rows), 1 << len(odd_rows)

    even_sum_tabs, odd_sum_tabs, flip_bases = [], [], []
    keep_min_tabs, flip_min_tabs = [], []
    for j in range(m):
        even_vis = [visible[i][j] for i in even_rows]
        even_hid = [hidden[i][j] for i in even_rows]
        odd_vis = [visible[i][j] for i in odd_rows]
        odd_hid = [hidden[i][j] for i in odd_rows]
        # even_sums[e]: 짝수 번째 행들만 골라 뒤집었을 때(e의 비트가 1인 행) 이 열의 합, odd_sums[o]: 홀수 번째 행 버전
        even_sums = [0] * even_mask_count
        even_sums[0] = sum(even_vis)
        for e in range(1, even_mask_count):
            low = e & -e
            t = low.bit_length() - 1
            even_sums[e] = even_sums[e ^ low] + even_hid[t] - even_vis[t]  # 비트 하나를 켠 경우 = 그 행만 값이 바뀜
        odd_sums = [0] * odd_mask_count
        odd_sums[0] = sum(odd_vis)
        for o in range(1, odd_mask_count):
            low = o & -o
            t = low.bit_length() - 1
            odd_sums[o] = odd_sums[o ^ low] + odd_hid[t] - odd_vis[t]
        even_sum_tabs.append(even_sums)
        odd_sum_tabs.append(odd_sums)
        flip_bases.append(sum(even_vis) + sum(even_hid) + sum(odd_vis) + sum(odd_hid) - k)  # 뒤집은 열의 점수 = 이 밑값(전체합 - 비용 k) - 현재 합

        if both_even:
            # 빼도 되는 칸은 (행+열) 합이 홀수인 칸: 짝수 열이면 홀수 행들, 홀수 열이면 짝수 행들
            vis, hid = (odd_vis, odd_hid) if j % 2 == 0 else (even_vis, even_hid)
            w = len(vis)
            keep_mins = [min(hid[t] if (s >> t) & 1 else vis[t] for t in range(w)) for s in range(1 << w)]
            full = (1 << w) - 1
            flip_mins = [keep_mins[s ^ full] for s in range(1 << w)]  # 열을 뒤집으면 보이는 면이 반대가 됨
            keep_min_tabs.append(keep_mins)
            flip_min_tabs.append(flip_mins)

    # 마스크 번호 = e * odd_mask_count + o, scores[마스크] = 열마다 유리한 쪽을 고른 점수 합
    scores = [0] * (even_mask_count * odd_mask_count)
    if not both_even:
        for j in range(m):
            even_sums, odd_sums, flip_base = even_sum_tabs[j], odd_sum_tabs[j], flip_bases[j]
            idx = 0
            for e in range(even_mask_count):
                even_sum = even_sums[e]
                for odd_sum in odd_sums:
                    cur = even_sum + odd_sum
                    alt = flip_base - cur
                    scores[idx] += cur if cur >= alt else alt
                    idx += 1
        best = None
        idx = 0
        for e in range(even_mask_count):
            even_cost = k * bin(e).count("1")  # 행 뒤집기 비용
            for o in range(odd_mask_count):
                value = scores[idx] - even_cost - k * bin(o).count("1")
                if best is None or value > best:
                    best = value
                idx += 1
        return best

    # drop_deltas[마스크] = 칸 하나를 뺄 때 (그 열의 선택을 바꾸는 경우까지 포함해) 손해를 가장 줄인 보정값
    drop_deltas = [-(1 << 60)] * (even_mask_count * odd_mask_count)
    for j in range(m):
        even_sums, odd_sums, flip_base = even_sum_tabs[j], odd_sum_tabs[j], flip_bases[j]
        keep_mins, flip_mins = keep_min_tabs[j], flip_min_tabs[j]
        if j % 2:  # 홀수 열: 뺄 칸 후보가 짝수 행이라 e에만 의존 -> e 루프에서 미리 꺼냄
            idx = 0
            for e in range(even_mask_count):
                even_sum = even_sums[e]
                keep_min = keep_mins[e]
                flip_min = flip_mins[e]
                neg_keep_min = -keep_min
                neg_flip_min = -flip_min
                for odd_sum in odd_sums:
                    cur = even_sum + odd_sum
                    alt = flip_base - cur
                    if cur >= alt:
                        scores[idx] += cur
                        delta = alt - cur - flip_min  # 열 선택을 뒤집고 그쪽에서 가장 싼 칸을 빼는 경우
                        if neg_keep_min > delta:
                            delta = neg_keep_min
                    else:
                        scores[idx] += alt
                        delta = cur - alt - keep_min
                        if neg_flip_min > delta:
                            delta = neg_flip_min
                    if delta > drop_deltas[idx]:
                        drop_deltas[idx] = delta
                    idx += 1
        else:  # 짝수 열: 뺄 칸 후보가 홀수 행이라 o에만 의존 -> o를 바깥 루프로
            for o in range(odd_mask_count):
                odd_sum = odd_sums[o]
                keep_min = keep_mins[o]
                flip_min = flip_mins[o]
                neg_keep_min = -keep_min
                neg_flip_min = -flip_min
                idx = o
                for even_sum in even_sums:
                    cur = even_sum + odd_sum
                    alt = flip_base - cur
                    if cur >= alt:
                        scores[idx] += cur
                        delta = alt - cur - flip_min
                        if neg_keep_min > delta:
                            delta = neg_keep_min
                    else:
                        scores[idx] += alt
                        delta = cur - alt - keep_min
                        if neg_flip_min > delta:
                            delta = neg_flip_min
                    if delta > drop_deltas[idx]:
                        drop_deltas[idx] = delta
                    idx += odd_mask_count

    best = None
    idx = 0
    for e in range(even_mask_count):
        even_cost = k * bin(e).count("1")
        for o in range(odd_mask_count):
            value = scores[idx] + drop_deltas[idx] - even_cost - k * bin(o).count("1")
            if best is None or value > best:
                best = value
            idx += 1
    return best
