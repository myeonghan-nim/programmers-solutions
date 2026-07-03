def solution(money):
    def rob(arr):
        prev = curr = 0
        for m in arr:
            prev, curr = curr, max(curr, prev + m)
        return curr

    return max(rob(money[:-1]), rob(money[1:]))
