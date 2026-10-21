def solution(price):
    # 금액 구간별 할인율을 적용하되, 정수 연산(가격 x 남는 비율 // 100)으로 계산해 소수 오차 없이 버림한다
    if price >= 500000:
        return price * 80 // 100
    if price >= 300000:
        return price * 90 // 100
    if price >= 100000:
        return price * 95 // 100
    return price
