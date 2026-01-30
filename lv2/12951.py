def solution(s):
    words = s.split(" ")
    for i in range(len(words)):
        if words[i].isalpha():
            words[i] = words[i].title()
        else:
            words[i] = words[i].lower()
    return " ".join(words)
