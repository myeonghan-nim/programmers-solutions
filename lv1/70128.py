def solution(a, b):
    # 같은 위치의 원소끼리 zip으로 짝지어 곱한 값을 모두 더한다
    # 시간 복잡도: O(n)
    return sum(x * y for x, y in zip(a, b))
