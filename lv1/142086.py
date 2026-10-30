def solution(s):
    # 글자별 마지막 등장 위치를 딕셔너리에 갱신하며 현재 위치와의 거리를 구한다
    # 시간 복잡도: O(N) (N: s의 길이)
    last, answer = {}, []
    for i, c in enumerate(s):
        answer.append(i - last[c] if c in last else -1)
        last[c] = i
    return answer
