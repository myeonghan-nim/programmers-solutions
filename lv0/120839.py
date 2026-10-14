def solution(rsp):
    # 가위(2)는 바위(0)에, 바위(0)는 보(5)에, 보(5)는 가위(2)에 지므로 각 글자를 이기는 글자로 바꾼다
    win = {"2": "0", "0": "5", "5": "2"}
    return "".join(win[c] for c in rsp)
