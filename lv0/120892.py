def solution(cipher, code):
    # code번째 글자는 인덱스 code-1이므로, 거기서 시작해 code 간격으로 글자를 건너뛰며 뽑는 슬라이스를 쓴다
    return cipher[code - 1::code]
