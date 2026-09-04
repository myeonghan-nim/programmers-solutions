def solution(n, control):
    # 각 문자가 n을 얼마나 바꾸는지 표로 만들어 두고, 모든 변화량을 더해 n에 적용한다
    moves = {"w": 1, "s": -1, "d": 10, "a": -10}
    return n + sum(moves[ch] for ch in control)
