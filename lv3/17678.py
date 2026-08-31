def solution(n, t, m, timetable):
    # 크루 도착 시각을 분 단위로 바꿔 정렬한 뒤 버스 운행을 그대로 시뮬레이션한다. 마지막 버스에 자리가 남으면 버스 도착 시각에 오면 되고, 꽉 차면 마지막 탑승자보다 1분 일찍 와서 그 자리를 가로챈다.
    # 시간 복잡도: O(k log k) (k = len(timetable))
    timetable = sorted([int(time[:2]) * 60 + int(time[3:]) for time in timetable])
    bus_time = 540  # 첫 버스 09:00 = 540분
    crew_idx = 0
    for i in range(n):
        count = 0
        last_time = 0
        # 이 버스 도착 전에 줄 선 크루를 정원(m)까지 태운다
        while crew_idx < len(timetable) and timetable[crew_idx] <= bus_time and count < m:
            count += 1
            last_time = timetable[crew_idx]
            crew_idx += 1
        if i == n - 1:  # 마지막 버스
            if count < m:
                return f'{bus_time // 60:02d}:{bus_time % 60:02d}'
            else:
                last_time -= 1  # 만석: 마지막 탑승자보다 1분 먼저 줄 서기
                return f'{last_time // 60:02d}:{last_time % 60:02d}'
        bus_time += t
