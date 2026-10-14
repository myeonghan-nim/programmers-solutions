def solution(n):
    # 곱이 n인 순서쌍의 개수는 n의 약수 개수와 같고, 약수는 (i, n // i)로 짝을 이루므로 제곱근까지만 나눠 보며 2개씩 센다(제곱수면 짝이 같아 1개)
    count = 0
    for i in range(1, int(n**0.5) + 1):
        if n % i == 0:
            count += 1 if i * i == n else 2
    return count
