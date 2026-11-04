def solution(s):
    # 영단어를 해당 숫자 문자로 차례대로 치환하고 정수로 바꾼다: 한 영단어가 다른 영단어의 일부가 되는 경우가 없어 순서 상관없이 안전하다
    # 시간 복잡도: O(n)
    words = ["zero", "one", "two", "three", "four", "five", "six", "seven", "eight", "nine"]
    for digit, word in enumerate(words):
        s = s.replace(word, str(digit))
    return int(s)
