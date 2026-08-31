def solution(enroll, referral, seller, amount):
    # 각 판매원의 추천인을 부모로 기억해 두고, 판매 이익이 생길 때마다 10%를 떼어 부모에게 올려 보내는 과정을 그대로 따라간다. 이익이 한 단계마다 1/10로 줄어 금방 0원이 되므로 올라가는 횟수는 몇 번 안 된다.
    # 시간 복잡도: O(판매 기록 수) (기록당 올라가는 단계가 최대 5번 정도)
    index_by_name = {name: index for index, name in enumerate(enroll)}
    parent = [index_by_name[referrer] if referrer != "-" else -1 for referrer in referral]  # -1은 센터(민호)

    answer = [0] * len(enroll)
    for name, count in zip(seller, amount):
        current = index_by_name[name]
        profit = count * 100

        while current != -1 and profit > 0:
            commission = profit // 10  # 추천인에게 줄 10% (원 단위 아래는 버림)
            answer[current] += profit - commission

            if commission == 0:  # 1원 미만이면 더 이상 분배하지 않음
                break

            current = parent[current]
            profit = commission

    return answer
