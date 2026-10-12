def solution(numbers):
    # 원소가 모두 0 이상이므로 가장 큰 두 수를 곱한 값이 최댓값이다. 정렬 후 마지막 두 개를 곱한다
    numbers.sort()
    return numbers[-1] * numbers[-2]
