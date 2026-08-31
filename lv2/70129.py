def solution(s):
    # 매 변환마다 0의 개수를 세어 누적하고, 남은 1의 개수(길이 - 0의 개수)를 2진수 문자열로 바꾸는 과정을 s가 "1"이 될 때까지 반복한다.
    cnt = zeros = 0
    while s != "1":
        partial_zeros = s.count("0")
        zeros += partial_zeros
        s = bin(len(s) - partial_zeros)[2:]  # bin() 결과의 앞머리 "0b"는 잘라낸다
        cnt += 1
    return [cnt, zeros]
