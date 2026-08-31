def solution(s):
    # 문자열에서 "110"을 전부 뽑아낸 뒤(글자를 쌓아 가며 끝 3글자가 "110"이면 제거), 남은 문자열의 마지막 '0' 바로 뒤에 뽑아 둔 "110"들을 몰아넣으면 사전 순 최소가 된다. 남은 문자열엔 "110"이 없어 마지막 '0' 뒤는 전부 '1'이고, 그 '1'들보다 "110"이 앞서기 때문.
    # 시간 복잡도: O(전체 문자열 길이)
    answer = []
    target = '110'

    for x in s:
        stack = []
        count = 0

        for c in x:
            stack.append(c)
            if c == '0' and len(stack) >= 3 and stack[-2] == '1' and stack[-3] == '1':  # 끝 3글자가 "110"
                stack.pop()
                stack.pop()
                stack.pop()
                count += 1

        rest = ''.join(stack)
        insert_idx = rest.rfind('0') + 1  # '0'이 없으면 0이 되어 맨 앞에 삽입
        answer.append(rest[:insert_idx] + target * count + rest[insert_idx:])

    return answer
