def solution(m, n):
    # 가위질 한 번에 종이 조각이 정확히 하나 늘어나므로, 1조각에서 m*n조각이 되려면 m*n - 1번 잘라야 한다
    return m * n - 1
