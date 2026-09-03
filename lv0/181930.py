def solution(a, b, c):
    # 서로 다른 숫자가 2종류 이하면 제곱의 합을, 1종류면 세제곱의 합까지 차례로 곱해 나간다
    score = a + b + c
    kinds = len({a, b, c})
    if kinds <= 2:
        score *= a ** 2 + b ** 2 + c ** 2
    if kinds == 1:
        score *= a ** 3 + b ** 3 + c ** 3
    return score
