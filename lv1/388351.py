def solution(schedules, timelogs, startday):
    # 시각을 분 단위로 바꿔야 10분을 더해도 자리 올림이 맞으므로, 평일마다 출근 시각(분)이 희망 시각(분) + 10 이하인지 확인하고 모든 평일을 지킨 직원을 센다
    # 시간 복잡도: O(n)
    def to_minutes(time):
        return time // 100 * 60 + time % 100

    weekdays = [day for day in range(7) if (startday - 1 + day) % 7 < 5]  # (startday - 1 + day) % 7 은 day일차의 요일(0 월 ~ 6 일), 5 이상은 주말
    return sum(all(to_minutes(logs[day]) <= to_minutes(hope) + 10 for day in weekdays) for hope, logs in zip(schedules, timelogs))
