def solution(board, moves):
    # 열마다 인형을 아래에서 위 순서의 스택으로 미리 만들어 두고, 집은 인형이 바구니 맨 위와 같으면 둘 다 없애고 2개를 센다
    # 시간 복잡도: O(n^2 + m), n은 격자 한 변, m은 크레인 작동 횟수
    columns = [[doll for doll in reversed(column) if doll] for column in zip(*board)]  # 빈칸(0)은 버려 맨 위 인형이 리스트 끝에 온다
    basket = []
    popped = 0
    for move in moves:
        column = columns[move - 1]  # moves는 1번부터 시작
        if not column:  # 인형이 없는 열에서는 아무 일도 일어나지 않는다
            continue
        doll = column.pop()
        if basket and basket[-1] == doll:
            basket.pop()
            popped += 2
        else:
            basket.append(doll)
    return popped
