def solution(my_string, letter):
    # replace로 letter를 빈 문자열로 바꾸면 해당 문자가 모두 지워진다
    return my_string.replace(letter, "")
