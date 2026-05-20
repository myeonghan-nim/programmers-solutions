def solution(enroll, referral, seller, amount):
    index_by_name = {name: index for index, name in enumerate(enroll)}
    parent = [index_by_name[referrer] if referrer != "-" else -1 for referrer in referral]

    answer = [0] * len(enroll)
    for name, count in zip(seller, amount):
        current = index_by_name[name]
        profit = count * 100

        while current != -1 and profit > 0:
            commission = profit // 10
            answer[current] += profit - commission

            if commission == 0:
                break

            current = parent[current]
            profit = commission

    return answer
