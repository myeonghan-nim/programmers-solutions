def solution(arr, k):
    # k가 홀수면(2로 나눈 나머지가 1) 모든 원소에 k를 곱하고, 짝수면 모든 원소에 k를 더한다
    return [x * k if k % 2 else x + k for x in arr]
