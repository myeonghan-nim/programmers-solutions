def solution(a, b):
    # 홀수의 개수에 따라 점수가 갈린다. 둘 다 홀수면 제곱의 합, 하나만 홀수면 2*(a+b), 둘 다 짝수면 차이의 절댓값
    if a % 2 and b % 2:
        return a * a + b * b
    if a % 2 or b % 2:
        return 2 * (a + b)
    return abs(a - b)
