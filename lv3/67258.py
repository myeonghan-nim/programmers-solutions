def solution(gems):
    # 구간의 양 끝을 오른쪽으로만 움직이는 두 포인터 방식. 오른쪽 끝(end)을 늘려 보석을 담다가, 모든 종류가 모이면 왼쪽 끝(start)을 최대한 줄이며 가장 짧은 구간을 갱신한다.
    # 시간 복잡도: O(n)
    target = len(set(gems))
    counts = {}  # 현재 구간 안 보석별 개수
    start = 0
    best_start, best_end = 0, len(gems) - 1

    for end, gem in enumerate(gems):
        counts[gem] = counts.get(gem, 0) + 1

        while len(counts) == target:  # 모든 종류가 들어 있는 동안 왼쪽을 줄여 본다
            if end - start < best_end - best_start:
                best_start, best_end = start, end

            left = gems[start]
            counts[left] -= 1
            if counts[left] == 0:
                del counts[left]
            start += 1

    return [best_start + 1, best_end + 1]  # 진열대 번호는 1부터 시작
