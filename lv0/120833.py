def solution(numbers, num1, num2):
    # 슬라이스의 끝 인덱스는 포함되지 않으므로 num2 + 1까지 잘라야 num2번째 원소까지 담긴다
    return numbers[num1:num2 + 1]
