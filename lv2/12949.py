def solution(arr1, arr2):
    # 곱한 행렬의 (i, j) 원소 = arr1의 i번째 행과 arr2의 j번째 열을 자리끼리 곱해 더한 값. zip(*arr2)로 arr2의 행과 열을 뒤집어 두면 열을 행처럼 쉽게 꺼내 쓸 수 있다.
    # 시간 복잡도: O(n^3)
    answer = [[]]
    transposed_arr2 = list(zip(*arr2))
    for row in arr1:
        for col in transposed_arr2:
            answer[-1].append(sum(a * b for a, b in zip(row, col)))
        answer.append([])
    return answer[:-1]
