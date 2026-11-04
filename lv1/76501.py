def solution(absolutes, signs):
    # 부호가 True면 그대로, False면 음수로 바꿔 더한다
    # 시간 복잡도: O(n)
    return sum(n if positive else -n for n, positive in zip(absolutes, signs))
