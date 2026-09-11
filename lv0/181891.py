def solution(num_list, n):
    # 리스트를 n번째까지(앞부분)와 그 이후(뒷부분)로 나눈 뒤, 뒷부분과 앞부분 순서로 이어 붙인다
    return num_list[n:] + num_list[:n]
