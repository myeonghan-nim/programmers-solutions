def solution(n, s):
    # 합이 정해져 있을 때 곱이 최대가 되려면 원소들이 최대한 균등해야 한다. 몫 q를 n개에 깔고, 나머지 r개에만 1씩 더해 오름차순으로 만든다.
    # 시간 복잡도: O(n)
    if n > s:
        return [-1]  # 자연수 n개의 최소 합은 n이므로 만들 수 없음
    q, r = divmod(s, n)
    return [q] * (n - r) + [q + 1] * r
