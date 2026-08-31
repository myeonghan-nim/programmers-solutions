def solution(numbers):
    # 서로 다른 두 인덱스의 모든 짝의 합을 집합(set)에 넣어 중복을 없애고 정렬한다
    # 시간 복잡도: O(n²) — n이 최대 100이라 충분히 빠르다
    answer = set()
    for i in range(len(numbers)):
        for j in range(i + 1, len(numbers)):
            answer.add(numbers[i] + numbers[j])
    return sorted(answer)
