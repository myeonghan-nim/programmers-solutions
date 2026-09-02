def solution(cpr):
    # 심폐소생술의 올바른 순서 목록에서 각 동작이 몇 번째인지(index + 1) 찾아 담는다
    basic_order = ["check", "call", "pressure", "respiration", "repeat"]
    return [basic_order.index(action) + 1 for action in cpr]
