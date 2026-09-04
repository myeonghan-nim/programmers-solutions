def solution(my_string):
    # 각 인덱스에서 시작해 끝까지 자른 접미사를 전부 만든 뒤 사전순으로 정렬한다
    return sorted(my_string[i:] for i in range(len(my_string)))
