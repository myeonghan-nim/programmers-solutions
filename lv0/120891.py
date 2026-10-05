def solution(order):
    # 수를 문자열로 바꿔 3, 6, 9가 각각 몇 번 나오는지 세어 모두 더하면 박수 횟수다
    return sum(str(order).count(c) for c in "369")
