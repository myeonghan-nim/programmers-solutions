def solution(n):
    count = bin(n)[2:].count("1")
    num = n + 1
    while True:
        if bin(num)[2:].count("1") == count:
            return num
        num += 1
