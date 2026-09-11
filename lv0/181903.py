def solution(q, r, code):
    # q로 나눈 나머지가 r인 인덱스는 r부터 q 간격으로 나오므로 슬라이스 code[r::q]와 같다
    return code[r::q]
