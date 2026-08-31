def solution(s):
    # 공백 기준으로 단어를 나눠, 알파벳으로만 된 단어는 첫 글자만 대문자로(title), 숫자로 시작하는 단어는 전부 소문자로 바꾼다. split(" ")은 연속된 공백을 빈 문자열로 남기므로 다시 합치면 공백이 그대로 보존된다.
    words = s.split(" ")
    for i in range(len(words)):
        if words[i].isalpha():
            words[i] = words[i].title()
        else:
            words[i] = words[i].lower()
    return " ".join(words)
