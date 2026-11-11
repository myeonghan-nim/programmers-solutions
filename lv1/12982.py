def solution(d, budget):
    # 신청 금액이 적은 부서부터 지원해야 같은 예산으로 가장 많은 부서를 지원할 수 있으므로, 오름차순으로 정렬해 예산이 모자라기 직전까지 센다
    # 시간 복잡도: O(n log n), n은 d의 길이
    for count, amount in enumerate(sorted(d)):
        budget -= amount
        if budget < 0:
            return count  # 이번 부서는 지원하지 못했으므로 그 앞까지의 부서 수
    return len(d)
