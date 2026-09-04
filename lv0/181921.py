def solution(l, r):
    # l부터 r까지 모든 수를 확인해 자릿수가 0과 5로만 이루어진 수를 모으고, 하나도 없으면 [-1]을 돌려준다
    result = [x for x in range(l, r + 1) if set(str(x)) <= {"0", "5"}]
    return result or [-1]
