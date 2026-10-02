def solution(my_string):
    # 뺄셈 "- 4"를 "+ -4"로 바꾸면 수식 전체가 덧셈만 남으므로, " + "를 기준으로 잘라 낸 숫자들을 전부 더하면 된다
    return sum(int(x) for x in my_string.replace("- ", "+ -").split(" + "))
