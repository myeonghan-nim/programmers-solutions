def solution(polynomial):
    # " + "로 나눈 각 항이 x로 끝나면 x의 계수에, 아니면 상수에 더해 모은 뒤 규칙(계수 1 생략, 0인 부분 생략, 상수는 뒤)에 맞춰 문자열로 만든다
    x_coef = const = 0
    for term in polynomial.split(" + "):
        if term.endswith("x"):
            x_coef += int(term[:-1] or 1)
        else:
            const += int(term)
    x_part = "" if x_coef == 0 else "x" if x_coef == 1 else f"{x_coef}x"
    if x_part and const:
        return f"{x_part} + {const}"
    return x_part or str(const)
