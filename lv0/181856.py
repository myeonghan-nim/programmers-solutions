def solution(arr1, arr2):
    # (길이, 원소의 합) 순서로 비교하면 되므로 튜플로 만들어 대소를 가린다
    a, b = (len(arr1), sum(arr1)), (len(arr2), sum(arr2))
    return (a > b) - (a < b)
