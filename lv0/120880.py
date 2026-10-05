def solution(numlist, n):
    # n과의 거리(abs)가 작은 순으로 정렬하되, 거리가 같으면 -x를 두 번째 기준으로 삼아 큰 수가 앞에 오게 한다
    return sorted(numlist, key=lambda x: (abs(x - n), -x))
