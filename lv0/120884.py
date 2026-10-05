def solution(chicken):
    # 쿠폰 10장을 서비스 1마리로 바꿀 때마다 새 쿠폰이 또 생기므로, 쿠폰이 10장 미만이 될 때까지 교환을 반복하며 서비스 수를 더한다
    service = 0
    coupons = chicken
    while coupons >= 10:
        exchanged = coupons // 10
        service += exchanged
        coupons = coupons % 10 + exchanged
    return service
