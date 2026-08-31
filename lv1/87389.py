def solution(n):
    # n % x == 1 이려면 x는 n-1을 나누어 떨어뜨려야 한다(단 x는 2 이상). 따라서 답은 n-1의 2 이상인 가장 작은 약수(= 가장 작은 소인수)
    # 시간 복잡도: O(√n)
    answer = n - 1

    if not (answer % 2):
        return 2
    if not (answer % 3):
        return 3

    i = 5
    while i * i <= answer:  # 2, 3을 확인했으니 남은 약수 후보는 6k±1 꼴(5, 7, 11, 13, ...)뿐
        if not (answer % i):
            return i
        j = i + 2
        if not (answer % j):
            return j
        i += 6

    return answer  # 제곱근까지 약수가 없으면 n-1은 소수이므로 n-1 자신이 답
