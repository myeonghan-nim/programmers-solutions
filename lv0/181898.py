def solution(arr, idx):
    # idx부터 오른쪽으로 차례로 살펴보다 처음 1을 만난 인덱스를 돌려주고, 없으면 -1을 돌려준다
    for i in range(idx, len(arr)):
        if arr[i] == 1:
            return i
    return -1
