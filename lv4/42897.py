def solution(money):
    # 집이 원형으로 이어져 있어 첫 집과 마지막 집은 함께 털 수 없다. 그래서 (마지막 집 제외)와 (첫 집 제외) 두 경우를 일자 배열 DP로 풀어 큰 값을 고른다.
    # 시간 복잡도: O(n)
    def rob(arr):
        prev = curr = 0
        for m in arr:
            # 이번 집을 털면 prev + m, 안 털면 curr 그대로
            prev, curr = curr, max(curr, prev + m)
        return curr

    return max(rob(money[:-1]), rob(money[1:]))
