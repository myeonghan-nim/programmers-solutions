from collections import deque


def solution(rc, operations):
    # 행렬을 왼쪽 열 / 오른쪽 열 / 가운데(행별 덱) 세 부분으로 나눠 들고 있으면 ShiftRow와 Rotate 모두 양 끝의 원소 몇 개만 옮기는 O(1) 작업이 된다.
    # 시간 복잡도: O(연산 수 + 행렬 크기)
    c = len(rc[0])

    left = deque(row[0] for row in rc)
    right = deque(row[-1] for row in rc)
    mid = deque(deque(row[1:-1]) for row in rc)

    for op in operations:
        if op == "ShiftRow":  # 세 부분 모두 마지막 행을 맨 앞으로
            left.appendleft(left.pop())
            right.appendleft(right.pop())
            mid.appendleft(mid.pop())
        else:  # Rotate: 테두리만 시계 방향 한 칸, 모서리 근처 값 4개만 이동하면 됨
            if c > 2:
                mid[0].appendleft(left.popleft())
                right.appendleft(mid[0].pop())
                mid[-1].append(right.pop())
                left.append(mid[-1].popleft())
            else:  # 가운데가 없으면 왼쪽/오른쪽 열끼리 직접 주고받음
                right.appendleft(left.popleft())
                left.append(right.pop())

    return [[lv] + list(mv) + [rv] for lv, mv, rv in zip(left, mid, right)]
