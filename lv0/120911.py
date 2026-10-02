def solution(my_string):
    # lower로 모두 소문자로 바꾸고 sorted로 글자를 알파벳 순으로 정렬한 뒤 join으로 다시 문자열로 합친다
    return "".join(sorted(my_string.lower()))
