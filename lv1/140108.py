def solution(s):
    # 기준 글자 x가 없으면 새로 잡고, x와 다른 글자의 개수가 같아지는 순간 하나의 조각으로 세어 기준을 초기화한다
    # 시간 복잡도: O(N) (N: s의 길이)
    answer, x, same, diff = 0, "", 0, 0
    for c in s:
        if not x:
            x, answer = c, answer + 1
        if c == x:
            same += 1
        else:
            diff += 1
        if same == diff:
            x, same, diff = "", 0, 0
    return answer
