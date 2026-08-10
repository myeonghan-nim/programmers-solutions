from collections import deque


def solution(rc, operations):
    c = len(rc[0])

    left = deque(row[0] for row in rc)
    right = deque(row[-1] for row in rc)
    mid = deque(deque(row[1:-1]) for row in rc)

    for op in operations:
        if op == "ShiftRow":
            left.appendleft(left.pop())
            right.appendleft(right.pop())
            mid.appendleft(mid.pop())
        else:
            if c > 2:
                mid[0].appendleft(left.popleft())
                right.appendleft(mid[0].pop())
                mid[-1].append(right.pop())
                left.append(mid[-1].popleft())
            else:
                right.appendleft(left.popleft())
                left.append(right.pop())

    return [[lv] + list(mv) + [rv] for lv, mv, rv in zip(left, mid, right)]
