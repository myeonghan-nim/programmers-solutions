def solution(my_string, index_list):
    # index_list에 적힌 인덱스 순서대로 해당 위치의 글자를 뽑아 이어 붙인다
    return "".join(my_string[i] for i in index_list)
