import heapq


def solution(jobs):
    # 요청 시각 순으로 작업을 대기열에 넣고, 매번 우선순위가 가장 높은 작업부터 처리하는 시뮬레이션. 힙(가장 작은 값이 먼저 나오는 자료구조)에 (소요 시간, 요청 시각, 번호) 튜플을 넣으면 문제의 우선순위가 그대로 구현된다.
    # 시간 복잡도: O(n log n)
    n = len(jobs)
    jobs_by_request = sorted((request, duration, job_id) for job_id, (request, duration) in enumerate(jobs))
    waiting = []
    time = 0
    next_job = 0
    completed = 0
    total_turnaround = 0

    while completed < n:
        # 현재 시각까지 요청된 작업을 모두 대기열에 넣는다
        while next_job < n and jobs_by_request[next_job][0] <= time:
            request, duration, job_id = jobs_by_request[next_job]
            heapq.heappush(waiting, (duration, request, job_id))
            next_job += 1

        if waiting:
            duration, request, _ = heapq.heappop(waiting)
            time += duration
            total_turnaround += time - request  # 반환 시간 = 종료 시각 - 요청 시각
            completed += 1
        else:
            time = jobs_by_request[next_job][0]  # 대기 작업이 없으면 다음 요청 시각으로 점프

    return total_turnaround // n  # 평균의 정수 부분
