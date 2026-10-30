def solution(number, limit, power):
    # 각 i의 배수마다 약수 개수를 1씩 더해 모든 번호의 약수 개수를 구한 뒤 limit 초과분은 power로 바꿔 합산한다
    # 시간 복잡도: O(N log N) (N: number)
    count = [0] * (number + 1)
    for i in range(1, number + 1):
        for j in range(i, number + 1, i):
            count[j] += 1
    return sum(c if c <= limit else power for c in count[1:])
