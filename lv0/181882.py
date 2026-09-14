def solution(arr):
    # 50 이상 짝수는 반으로 나누고, 50 미만 홀수는 2배로 만들고, 나머지는 그대로 둔다
    return [a // 2 if a >= 50 and a % 2 == 0 else a * 2 if a < 50 and a % 2 else a for a in arr]
