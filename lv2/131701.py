def solution(elements):
    # 원형 수열은 배열을 두 번 이어 붙이면 일반 수열처럼 다룰 수 있다. 앞에서부터의 누적 합(prefix)을 만들어 두면 어떤 구간의 합도 뺄셈 한 번으로 나온다. 길이 1~n의 모든 구간 합을 집합에 넣어 서로 다른 값의 개수를 센다.
    # 시간 복잡도: O(n^2)
    n = len(elements)
    extended = elements * 2

    prefix = [0] * (2 * n + 1)
    for i, value in enumerate(extended, 1):
        prefix[i] = prefix[i - 1] + value

    sums = set()
    for length in range(1, n + 1):
        for start in range(n):
            sums.add(prefix[start + length] - prefix[start])  # 구간 [start, start+length)의 합

    return len(sums)
