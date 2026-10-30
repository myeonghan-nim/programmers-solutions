def solution(ingredient):
    # 스택에 재료를 쌓다가 위 네 개가 빵-야채-고기-빵이면 꺼내어 햄버거 하나로 센다
    # 시간 복잡도: O(N) (N: ingredient의 길이)
    stack, answer = [], 0
    for i in ingredient:
        stack.append(i)
        if stack[-4:] == [1, 2, 3, 1]:
            del stack[-4:]
            answer += 1
    return answer
