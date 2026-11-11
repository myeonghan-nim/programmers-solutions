def solution(num):
    # 작업을 최대 500번까지 그대로 따라 하며 1이 되는 순간의 횟수를 돌려주고, 500번을 다 해도 1이 아니면 -1을 돌려준다 (횟수를 작업 전에 확인하므로 1이 주어지면 0이다)
    # 시간 복잡도: O(1), 반복이 최대 500번으로 고정
    for count in range(501):
        if num == 1:
            return count
        num = num * 3 + 1 if num % 2 else num // 2
    return -1
