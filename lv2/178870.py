def solution(sequence, k):
    # 원소가 모두 양수라 구간을 오른쪽으로 늘리면 합이 커지고 왼쪽을 줄이면 작아진다. 오른쪽 끝을 한 칸씩 늘리면서 합이 k를 넘는 동안 왼쪽 끝을 당기는 투 포인터로 합이 k인 구간을 모두 훑는다
    # 시간 복잡도: O(n), n은 수열의 길이
    answer = [0, len(sequence)]  # 어떤 실제 구간보다도 긴 초깃값이라 처음 찾은 구간으로 반드시 바뀐다
    window_sum = 0
    left = 0
    for right, value in enumerate(sequence):
        window_sum += value
        while window_sum > k:
            window_sum -= sequence[left]
            left += 1
        # 더 짧을 때만 바꾸므로 길이가 같으면 먼저 찾은 앞쪽 구간이 남는다
        if window_sum == k and right - left < answer[1] - answer[0]:
            answer = [left, right]
    return answer
