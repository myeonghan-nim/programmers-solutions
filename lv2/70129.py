def solution(s):
    cnt = zeros = 0
    while s != "1":
        partial_zeros = s.count("0")
        zeros += partial_zeros
        s = bin(len(s) - partial_zeros)[2:]
        cnt += 1
    return [cnt, zeros]
