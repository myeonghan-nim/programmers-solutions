def solution(a, b):
    # a를 오른쪽으로 k번 밀어 b가 된다면 b를 두 번 이어 붙인 b+b 안의 위치 k에서 a가 나타난다. find는 가장 앞 위치(최소 횟수)를 주고 없으면 -1을 주므로 그대로 답이 된다
    return (b + b).find(a)
