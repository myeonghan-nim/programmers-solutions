def solution(s):
    # 공백 하나를 기준으로 나누면 연속 공백이 빈 문자열로 남아 다시 이어 붙일 때 공백 개수가 보존되므로, 단어마다 인덱스를 0부터 다시 세어 짝수 인덱스는 대문자, 홀수 인덱스는 소문자로 바꾼다
    # 시간 복잡도: O(len(s))
    return " ".join("".join(char.lower() if i % 2 else char.upper() for i, char in enumerate(word)) for word in s.split(" "))
