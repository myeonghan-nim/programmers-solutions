def solution(numbers, n):
    # 앞에서부터 차례로 더하다가 합이 n보다 커지는 순간 그 합을 돌려준다
    total = 0
    for x in numbers:
        total += x
        if total > n:
            return total
