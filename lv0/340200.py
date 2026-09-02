def solution(nickname):
    # 규칙 순서대로 문자를 바꾼 뒤(l은 I, w는 vv, W는 VV, O는 0), 길이가 4보다 짧으면 o를 붙이고 8보다 길면 8글자로 자른다
    fixed = nickname.replace("l", "I").replace("w", "vv").replace("W", "VV").replace("O", "0")
    fixed += "o" * (4 - len(fixed))
    return fixed[:8]
