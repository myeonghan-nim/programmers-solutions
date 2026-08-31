def solution(people, limit):
    # 몸무게를 정렬한 뒤, 가장 무거운 사람을 태울 때 가장 가벼운 사람이 같이 탈 수 있으면 태운다. 무거운 사람의 짝으로 가장 가벼운 사람조차 못 타면 아무도 못 타므로, 이 선택이 항상 최선이다.
    # 시간 복잡도: O(n log n) (정렬)
    people.sort()
    left, right = 0, len(people) - 1
    cnt = 0
    while left < right:
        remain = limit - people[right]
        if remain >= people[left]:  # 가장 가벼운 사람이 같이 탈 수 있으면 함께 태운다
            left += 1
        cnt += 1
        right -= 1
    return cnt + (1 if left == right else 0)  # 마지막에 한 명이 남았으면 보트 한 대 추가
