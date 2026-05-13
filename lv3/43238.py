def solution(n, times):
    left, right = 1, min(times) * n
    answer = right

    while left <= right:
        mid = (left + right) // 2
        people = sum(mid // time for time in times)

        if people >= n:
            answer = mid
            right = mid - 1
        else:
            left = mid + 1

    return answer
