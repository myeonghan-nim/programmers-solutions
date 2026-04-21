def solution(user_id, banned_id):
    def match(user, ban):
        return len(user) == len(ban) and all(b == '*' or u == b for u, b in zip(user, ban))

    candidates = [[i for i, user in enumerate(user_id) if match(user, ban)] for ban in banned_id]

    states = {0}
    for cand in candidates:
        next_states = set()
        for mask in states:
            for i in cand:
                bit = 1 << i
                if mask & bit == 0:
                    next_states.add(mask | bit)
        states = next_states

    return len(states)
