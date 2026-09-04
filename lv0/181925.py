def solution(num_log):
    # 연속한 두 값의 차이(+1, -1, +10, -10)가 어떤 키를 눌렀는지 알려주므로 차이를 문자로 바꿔 이어 붙인다
    keys = {1: "w", -1: "s", 10: "d", -10: "a"}
    return "".join(keys[b - a] for a, b in zip(num_log, num_log[1:]))
