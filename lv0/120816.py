def solution(slice, n):
    # n명이 slice조각짜리 피자를 한 조각 이상 먹으려면 n을 slice로 나눠 올림한 판 수가 필요하다((n + slice - 1) // slice는 올림 나눗셈)
    return (n + slice - 1) // slice
