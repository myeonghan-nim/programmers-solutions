def solution(num, k):
    # 숫자를 문자열로 바꾸면 find로 k가 처음 나오는 위치(없으면 -1)를 알 수 있고, 자리 수는 1부터 세므로 1을 더한다
    position = str(num).find(str(k))
    return position + 1 if position != -1 else -1
