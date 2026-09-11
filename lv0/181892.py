def solution(num_list, n):
    # 리스트 인덱스는 0부터 시작하므로 n번째 원소는 인덱스 n-1이고, 거기서부터 끝까지 잘라낸다
    return num_list[n - 1:]
