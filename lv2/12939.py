def solution(s):
    min_num, max_num = float('inf'), float('-inf')
    for num in s.split():
        n = int(num)
        min_num = min(min_num, n)
        max_num = max(max_num, n)
    return f"{min_num} {max_num}"
