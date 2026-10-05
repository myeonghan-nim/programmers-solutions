def solution(lines):
    # 수직선을 길이 1짜리 칸으로 쪼개, 각 선분이 덮는 칸마다 덮인 횟수를 세고 두 번 이상 덮인 칸의 개수를 더한다
    covered = [0] * 200
    for start, end in lines:
        for i in range(start, end):
            covered[i + 100] += 1
    return sum(c >= 2 for c in covered)
