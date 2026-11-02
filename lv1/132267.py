def solution(a, b, n):
    # 교환 한 번마다 빈 병이 a - b개 줄고 b병을 받으므로, 빈 병이 a개 미만이 될 때까지의 교환 횟수 (n - a) // (a - b) + 1 에 b를 곱하면 된다
    # 시간 복잡도: O(1)
    return max(0, (n - a) // (a - b) + 1) * b
