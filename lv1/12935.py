def solution(arr):
    # 최솟값을 한 번만 구해 두고 그 값이 아닌 원소만 남기며, 원소가 하나뿐이라 결과가 비면 [-1]을 돌려준다 (arr의 원소는 서로 달라 최솟값은 하나뿐이다)
    # 시간 복잡도: O(len(arr))
    smallest = min(arr)
    return [num for num in arr if num != smallest] or [-1]
