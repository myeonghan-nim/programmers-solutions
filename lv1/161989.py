def solution(n, m, section):
    # 왼쪽부터 보면서 아직 칠하지 않은 구역을 만나면 그 구역을 왼쪽 끝으로 롤러를 한 번 칠하고, 덮인 범위는 건너뛴다
    # 시간 복잡도: O(S) (S: section의 길이)
    count, painted_until = 0, 0
    for s in section:
        if s > painted_until:
            count += 1
            painted_until = s + m - 1
    return count
