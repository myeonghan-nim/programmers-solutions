def solution(before, after):
    # 순서만 바꿔 만들 수 있다는 건 두 문자열을 정렬했을 때 같다는 뜻이다
    return 1 if sorted(before) == sorted(after) else 0
