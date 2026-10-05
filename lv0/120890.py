def solution(array, n):
    # n과의 거리(abs)가 가장 작은 수를 고르되, 거리가 같으면 값 자체가 작은 쪽이 뽑히도록 (거리, 값) 순서로 비교한다
    return min(array, key=lambda x: (abs(x - n), x))
