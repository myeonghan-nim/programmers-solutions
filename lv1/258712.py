from collections import Counter


def solution(friends, gifts):
    # (준 사람, 받은 사람) 쌍별 횟수와 선물 지수를 센 뒤, 모든 두 사람 쌍에 규칙을 적용해 다음 달에 받을 선물 수를 구한다
    # 시간 복잡도: O(G + F^2) (G: gifts의 길이, F: friends의 길이)
    given = Counter(tuple(gift.split()) for gift in gifts)
    index = Counter()
    for (giver, receiver), count in given.items():
        index[giver] += count
        index[receiver] -= count

    received = Counter()
    for i, a in enumerate(friends):
        for b in friends[i + 1 :]:
            # 주고받은 수를 먼저 비교하고, 같으면(기록이 없는 경우 포함) 선물 지수로 비교한다
            key_a = (given[a, b], index[a])
            key_b = (given[b, a], index[b])
            if key_a > key_b:
                received[a] += 1
            elif key_b > key_a:
                received[b] += 1
    return max(received.values(), default=0)
