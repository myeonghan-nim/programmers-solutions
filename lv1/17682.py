import re


def solution(dart_result):
    # 정규식으로 "점수+영역+옵션" 세 덩어리를 뽑아 순서대로 누적한다. 스타상은 직전 점수도 2배로 만들어야 하므로 리스트에 담아 바로 앞 원소를 함께 고친다
    # 시간 복잡도: O(1) (기회가 3번으로 고정)
    scores = []
    for score, area, option in re.findall(r"(\d+)([SDT])([*#]?)", dart_result):
        scores.append(int(score) ** ("SDT".index(area) + 1))  # S, D, T는 각각 1, 2, 3제곱
        if option == "*":
            scores[-2:] = [s * 2 for s in scores[-2:]]  # 첫 기회면 scores[-2:]에 원소가 하나뿐이라 자기 자신만 2배가 된다
        elif option == "#":
            scores[-1] *= -1
    return sum(scores)
