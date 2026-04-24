def solution(gems):
    target = len(set(gems))
    counts = {}
    start = 0
    best_start, best_end = 0, len(gems) - 1

    for end, gem in enumerate(gems):
        counts[gem] = counts.get(gem, 0) + 1

        while len(counts) == target:
            if end - start < best_end - best_start:
                best_start, best_end = start, end

            left = gems[start]
            counts[left] -= 1
            if counts[left] == 0:
                del counts[left]
            start += 1

    return [best_start + 1, best_end + 1]
