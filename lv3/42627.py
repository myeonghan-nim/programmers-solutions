import heapq


def solution(jobs):
    n = len(jobs)
    jobs_by_request = sorted((request, duration, job_id) for job_id, (request, duration) in enumerate(jobs))
    waiting = []
    time = 0
    next_job = 0
    completed = 0
    total_turnaround = 0

    while completed < n:
        while next_job < n and jobs_by_request[next_job][0] <= time:
            request, duration, job_id = jobs_by_request[next_job]
            heapq.heappush(waiting, (duration, request, job_id))
            next_job += 1

        if waiting:
            duration, request, _ = heapq.heappop(waiting)
            time += duration
            total_turnaround += time - request
            completed += 1
        else:
            time = jobs_by_request[next_job][0]

    return total_turnaround // n
