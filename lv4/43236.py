def solution(distance, rocks, n):
    # "바위 사이 최소 거리를 mid 이상으로 만들 수 있는가?"를 이분 탐색한다. 앞에서부터 훑으며 간격이 mid보다 좁으면 그 바위를 제거하는 식으로 세어, 제거 수가 n 이하면 mid를 더 키워 본다.
    # 시간 복잡도: O(N log D) (N은 바위 수, D는 distance)
    points = sorted(rocks)
    points.append(distance)  # 도착지점도 간격 계산에 포함

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
                removed += 1  # 간격이 좁으면 이 바위를 제거한다고 가정
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
