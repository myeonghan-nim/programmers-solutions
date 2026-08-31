def solution(s):
    # 마나커(Manacher) 알고리즘: 모든 위치를 중심으로 하는 팰린드롬 반지름을 앞서 계산한 대칭 결과를 재활용하며 한 번의 순회로 구한다. 문자 사이에 '#'을 끼워 홀수/짝수 길이 팰린드롬을 한꺼번에 처리한다.
    # 시간 복잡도: O(n)
    t = "#" + "#".join(s) + "#"
    n = len(t)
    radius = [0] * n

    center = 0
    right = 0  # 지금까지 찾은 팰린드롬이 덮는 가장 오른쪽 위치

    for i in range(n):
        mirror = 2 * center - i  # center 기준 i의 대칭 위치

        if i < right:
            # 대칭 위치의 결과를 재활용(단, 덮인 범위를 넘지는 못함)
            radius[i] = min(right - i, radius[mirror])

        # 남은 부분은 직접 비교하며 반지름을 확장
        while i - radius[i] - 1 >= 0 and i + radius[i] + 1 < n and t[i - radius[i] - 1] == t[i + radius[i] + 1]:
            radius[i] += 1

        if i + radius[i] > right:
            center = i
            right = i + radius[i]

    # 변형 문자열에서의 반지름 = 원래 문자열에서의 팰린드롬 길이
    return max(radius)
