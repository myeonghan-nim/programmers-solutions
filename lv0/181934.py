def solution(ineq, eq, n, m):
    # eq가 "="이고 두 수가 같으면 조건이 참이고, 그 외에는 부등호 방향(ineq)대로 n과 m을 비교한다. 참이면 1, 거짓이면 0
    if eq == "=" and n == m:
        return 1
    return int(n > m if ineq == ">" else n < m)
