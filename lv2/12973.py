def solution(s):
    # 문자를 차곡차곡 쌓다가(스택: 마지막에 넣은 것부터 꺼내는 구조), 방금 쌓은 문자와 같은 문자가 또 오면 짝이 되므로 둘 다 지운다. 끝까지 처리한 뒤 아무것도 남지 않으면 전부 제거할 수 있는 문자열이다.
    # 시간 복잡도: O(n)
    if len(s) < 2:
        return 0

    stack = []
    for char in s:
        if stack and stack[-1] == char:
            stack.pop()
        else:
            stack.append(char)

    return 1 if not stack else 0
