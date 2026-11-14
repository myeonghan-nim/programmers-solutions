from math import isqrt


def solution(n):
    # 에라토스테네스의 체: 2부터 차례로 소수의 배수를 지워 나가면 남는 수가 소수다. 합성수는 √n 이하의 약수를 반드시 가지므로 √n까지만 지우면 된다
    # 시간 복잡도: O(n log log n)
    is_prime = [True] * (n + 1)
    is_prime[0] = is_prime[1] = False
    for number in range(2, isqrt(n) + 1):
        if is_prime[number]:
            # number * number보다 작은 배수는 더 작은 소수의 배수로 이미 지워졌으므로 제곱부터 지운다
            multiples = range(number * number, n + 1, number)
            is_prime[number * number :: number] = [False] * len(multiples)
    return sum(is_prime)
