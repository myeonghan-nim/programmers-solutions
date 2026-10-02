def solution(babbling):
    # 낼 수 있는 네 발음을 각각 공백 한 칸으로 바꿔 보고 전부 지워져 공백만 남으면 발음할 수 있는 단어다. 공백으로 바꾸는 이유는 지운 자리 앞뒤 글자가 붙어 새 발음처럼 보이는 것을 막기 위해서다
    count = 0
    for word in babbling:
        for sound in ("aya", "ye", "woo", "ma"):
            word = word.replace(sound, " ")
        if word.strip() == "":
            count += 1
    return count
