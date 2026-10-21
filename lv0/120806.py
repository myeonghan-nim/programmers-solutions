def solution(num1, num2):
    # 나누기 전에 1000을 먼저 곱하고 정수 나눗셈(//)을 하면 소수 오차 없이 정수 부분만 얻는다
    return num1 * 1000 // num2
