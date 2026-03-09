def solution(n, words):
    answer = [0, 0]
    dictionary = set()
    for i in range(len(words)):
        if i > 0 and (words[i] in dictionary or words[i - 1][-1] != words[i][0]):
            answer = [(i % n) + 1, (i // n) + 1]
            break
        dictionary.add(words[i])
    return answer
