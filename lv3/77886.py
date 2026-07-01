def solution(s):
    answer = []
    target = '110'

    for x in s:
        stack = []
        count = 0

        for c in x:
            stack.append(c)
            if c == '0' and len(stack) >= 3 and stack[-2] == '1' and stack[-3] == '1':
                stack.pop()
                stack.pop()
                stack.pop()
                count += 1

        rest = ''.join(stack)
        insert_idx = rest.rfind('0') + 1
        answer.append(rest[:insert_idx] + target * count + rest[insert_idx:])

    return answer
