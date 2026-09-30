def solution(arr, delete_list):
    # delete_list에 없는 원소만 원래 순서대로 골라 새 리스트를 만든다
    return [x for x in arr if x not in delete_list]
