def solution(number):
    # 문제에 나온 성질 그대로, 각 자리 숫자를 모두 더한 값을 9로 나눈 나머지를 구한다
    return sum(int(d) for d in number) % 9
