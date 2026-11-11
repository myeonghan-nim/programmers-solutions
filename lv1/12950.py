def solution(arr1, arr2):
    # 두 행렬을 zip으로 행끼리 짝짓고, 각 행 안에서 다시 zip으로 같은 열의 값끼리 짝지어 더한다
    # 시간 복잡도: O(행 수 * 열 수)
    return [[a + b for a, b in zip(row1, row2)] for row1, row2 in zip(arr1, arr2)]
