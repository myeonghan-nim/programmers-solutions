def solution(h1, m1, s1, h2, m2, s2):
    # 초침은 분침을 3600/59초마다, 시침을 43200/719초마다 따라잡는다. 그래서 0시부터 t초까지 울린 횟수는 나눗셈 두 번으로 구할 수 있고, 답은 (끝 시각까지의 횟수) - (시작 시각까지의 횟수)에 시작 시각 정각의 알람을 더한 값이다
    # 시간 복잡도: O(1)
    def alarms_until(seconds):
        # 0시 정각의 알람 1번을 더하고, 12시 정각은 분침·시침 겹침이 동시에 일어나 두 번 세어지므로 1번 뺀다. 719와 708(= 59 * 12)이 서로소라 두 겹침이 동시에 일어나는 때는 0시와 12시뿐이다
        return seconds * 59 // 3600 + seconds * 719 // 43200 + 1 - (seconds >= 43200)

    start = h1 * 3600 + m1 * 60 + s1
    end = h2 * 3600 + m2 * 60 + s2
    rings_at_start = start * 59 % 3600 == 0 or start * 719 % 43200 == 0
    return alarms_until(end) - alarms_until(start) + rings_at_start
