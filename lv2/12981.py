def solution(n, words):
    # 단어를 순서대로 보며 (1) 이미 나온 단어인지 (2) 앞 단어의 끝 글자로 시작하는지 검사한다. i번째(0부터 셈) 단어에서 틀리면 말한 사람은 i % n + 1번, 그 사람의 i // n + 1번째 차례다.
    # 시간 복잡도: O(단어 수)
    answer = [0, 0]
    used_words = set()  # 지금까지 나온 단어 모음 (중복 검사를 빠르게 하기 위함)
    for i in range(len(words)):
        if i > 0 and (words[i] in used_words or words[i - 1][-1] != words[i][0]):
            answer = [(i % n) + 1, (i // n) + 1]
            break
        used_words.add(words[i])
    return answer
