def solution(str1, str2):
    # in 연산자로 str1이 str2 안에 들어 있는지 확인하고 결과(True/False)를 int로 바꿔 1 또는 0을 만든다
    return int(str1 in str2)
