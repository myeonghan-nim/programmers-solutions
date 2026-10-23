from math import lcm


def solution(signals):
    # 모든 신호등은 주기들의 최소공배수(L)마다 처음 상태로 돌아오므로 1초부터 L초까지만 보면 되고, 후보 시각은 주기가 가장 긴 신호등이 노란불인 순간으로 좁혀 나머지 신호등만 확인한다
    # 시간 복잡도: O(L / P * Y * n), P와 Y는 주기가 가장 긴 신호등의 주기와 노란불 지속 시간
    periods = [sum(signal) for signal in signals]
    total = lcm(*periods)
    g, y, _ = max(signals, key=sum)
    for base in range(0, total, g + y + _):
        for t in range(base + g + 1, base + g + y + 1):  # 주기가 가장 긴 신호등이 노란불인 시각
            if all(gi <= (t - 1) % p < gi + yi for (gi, yi, _), p in zip(signals, periods)):  # 시각 t는 주기 안에서 (t - 1) % p 번째 초이고, g ~ g + y - 1 번째 초가 노란불이다
                return t
    return -1  # L초 안에 없으면 그 뒤로도 같은 상태가 반복되므로 영원히 없다
