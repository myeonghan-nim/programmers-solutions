def solution(cards1, cards2, goal):
    # 각 뭉치에서 다음에 쓸 카드 위치를 가리키며(투 포인터), goal의 단어가 어느 한 뭉치의 다음 카드와 같으면 그 위치를 한 칸 옮긴다
    card1, card2 = 0, 0
    for word in goal:
        if card1 < len(cards1) and word == cards1[card1]:
            card1 += 1
        elif card2 < len(cards2) and word == cards2[card2]:
            card2 += 1
        else:
            return "No"  # 두 뭉치의 다음 카드 어느 쪽과도 다르면 만들 수 없다
    return "Yes"
