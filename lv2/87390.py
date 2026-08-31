def solution(n, left, right):
    # n이 천만까지라 배열을 실제로 만들면 너무 크므로, 각 위치의 값을 공식으로 바로 구한다. 1차원 위치 i는 2차원의 (i // n)행 (i % n)열이고, 그 칸의 값은 max(행, 열) + 1 이다.
    # 시간 복잡도: O(right - left)
    answer = []
    for i in range(left, right + 1):
        answer.append(max(i // n, i % n) + 1)
    return answer
