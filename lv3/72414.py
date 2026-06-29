def solution(play_time, adv_time, logs):
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

    for i in range(1, play_time):
        total_time[i] += total_time[i - 1]

    for i in range(1, play_time):
        total_time[i] += total_time[i - 1]

    max_viewers = total_time[adv_time - 1]
    max_start_time = 0

    for start in range(1, play_time - adv_time + 1):
        end = start + adv_time - 1
        viewers = total_time[end] - total_time[start - 1]
        if viewers > max_viewers:
            max_viewers = viewers
            max_start_time = start

    return seconds_to_time(max_start_time)
