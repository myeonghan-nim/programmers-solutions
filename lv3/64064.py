def solution(user_id, banned_id):
    # 불량 아이디마다 매핑 가능한 사용자 후보를 구한 뒤, 이미 뽑힌 사용자 집합을 비트마스크(사용자 한 명당 2진수 한 자리)로 표현해 겹치지 않게 한 명씩 배정한다. 최종적으로 서로 다른 사용자 집합이 몇 가지인지 세면 된다.
    # 시간 복잡도: O(banned 수 * 2^(user 수) * user 수) (user가 최대 8명이라 작음)
    def match(user, ban):
        return len(user) == len(ban) and all(b == '*' or u == b for u, b in zip(user, ban))

    candidates = [[i for i, user in enumerate(user_id) if match(user, ban)] for ban in banned_id]

    states = {0}
    for cand in candidates:
        next_states = set()
        for mask in states:
            for i in cand:
                bit = 1 << i
                if mask & bit == 0:  # 아직 뽑히지 않은 사용자만 배정 가능
                    next_states.add(mask | bit)
        states = next_states

    return len(states)
