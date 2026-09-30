def solution(picture, k):
    # 각 글자를 가로로 k번 반복해 늘린 줄을 만들고, 그렇게 만든 줄을 세로로도 k번씩 넣는다
    return ["".join(c * k for c in row) for row in picture for _ in range(k)]
