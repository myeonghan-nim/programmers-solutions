def solution(code):
    # code를 한 글자씩 읽으며 "1"이 나오면 mode를 0과 1 사이로 바꾸고, 다른 문자는 인덱스의 짝홀이 mode와 같을 때만 모은다. 모은 결과가 비어 있으면 "EMPTY"를 돌려준다
    mode = 0
    ret = ""
    for idx, ch in enumerate(code):
        if ch == "1":
            mode = 1 - mode
        elif idx % 2 == mode:
            ret += ch
    return ret or "EMPTY"
