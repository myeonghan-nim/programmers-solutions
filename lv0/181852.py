def solution(num_list):
    # 오름차순으로 정렬한 뒤 가장 작은 5개를 건너뛰고 나머지를 담는다
    return sorted(num_list)[5:]
