def solution(survey, choices):
    # 선택지 1~3은 survey 앞 글자 유형에 4 - choice점, 5~7은 뒷 글자 유형에 choice - 4점을 더한 뒤, 지표별로 점수가 높은 유형(같으면 사전순 앞)을 고른다
    # 시간 복잡도: O(n)
    score = {t: 0 for t in "RTCFJMAN"}
    for (disagree, agree), choice in zip(survey, choices):
        if choice < 4:
            score[disagree] += 4 - choice
        else:
            score[agree] += choice - 4  # choice가 4(모르겠음)면 0점이 더해져 결과에 영향 없음
    return "".join(min(pair, key=lambda t: (-score[t], t)) for pair in ("RT", "CF", "JM", "AN"))  # 점수 내림차순, 같으면 사전순
