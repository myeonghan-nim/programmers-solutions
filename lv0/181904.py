def solution(my_string, m, c):
    # 한 줄에 m글자씩 적으면 c번째 열의 글자는 인덱스 c-1부터 m 간격으로 나온다
    return my_string[c - 1::m]
