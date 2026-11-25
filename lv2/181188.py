def solution(targets):
    # 끝점이 빠른 폭격 미사일부터 보면서, 아직 요격되지 않은 미사일을 만나면 그 끝점 바로 앞에서 쏜다. 끝점이 가장 빠른 미사일은 어차피 요격해야 하고, 최대한 오른쪽에서 쏠수록 뒤따르는 미사일을 더 많이 함께 맞히기 때문이다
    # 시간 복잡도: O(n log n)
    count = 0
    last_shot = 0
    for start, end in sorted(targets, key=lambda target: target[1]):
        # 개구간이라 끝점 자체에서는 요격할 수 없으므로 실제 발사 위치는 end 바로 앞이고, start가 last_shot 이상인 미사일은 그 발사에 맞지 않는다
        if start >= last_shot:
            count += 1
            last_shot = end
    return count
