from collections import Counter


def solution(array):
    # 값별 등장 횟수를 센 뒤 가장 많이 나온 두 값을 비교해, 1등이 2등과 동률이면 -1, 아니면 1등 값을 돌려준다
    top = Counter(array).most_common(2)
    if len(top) > 1 and top[0][1] == top[1][1]:
        return -1
    return top[0][0]
