def solution(food_times, k):
    # 시간이 적게 걸리는 음식부터 정렬해 두고, "남은 음식 전부를 같은 횟수씩 먹는" 구간을 통째로 건너뛰며 k를 줄인다. 한 구간을 다 못 채우는 순간, 남은 음식들을 번호 순으로 세워 k의 나머지 번째 음식이 답이 된다.
    # 시간 복잡도: O(N log N)
    if sum(food_times) <= k:
        return -1

    foods = sorted((t, i + 1) for i, t in enumerate(food_times))
    n = len(foods)
    prev = 0

    for idx, (t, _) in enumerate(foods):
        m = n - idx  # 아직 남아 있는 음식 수
        chunk = (t - prev) * m  # 남은 음식 전부를 (t - prev)바퀴 먹는 데 드는 시간
        if k < chunk:
            rest = sorted(foods[idx:], key=lambda x: x[1])  # 남은 음식을 번호 순으로
            return rest[k % m][1]  # 한 바퀴(m개) 안에서 k초 뒤에 먹을 음식
        k -= chunk
        prev = t
