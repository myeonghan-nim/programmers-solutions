def solution(n, k, cmd):
    # 행마다 바로 위/아래 행 번호를 배열로 기억해 연결 리스트처럼 쓴다. 삭제(C)는 위아래 이웃끼리 이어 붙이고, 복구(Z)는 삭제 순서를 쌓아 둔 목록에서 가장 최근 것을 꺼내 제자리에 다시 끼워 넣으면 되어 명령마다 거의 O(1)이다.
    # 시간 복잡도: O(n + 명령 수 + 이동량 총합) (이동량 총합은 100만 이하로 제한됨)
    answer = ['O'] * n
    prev_row = [i - 1 for i in range(n)]
    next_row = [i + 1 for i in range(n)]
    next_row[n - 1] = -1  # -1은 표 밖(이웃 없음)을 뜻함

    current = k
    deleted = []
    for c in cmd:
        op = c[0]
        if op == 'D':
            for _ in range(int(c[2:])):
                current = next_row[current]
        elif op == 'C':
            answer[current] = 'X'
            deleted.append(current)

            prev_idx = prev_row[current]
            next_idx = next_row[current]

            if prev_idx != -1:
                next_row[prev_idx] = next_idx
            if next_idx != -1:
                prev_row[next_idx] = prev_idx
                current = next_idx
            else:
                current = prev_idx  # 마지막 행을 지웠으면 바로 윗 행을 선택
        elif op == 'U':
            for _ in range(int(c[2:])):
                current = prev_row[current]
        else:  # Z: 가장 최근에 삭제된 행 복구 (선택된 행은 그대로)
            restored = deleted.pop()
            answer[restored] = 'O'

            prev_idx = prev_row[restored]
            next_idx = next_row[restored]

            if prev_idx != -1:
                next_row[prev_idx] = restored
            if next_idx != -1:
                prev_row[next_idx] = restored

    return ''.join(answer)
