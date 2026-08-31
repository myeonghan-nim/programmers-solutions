def solution(n):
    # 피보나치 수를 "빠른 두 배 공식"으로 구한다: F(2k) = F(k)*(2*F(k+1) - F(k)), F(2k+1) = F(k)^2 + F(k+1)^2. n을 2진수로 읽으며 (a, b) = (F(m), F(m+1)) 쌍을 자릿수마다 두 배로 키워 가면 n번째까지 곧바로 도달한다.
    # 시간 복잡도: O(log n)
    mod = 1234567

    a, b = 0, 1
    for bit in bin(n)[2:]:
        c = (a * ((b << 1) - a)) % mod  # c = F(2m)
        d = (a * a + b * b) % mod  # d = F(2m+1)
        if bit == "0":
            a, b = c, d
        else:
            a, b = d, (c + d) % mod

    return a
