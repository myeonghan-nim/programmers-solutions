def solution(arr):
    # 각 원소 a를 a번씩 반복해 순서대로 이어 붙인다
    return [a for a in arr for _ in range(a)]
