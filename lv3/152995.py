def solution(scores):
    target_attitude_score, target_peer_score = scores[0]
    target_score = target_attitude_score + target_peer_score
    answer = 1

    max_peer_score = 0
    for attitude_score, peer_score in sorted(scores, key=lambda score: (-score[0], score[1])):
        if peer_score < max_peer_score:
            if attitude_score == target_attitude_score and peer_score == target_peer_score:
                return -1
            continue

        if attitude_score + peer_score > target_score:
            answer += 1
        max_peer_score = peer_score

    return answer
