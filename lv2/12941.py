def solution(a, b):
    # 곱의 합을 가장 작게 만들려면 한쪽의 작은 수를 다른 쪽의 큰 수와 짝지어야 한다. 둘 다 오름차순으로 정렬한 뒤 a의 i번째와 b의 뒤에서 i번째를 곱해 더한다.
    # 시간 복잡도: O(n log n) (정렬)
    n = len(a)
    a.sort()
    b.sort()
    return sum([a[i] * b[n - 1 - i] for i in range(n)])
