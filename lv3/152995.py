def solution(scores):
    # 근무 태도 점수 내림차순(같으면 동료 평가 오름차순)으로 훑으면, 지금까지 나온 동료 평가 최댓값보다 낮은 사람은 두 점수가 모두 더 높은 사람이 있다는 뜻(탈락)이다. 탈락하지 않은 사람 중 완호보다 점수 합이 큰 사람 수 + 1이 완호의 석차가 된다.
    # 시간 복잡도: O(n log n)
    target_attitude_score, target_peer_score = scores[0]
    target_score = target_attitude_score + target_peer_score
    answer = 1

    max_peer_score = 0
    # 태도 점수가 같은 사람끼리는 서로 탈락시킬 수 없으므로 동료 평가 오름차순으로 정렬
    for attitude_score, peer_score in sorted(scores, key=lambda score: (-score[0], score[1])):
        if peer_score < max_peer_score:  # 앞에 두 점수 모두 더 높은 사람이 존재 → 탈락
            if attitude_score == target_attitude_score and peer_score == target_peer_score:
                return -1  # 완호와 같은 점수가 탈락했다면 완호도 탈락
            continue

        if attitude_score + peer_score > target_score:
            answer += 1
        max_peer_score = peer_score

    return answer
