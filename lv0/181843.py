def solution(my_string, target):
    # in 연산자로 target이 my_string 안에 들어 있는지 확인하고 결과(True/False)를 int로 바꿔 1 또는 0을 만든다
    return int(target in my_string)
