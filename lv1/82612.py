def solution(price, money, count):
    # 총 이용료는 price × (1 + 2 + ... + count) = price × count × (count + 1) ÷ 2 이고, 돈이 충분하면 0을 반환한다
    # 시간 복잡도: O(1)
    return max(0, price * count * (count + 1) // 2 - money)
