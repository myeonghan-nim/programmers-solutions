def solution(arr, n):
    # 길이가 홀수면 짝수 인덱스에, 짝수면 홀수 인덱스에 n을 더한다 (더할 자리는 인덱스 홀짝이 길이 홀짝과 다른 곳)
    return [x + n if i % 2 != len(arr) % 2 else x for i, x in enumerate(arr)]
