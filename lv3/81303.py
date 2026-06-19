def solution(n, k, cmd):
    answer = ['O'] * n
    prev_row = [i - 1 for i in range(n)]
    next_row = [i + 1 for i in range(n)]
    next_row[n - 1] = -1

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
                current = prev_idx
        elif op == 'U':
            for _ in range(int(c[2:])):
                current = prev_row[current]
        else:
            restored = deleted.pop()
            answer[restored] = 'O'

            prev_idx = prev_row[restored]
            next_idx = next_row[restored]

            if prev_idx != -1:
                next_row[prev_idx] = restored
            if next_idx != -1:
                prev_row[next_idx] = restored

    return ''.join(answer)
