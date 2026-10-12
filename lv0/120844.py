def solution(numbers, direction):
    # 오른쪽 회전은 마지막 원소를 맨 앞으로, 왼쪽 회전은 첫 원소를 맨 뒤로 옮긴 것과 같다
    if direction == "right":
        return numbers[-1:] + numbers[:-1]
    return numbers[1:] + numbers[:1]
