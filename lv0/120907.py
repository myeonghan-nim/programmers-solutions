def solution(quiz):
    # 수식을 공백으로 쪼개 x, 연산자, y, "=", z 다섯 조각으로 나눈 뒤, 직접 계산한 값이 z와 같으면 "O" 다르면 "X"를 담는다
    answer = []
    for expression in quiz:
        x, op, y, _, z = expression.split()
        value = int(x) + int(y) if op == "+" else int(x) - int(y)
        answer.append("O" if value == int(z) else "X")
    return answer
