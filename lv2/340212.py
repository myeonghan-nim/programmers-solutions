def solution(diffs, times, limit):
    # 숙련도가 높을수록 전체 소요 시간은 줄기만 하므로, "제한 시간 안에 끝나는가"는 어느 숙련도부터 계속 참이다. 그 경계를 이분 탐색으로 찾는다
    # 시간 복잡도: O(n * log(max(diffs)))
    def total_time(level):
        # 첫 퍼즐은 난이도가 1로 고정이라 틀리지 않으므로 이전 퍼즐 시간이 0이어도 된다
        total = 0
        previous_time = 0
        for difficulty, current_time in zip(diffs, times):
            mistakes = max(difficulty - level, 0)
            total += (current_time + previous_time) * mistakes + current_time
            previous_time = current_time
        return total

    # 숙련도가 max(diffs)이면 한 번도 틀리지 않고, 그때는 반드시 제한 시간 안에 끝난다고 문제가 보장한다
    low, high = 1, max(diffs)
    while low < high:
        middle = (low + high) // 2
        if total_time(middle) <= limit:
            high = middle
        else:
            low = middle + 1
    return low
