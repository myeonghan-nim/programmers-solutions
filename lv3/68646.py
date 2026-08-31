def solution(a):
    # "작은 쪽 터트리기"는 1번뿐이므로, 어떤 풍선이 끝까지 남으려면 자기보다 작은 풍선이 왼쪽에만 없거나 오른쪽에만 없어야 한다. 즉 왼쪽에서 훑을 때 새 최솟값이 되거나, 오른쪽에서 훑을 때 새 최솟값이 되면 생존 가능.
    # 시간 복잡도: O(n)
    answer = 0

    min_value = float('inf')
    for x in a:
        if x < min_value:  # 왼쪽의 모든 풍선보다 작음
            answer += 1
            min_value = x

    min_value = float('inf')
    for x in reversed(a):
        if x < min_value:  # 오른쪽의 모든 풍선보다 작음
            answer += 1
            min_value = x

    return answer - 1  # 전체 최솟값 풍선은 양쪽에서 두 번 세어지므로 1을 뺀다
