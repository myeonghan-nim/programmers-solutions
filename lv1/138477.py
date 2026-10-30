import heapq


def solution(k, score):
    # 최소 힙에 점수를 넣고 k개를 넘으면 최솟값을 빼서 상위 k개만 유지하며 매일 힙의 최솟값을 기록한다
    # 시간 복잡도: O(N log K) (N: score의 길이)
    heap, answer = [], []
    for s in score:
        heapq.heappush(heap, s)
        if len(heap) > k:
            heapq.heappop(heap)
        answer.append(heap[0])
    return answer
