def solution(score):
    # 평균 비교는 두 점수의 합 비교와 같으므로, 각 학생의 등수는 자기보다 합이 큰 학생 수에 1을 더한 값이다
    totals = [sum(s) for s in score]
    return [1 + sum(other > total for other in totals) for total in totals]
