def solution(s):
    # 숫자는 리스트에 쌓고 "Z"가 나오면 마지막에 쌓은 숫자를 꺼내 버린 뒤, 남은 숫자를 모두 더한다
    stack = []
    for token in s.split():
        if token == "Z":
            stack.pop()
        else:
            stack.append(int(token))
    return sum(stack)
