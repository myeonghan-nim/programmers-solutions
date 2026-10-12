def solution(numbers):
    # 음수가 있으므로 최댓값은 가장 큰 두 수의 곱 아니면 가장 작은 두 음수의 곱이다. 정렬 후 둘을 비교한다
    numbers.sort()
    return max(numbers[-1] * numbers[-2], numbers[0] * numbers[1])
