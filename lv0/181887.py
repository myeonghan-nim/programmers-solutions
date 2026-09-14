def solution(num_list):
    # 홀수 번째는 인덱스 0, 2, ...이고 짝수 번째는 인덱스 1, 3, ...이므로 두 슬라이스의 합 중 큰 값을 고른다
    return max(sum(num_list[::2]), sum(num_list[1::2]))
