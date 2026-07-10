def solution(food_times, k):
    if sum(food_times) <= k:
        return -1

    foods = sorted((t, i + 1) for i, t in enumerate(food_times))
    n = len(foods)
    prev = 0

    for idx, (t, _) in enumerate(foods):
        m = n - idx
        chunk = (t - prev) * m
        if k < chunk:
            rest = sorted(foods[idx:], key=lambda x: x[1])
            return rest[k % m][1]
        k -= chunk
        prev = t
