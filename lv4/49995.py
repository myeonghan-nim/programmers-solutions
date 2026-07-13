def solution(cookie):
    n = len(cookie)
    answer = 0

    for i in range(n - 1):
        left, right = cookie[i], cookie[i + 1]
        li, ri = i - 1, i + 2
        while True:
            if left == right and left > answer:
                answer = left
            if left <= right and li >= 0:
                left += cookie[li]
                li -= 1
            elif right <= left and ri < n:
                right += cookie[ri]
                ri += 1
            else:
                break

    return answer
