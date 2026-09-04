def solution(arr):
    # 각 수마다 스택 끝의 크거나 같은 원소를 모두 빼낸 뒤 자신을 넣으면 문제의 반복 규칙과 같아진다
    stk = []
    for num in arr:
        while stk and stk[-1] >= num:
            stk.pop()
        stk.append(num)
    return stk
