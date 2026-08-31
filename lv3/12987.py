def solution(a, b):
    # 둘 다 오름차순 정렬 후 작은 수끼리 맞대 본다. B가 이기면 승점을 얻고 둘 다 다음으로, 못 이기면 그 B는 버린다(작은 B는 아껴도 쓸 데가 없다).
    # 시간 복잡도: O(n log n)
    a.sort()
    b.sort()

    n = len(a)
    i, j = 0, 0
    count = 0
    while i < n and j < n:
        if a[i] < b[j]:  # 이길 수 있으면 승점 1
            count += 1
            i += 1
            j += 1
        else:  # 못 이기는 B는 버리고 더 큰 B로 시도
            j += 1
    return count
