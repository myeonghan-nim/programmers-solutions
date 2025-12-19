def solution(cards1, cards2, goal):
    card1, card2 = 0, 0
    for word in goal:
        if card1 < len(cards1) and word == cards1[card1]:
            card1 += 1
        elif card2 < len(cards2) and word == cards2[card2]:
            card2 += 1
        else:
            return "No"
    return "Yes"
