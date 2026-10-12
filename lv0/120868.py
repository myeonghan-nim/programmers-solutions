def solution(sides):
    # 나머지 한 변 x는 |a-b| < x < a+b 를 만족해야 하므로, 가능한 정수 개수는 2 * min(a, b) - 1 로 바로 계산된다
    return 2 * min(sides) - 1
