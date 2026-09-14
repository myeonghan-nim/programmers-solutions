def solution(num_list):
    # 짝수든 홀수든 한 번의 연산 결과는 2로 나눈 몫과 같으므로, 각 수가 1이 될 때까지 몫으로 바꾼 횟수를 전부 더한다
    count = 0
    for x in num_list:
        while x > 1:
            x //= 2
            count += 1
    return count
