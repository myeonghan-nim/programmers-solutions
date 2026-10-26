def solution(bandage, health, attacks):
    # 공격 사이의 회복 시간(gap초)마다 초당 회복량 × gap에 완주 횟수(gap // t)만큼 추가 회복량을 더해 한 번에 회복하고, 공격을 받아 0 이하가 되면 -1을 반환한다
    # 시간 복잡도: O(A) (A: attacks의 길이)
    t, x, y = bandage
    current = health
    last_time = 0
    for attack_time, damage in attacks:
        gap = attack_time - last_time - 1  # 공격당하는 순간에는 회복하지 못하므로 사이 시간만 센다
        current = min(health, current + gap * x + gap // t * y)
        current -= damage
        if current <= 0:
            return -1
        last_time = attack_time
    return current
