def solution(left, right):
    # 약수는 (a, n/a) 쌍으로 묶이므로 개수가 홀수인 수는 제곱수뿐이다: 제곱수면 빼고 아니면 더한다
    # 시간 복잡도: O(n)
    return sum(-n if int(n ** 0.5) ** 2 == n else n for n in range(left, right + 1))
