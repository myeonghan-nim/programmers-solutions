def solution(answers):
    # 세 사람의 찍는 방식은 일정한 패턴의 반복이므로, i번 문제는 패턴의 i % (패턴 길이) 위치와 비교해 맞힌 개수를 센다
    # 시간 복잡도: O(n)
    patterns = [[1, 2, 3, 4, 5], [2, 1, 2, 3, 2, 4, 2, 5], [3, 3, 1, 1, 2, 2, 4, 4, 5, 5]]
    counts = [0, 0, 0]
    for i, answer in enumerate(answers):
        for j, pattern in enumerate(patterns):
            if answer == pattern[i % len(pattern)]:
                counts[j] += 1
    max_count = max(counts)
    return [i + 1 for i, count in enumerate(counts) if count == max_count]  # 최고 점수인 사람들의 번호(1부터), 오름차순
