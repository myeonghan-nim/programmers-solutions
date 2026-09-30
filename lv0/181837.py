def solution(order):
    # 주문 문자열에 "cafelatte"가 들어 있으면 5000원, 나머지(아메리카노 종류와 "anything")는 모두 4500원이므로 그대로 더한다
    return sum(5000 if "cafelatte" in menu else 4500 for menu in order)
