def solution(n, stations, w):
    # 왼쪽부터 훑으며 전파가 안 닿는 빈 구간의 길이를 구하고, 기지국 하나가 덮는 폭(2w+1)으로 나눠 올림한 만큼 설치한다.
    # 시간 복잡도: O(len(stations))
    answer = 0

    now = 1  # 아직 전파가 닿지 않은 가장 왼쪽 아파트 번호
    coverage = 2 * w + 1
    for station in stations:
        left = station - w  # 이 기지국이 덮는 왼쪽 끝
        if now < left:
            gap = left - now  # 빈 구간 길이
            q, r = divmod(gap, coverage)
            answer += q + (1 if r else 0)  # 올림 나눗셈
        now = station + w + 1

    # 마지막 기지국 오른쪽에 남은 빈 구간 처리
    if now <= n:
        gap = n - now + 1
        q, r = divmod(gap, coverage)
        answer += q + (1 if r else 0)

    return answer
