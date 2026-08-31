def solution(cookie):
    # 두 아들 몫의 경계(i번과 i+1번 사이)를 고정해 두고, 합이 작은 쪽을 바깥으로 한 칸씩 넓히며 양쪽 합이 같아지는 순간을 찾는 투 포인터.
    # 시간 복잡도: O(n^2)
    n = len(cookie)
    answer = 0

    for i in range(n - 1):
        left, right = cookie[i], cookie[i + 1]  # 경계 양옆 한 칸씩에서 시작
        li, ri = i - 1, i + 2  # 다음에 넓힐 위치
        while True:
            if left == right and left > answer:
                answer = left
            if left <= right and li >= 0:  # 왼쪽 합이 작거나 같으면 왼쪽으로 확장
                left += cookie[li]
                li -= 1
            elif right <= left and ri < n:
                right += cookie[ri]
                ri += 1
            else:  # 더 넓힐 곳이 없으면 이 경계는 끝
                break

    return answer
