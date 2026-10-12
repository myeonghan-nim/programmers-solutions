def solution(numbers, k):
    # 한 명을 건너뛰므로 공은 던질 때마다 두 칸씩 이동하고, k번째로 던지는 사람의 위치는 2 * (k - 1)을 인원수로 나눈 나머지 인덱스다
    return numbers[2 * (k - 1) % len(numbers)]
