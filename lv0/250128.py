def solution(numbers, our_score, score_list):
    # n번 학생의 실제 성적은 score_list[n - 1]이므로, 문의한 학생마다 가채점 점수와 비교해 같으면 "Same" 다르면 "Different"를 담는다
    return ["Same" if score_list[n - 1] == score else "Different" for n, score in zip(numbers, our_score)]
