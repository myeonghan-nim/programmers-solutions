def solution(n, numlist):
    # n으로 나눈 나머지가 0인 수(= n의 배수)만 골라 새 리스트를 만든다
    return [number for number in numlist if number % n == 0]
