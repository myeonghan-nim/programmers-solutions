def solution(num_list, n):
    # 시작 인덱스를 0, n, 2n, ...으로 옮겨 가며 n개씩 슬라이스해 2차원 리스트를 만든다
    return [num_list[i:i + n] for i in range(0, len(num_list), n)]
