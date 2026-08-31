def solution(n, times):
    # "시간 T 안에 n명을 심사할 수 있는가?"는 T가 클수록 참이 되므로, 가능한 최소 T를 이분 탐색(범위를 절반씩 좁히는 탐색)으로 찾는다. T 동안 심사 가능한 인원 = 심사관마다 T // (심사 시간) 의 합.
    # 시간 복잡도: O(len(times) * log(min(times) * n))
    left, right = 1, min(times) * n  # 가장 빠른 심사관 혼자 다 봐도 min * n이면 충분
    answer = right

    while left <= right:
        mid = (left + right) // 2
        people = sum(mid // time for time in times)

        if people >= n:  # mid 시간이면 충분: 답을 기록하고 더 줄여 본다
            answer = mid
            right = mid - 1
        else:
            left = mid + 1

    return answer
