def solution(arr):
    # 변환을 반복 적용하다가 배열이 직전과 똑같아지는 순간, 그 직전까지 적용한 횟수를 돌려준다
    x = 0
    while True:
        nxt = [a // 2 if a >= 50 and a % 2 == 0 else a * 2 + 1 if a < 50 and a % 2 else a for a in arr]
        if nxt == arr:
            return x
        arr = nxt
        x += 1
