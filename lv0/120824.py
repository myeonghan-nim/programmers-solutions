def solution(num_list):
    # 2로 나눈 나머지가 0인 짝수 개수를 먼저 세면, 홀수 개수는 전체 개수에서 짝수 개수를 뺀 값이다
    even = sum(n % 2 == 0 for n in num_list)
    return [even, len(num_list) - even]
