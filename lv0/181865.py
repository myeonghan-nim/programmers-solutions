def solution(binomial):
    # "a op b"를 공백으로 쪼개 두 수와 연산자를 얻고, 연산자에 맞는 계산 결과를 돌려준다
    a, op, b = binomial.split()
    a, b = int(a), int(b)
    return a + b if op == "+" else a - b if op == "-" else a * b
