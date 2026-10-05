def solution(s):
    # 딱 한 번만 나온 글자들만 골라 사전 순으로 정렬해 이어 붙인다
    return "".join(sorted(c for c in set(s) if s.count(c) == 1))
