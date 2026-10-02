def solution(s1, s2):
    # 두 배열을 집합(set)으로 바꾸면 & 연산으로 공통 원소만 남길 수 있으므로 그 개수를 센다
    return len(set(s1) & set(s2))
