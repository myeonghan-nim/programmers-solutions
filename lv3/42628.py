import heapq


def solution(operations):
    # 최솟값용 힙과 최댓값용 힙(부호 반전)에 같은 값을 넣어 두고, 삭제는 alive 표시만 꺼서 처리한다(지연 삭제). 반대쪽 힙에 남은 죽은 원소는 꼭대기에 올라왔을 때 걷어낸다.
    # 시간 복잡도: O(n log n)
    min_heap = []
    max_heap = []
    alive = [False] * len(operations)  # 연산 번호(uid)로 각 원소의 생존 여부 관리

    def prune(heap):
        # 힙 꼭대기에 쌓인 이미 삭제된 원소들을 제거
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

        if value == 1:  # 최댓값 삭제
            prune(max_heap)
            if max_heap:
                _, top_uid = heapq.heappop(max_heap)
                alive[top_uid] = False
        else:  # 최솟값 삭제
            prune(min_heap)
            if min_heap:
                _, top_uid = heapq.heappop(min_heap)
                alive[top_uid] = False

    prune(min_heap)
    prune(max_heap)

    if not min_heap:
        return [0, 0]

    return [-max_heap[0][0], min_heap[0][0]]
