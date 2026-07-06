def solution(k, room_number):
    parent = {}

    def find(x):
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
        parent[empty] = empty + 1
    return answer
