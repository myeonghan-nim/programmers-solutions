def solution(s, n):
    # 각 알파벳을 대소문자별 시작 문자("A" 또는 "a")로부터의 거리로 바꾼 뒤 n을 더하고 26으로 나눈 나머지를 취하면 "z" 다음이 "a"로 이어지며, 공백은 그대로 둔다
    # 시간 복잡도: O(len(s))
    answer = []
    for char in s:
        if char == " ":
            answer.append(char)
        else:
            base = ord("a") if char.islower() else ord("A")
            answer.append(chr((ord(char) - base + n) % 26 + base))
    return "".join(answer)
