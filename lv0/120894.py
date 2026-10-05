def solution(numbers):
    # 영어 단어를 해당 숫자 글자로 하나씩 replace로 바꿔 나가면 숫자만 남은 문자열이 되고, 이를 정수로 바꾼다
    words = ["zero", "one", "two", "three", "four", "five", "six", "seven", "eight", "nine"]
    for digit, word in enumerate(words):
        numbers = numbers.replace(word, str(digit))
    return int(numbers)
