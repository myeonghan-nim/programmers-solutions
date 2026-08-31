from collections import Counter


def solution(k, tangerine):
    # 크기별로 귤이 몇 개씩 있는지 센 뒤, 개수가 많은 크기부터 상자에 담으면 가장 적은 종류로 k개를 채울 수 있다. k개가 채워지는 순간의 종류 수가 답이다.
    # 시간 복잡도: O(n log n) (정렬)
    for cnt, v in enumerate(sorted(Counter(tangerine).values(), reverse=True), 1):
        k -= v
        if k <= 0:
            return cnt
