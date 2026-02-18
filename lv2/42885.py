def solution(people, limit):
    people.sort()
    left, right = 0, len(people) - 1
    cnt = 0
    while left < right:
        remain = limit - people[right]
        if remain >= people[left]:
            left += 1
        cnt += 1
        right -= 1
    return cnt + (1 if left == right else 0)
