def solution(wallet, bill):
    # 지폐를 90도 돌려 넣을 수 있으므로 지갑과 지폐를 각각 (짧은 변, 긴 변)으로 정렬해 비교하고, 들어가지 않는 동안 긴 변을 반으로 접는다
    # 시간 복잡도: O(log(max(bill))), 접을 때마다 긴 변이 절반이 된다
    short_side, long_side = sorted(wallet)
    small, big = sorted(bill)
    answer = 0
    while small > short_side or big > long_side:
        small, big = sorted((small, big // 2))  # 긴 변을 접은 뒤 다시 짧은 변·긴 변 순서로 맞춘다
        answer += 1
    return answer
