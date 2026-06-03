def solution(n, t, m, timetable):
    timeable = sorted([int(time[:2]) * 60 + int(time[3:]) for time in timetable])
    bus_time = 540
    crew_idx = 0
    for i in range(n):
        count = 0
        last_time = 0
        while crew_idx < len(timeable) and timeable[crew_idx] <= bus_time and count < m:
            count += 1
            last_time = timeable[crew_idx]
            crew_idx += 1
        if i == n - 1:
            if count < m:
                return f'{bus_time // 60:02d}:{bus_time % 60:02d}'
            else:
                last_time -= 1
                return f'{last_time // 60:02d}:{last_time % 60:02d}'
        bus_time += t
