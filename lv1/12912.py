def solution(a, b):
    # 등차수열의 합 공식: (첫 수 + 끝 수) × 개수 ÷ 2 로 한 번에 계산한다
    # 시간 복잡도: O(1)
    start, end = min(a, b), max(a, b)
    return (start + end) * (end - start + 1) // 2
