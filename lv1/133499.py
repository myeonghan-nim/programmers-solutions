def solution(babbling):
    # 같은 발음이 연달아 나오는 단어를 거른 뒤 네 발음을 공백으로 치환해 글자가 남지 않으면 발음 가능으로 센다
    # 시간 복잡도: O(N × L) (N: babbling의 길이, L: 단어의 최대 길이)
    sounds = ["aya", "ye", "woo", "ma"]
    answer = 0
    for word in babbling:
        if any(s * 2 in word for s in sounds):
            continue
        for s in sounds:
            word = word.replace(s, " ")
        answer += word.strip() == ""
    return answer
