def solution(bin1, bin2):
    # int(x, 2)로 이진수 문자열을 정수로 바꿔 더한 뒤, bin()으로 다시 이진수 문자열로 만들고 앞의 "0b"를 떼어 낸다
    return bin(int(bin1, 2) + int(bin2, 2))[2:]
