def solution(arr):
    # zip(*arr)은 행과 열을 맞바꾼(전치) 배열을 만들므로, 원본과 전치가 같으면 모든 칸에서 arr[i][j] = arr[j][i]가 성립한다
    return int(arr == [list(row) for row in zip(*arr)])
