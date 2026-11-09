def solution(array, commands):
    # 문제의 i, j, k는 1부터 세므로 슬라이스는 [i-1:j], 정렬 뒤 인덱스는 k-1로 옮겨 그대로 계산한다
    # 시간 복잡도: O(m * n log n) (m은 명령 수, n은 배열 길이)
    return [sorted(array[i - 1:j])[k - 1] for i, j, k in commands]
