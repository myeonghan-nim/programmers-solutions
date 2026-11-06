def solution(numbers, hand):
    # 키패드를 4행 3열 좌표로 보고 두 엄지의 위치를 갱신해 가며, 가운데 열은 맨해튼 거리가 더 가까운 손(같으면 주로 쓰는 손)으로 누른다
    # 시간 복잡도: O(n)
    position = {"L": (3, 0), "R": (3, 2)}  # 시작 위치는 *와 #
    preferred = hand[0].upper()  # "left" → "L", "right" → "R"
    answer = []
    for number in numbers:
        row, col = divmod((number or 11) - 1, 3)  # 0은 11번째 칸(맨 아래 가운데)으로 취급
        if col == 0:
            thumb = "L"
        elif col == 2:
            thumb = "R"
        else:
            left, right = (abs(r - row) + abs(c - col) for r, c in (position["L"], position["R"]))
            if left == right:
                thumb = preferred
            else:
                thumb = "L" if left < right else "R"
        position[thumb] = (row, col)
        answer.append(thumb)
    return "".join(answer)
