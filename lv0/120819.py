def solution(money):
    # 5500원으로 나눈 몫이 살 수 있는 잔 수, 나머지가 남는 돈이다
    return [money // 5500, money % 5500]
