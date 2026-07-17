def solution(distance, rocks, n):
    points = sorted(rocks)
    points.append(distance)

    left = 1
    right = distance

    answer = 0
    while left <= right:
        mid = (left + right) // 2

        previous = 0
        removed = 0

        for point in points:
            gap = point - previous

            if gap < mid:
                removed += 1
            else:
                previous = point

            if removed > n:
                break

        if removed <= n:
            answer = mid
            left = mid + 1
        else:
            right = mid - 1

    return answer
