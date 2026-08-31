from collections import Counter


def solution(n, stages):
    # 실패율 = 그 스테이지에 멈춘 사람 수 ÷ 그 스테이지에 도달한 사람 수. 1번부터 차례로 올라가며 도달 인원(remaining)에서 멈춘 인원을 빼 나간다
    # 시간 복잡도: O(len(stages) + n log n)
    remaining, counter = len(stages), Counter(stages)  # counter: 스테이지별로 멈춘 사람 수
    failure_rate = {}
    for stage in range(1, n + 1):
        count = counter.get(stage, 0)
        if not remaining:
            failure_rate[stage] = 0  # 도달한 사람이 없으면 실패율은 0
        else:
            failure_rate[stage] = count / remaining
        remaining -= count  # 여기서 멈춘 사람은 다음 스테이지에 도달하지 못했다
    # 실패율 내림차순 정렬. 같으면 정렬이 원래 순서를 지켜 줘서 번호가 작은 쪽이 먼저 온다
    return [k for k, _ in sorted(failure_rate.items(), key=lambda item: item[1], reverse=True)]
