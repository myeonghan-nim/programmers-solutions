def solution(arr):
    # 행 수와 열 수 중 큰 쪽을 목표 크기로 잡고, 각 행 끝에 모자란 만큼 0을 붙인 뒤 모자란 개수만큼 0으로만 된 행을 추가한다
    size = max(len(arr), len(arr[0]))
    return [row + [0] * (size - len(row)) for row in arr] + [[0] * size for _ in range(size - len(arr))]
