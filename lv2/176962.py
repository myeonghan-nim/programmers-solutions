def solution(plans):
    # 시작 시각순으로 과제를 스택에 쌓고, 다음 과제가 시작하기 전까지 남는 시간으로 스택 맨 위(지금 과제, 그다음은 가장 최근에 멈춘 과제)부터 끝낸다
    # 시간 복잡도: O(n log n), n은 과제 수
    schedule = sorted((int(start[:2]) * 60 + int(start[3:]), name, int(playtime)) for name, start, playtime in plans)
    answer = []
    unfinished = []  # [이름, 남은 시간]을 담으며 맨 위가 지금 하고 있거나 가장 최근에 멈춘 과제다
    for index, (start, name, playtime) in enumerate(schedule):
        unfinished.append([name, playtime])
        # 마지막 과제 뒤로는 새 과제가 없어 쌓인 과제를 모두 끝낼 수 있다
        free_time = schedule[index + 1][0] - start if index + 1 < len(schedule) else float("inf")
        while unfinished and unfinished[-1][1] <= free_time:
            free_time -= unfinished[-1][1]
            answer.append(unfinished.pop()[0])
        if unfinished:
            unfinished[-1][1] -= free_time  # 끝내지 못한 맨 위 과제는 남은 시간만큼만 진행하고 멈춘다
    return answer
