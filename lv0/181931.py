def solution(a, d, included):
    # 등차수열의 i번째 항(i는 0부터)은 a + d * i이므로, included가 True인 자리의 항만 골라 더한다
    return sum(a + d * i for i, ok in enumerate(included) if ok)
