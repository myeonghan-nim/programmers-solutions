def solution(arr, k):
    # 처음 나온 수만 순서대로 남기고(dict.fromkeys는 중복을 없애도 순서를 지킨다) 앞의 k개를 뽑은 뒤, 모자라면 -1로 채운다
    picked = list(dict.fromkeys(arr))[:k]
    return picked + [-1] * (k - len(picked))
