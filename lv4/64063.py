def solution(k, room_number):
    # 방 번호마다 "그 번호부터 봤을 때 처음 나오는 빈 방"을 딕셔너리로 기억한다. 방을 배정하면 그 방의 다음 빈 방 후보를 바로 뒤 번호로 이어 붙인다. k가 최대 10^12라 배열 대신 실제로 건드린 번호만 저장한다.
    # 시간 복잡도: O(n * α(n))  (n = 고객 수, 사실상 O(n))
    parent = {}

    def find(x):
        # 빈 방이 나올 때까지 따라간 뒤, 지나온 번호를 모두 결과에 직접 연결(경로 압축)
        path = []
        while x in parent:
            path.append(x)
            x = parent[x]
        for node in path:
            parent[node] = x
        return x

    answer = []
    for room in room_number:
        empty = find(room)
        answer.append(empty)
        parent[empty] = empty + 1  # 방금 찬 방의 다음 빈 방 후보는 바로 뒤 번호
    return answer
