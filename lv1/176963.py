def solution(name, yearning, photo):
    # 이름별 그리움 점수를 딕셔너리로 만들고, 사진마다 인물 점수를 더한다 (점수가 없는 인물은 0점)
    # 시간 복잡도: O(N + P) (N: name의 길이, P: 모든 사진 속 인물 수의 합)
    score = dict(zip(name, yearning))
    return [sum(score.get(person, 0) for person in people) for people in photo]
