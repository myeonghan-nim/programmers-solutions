def solution(arr):
    # 스택 꼭대기와 같은 값이 오면 꼭대기를 빼고, 다르거나 비어 있으면 쌓는 과정을 반복한다; 다 비면 [-1]
    stk = []
    for x in arr:
        if stk and stk[-1] == x:
            stk.pop()
        else:
            stk.append(x)
    return stk or [-1]
