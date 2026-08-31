def solution(play_time, adv_time, logs):
    # 시각을 모두 초 단위 숫자로 바꾼 뒤, 시청 기록의 시작 초에 +1 / 끝 초에 -1을 찍고 한 번 누적하면 각 초의 시청자 수, 한 번 더 누적하면 처음부터 그 초까지의 누적 재생시간이 된다. 광고 시작 시각을 1초씩 옮기며 구간 합이 최대인 곳을 찾는다.
    # 시간 복잡도: O(전체 재생시간(초) + 기록 수)
    def time_to_seconds(time_str):
        h, m, s = map(int, time_str.split(':'))
        return h * 3600 + m * 60 + s

    def seconds_to_time(seconds):
        h = seconds // 3600
        m = (seconds % 3600) // 60
        s = seconds % 60
        return f"{h:02d}:{m:02d}:{s:02d}"

    play_time = time_to_seconds(play_time)
    adv_time = time_to_seconds(adv_time)
    total_time = [0] * (play_time + 1)

    for log in logs:
        start, end = log.split('-')
        start_sec = time_to_seconds(start)
        end_sec = time_to_seconds(end)
        total_time[start_sec] += 1
        total_time[end_sec] -= 1

    for i in range(1, play_time):  # 1차 누적: 각 초를 보고 있는 시청자 수
        total_time[i] += total_time[i - 1]

    for i in range(1, play_time):  # 2차 누적: 0초부터 i초까지의 누적 재생시간
        total_time[i] += total_time[i - 1]

    max_watch_time = total_time[adv_time - 1]
    max_start_time = 0

    for start in range(1, play_time - adv_time + 1):
        end = start + adv_time - 1
        watch_time = total_time[end] - total_time[start - 1]
        if watch_time > max_watch_time:  # 같은 값이면 더 빠른 시작 시각을 유지
            max_watch_time = watch_time
            max_start_time = start

    return seconds_to_time(max_start_time)
