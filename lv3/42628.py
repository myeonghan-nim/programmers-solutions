import heapq


def solution(operations):
    min_heap = []
    max_heap = []
    alive = [False] * len(operations)

    def prune(heap, sign):
        while heap and not alive[heap[0][1]]:
            heapq.heappop(heap)

    for uid, operation in enumerate(operations):
        command, raw = operation.split()
        value = int(raw)

        if command == "I":
            heapq.heappush(min_heap, (value, uid))
            heapq.heappush(max_heap, (-value, uid))
            alive[uid] = True
            continue

        if value == 1:
            prune(max_heap, -1)
            if max_heap:
                _, uid = heapq.heappop(max_heap)
                alive[uid] = False
        else:
            prune(min_heap, 1)
            if min_heap:
                _, uid = heapq.heappop(min_heap)
                alive[uid] = False

    prune(min_heap, 1)
    prune(max_heap, -1)

    if not min_heap:
        return [0, 0]

    return [-max_heap[0][0], min_heap[0][0]]
