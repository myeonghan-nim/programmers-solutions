def solution(s):
    # 공백으로 나눈 숫자들을 하나씩 보면서 가장 작은 값과 가장 큰 값을 갱신한다.
    # 시간 복잡도: O(n)
    min_num, max_num = float("inf"), float("-inf")
    for num in s.split():
        n = int(num)
        min_num = min(min_num, n)
        max_num = max(max_num, n)
    return f"{min_num} {max_num}"
