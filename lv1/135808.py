def solution(k, m, score):
    # 내림차순 정렬 후 m개씩 묶으면 각 상자의 마지막 원소가 최저 점수이므로 그 합에 m을 곱한다
    # 시간 복잡도: O(N log N) (N: score의 길이)
    score.sort(reverse=True)
    return sum(score[m - 1 :: m]) * m
